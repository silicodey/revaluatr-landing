#!/usr/bin/env python3
"""
RevaluatR Landing Page Backend - Flask Server
Simple backend to collect waitlist emails and store them in CSV
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import csv
import os
from datetime import datetime
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__, static_folder='.')
CORS(app)  # Enable CORS for API requests

# File to store waitlist signups
WAITLIST_FILE = 'waitlist.csv'

# Initialize CSV file if it doesn't exist
if not os.path.exists(WAITLIST_FILE):
    with open(WAITLIST_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Name', 'Email', 'Company', 'IP Address'])

# Email and Google Sheets configuration
EMAIL_ENABLED = os.environ.get('EMAIL_ENABLED', 'false').lower() == 'true'
SHEETS_ENABLED = os.environ.get('SHEETS_ENABLED', 'false').lower() == 'true'

def send_email_notification(name, email, company, timestamp):
    """Send email notification for new signup"""
    if not EMAIL_ENABLED:
        return

    try:
        sender_email = os.environ.get('SMTP_EMAIL')
        sender_password = os.environ.get('SMTP_PASSWORD')
        recipient_email = os.environ.get('NOTIFICATION_EMAIL')

        if not all([sender_email, sender_password, recipient_email]):
            print("Email credentials not configured")
            return

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f'New RevaluatR Waitlist Signup: {name}'

        body = f"""
New waitlist signup!

Name: {name}
Email: {email}
Company: {company or 'N/A'}
Timestamp: {timestamp}

--
RevaluatR Automated Notification
"""

        msg.attach(MIMEText(body, 'plain'))

        # Use Gmail SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"Email notification sent for: {email}")

    except Exception as e:
        print(f"Error sending email: {str(e)}")

def save_to_google_sheets(name, email, company, timestamp, ip_address):
    """Save signup to Google Sheets"""
    if not SHEETS_ENABLED:
        return

    try:
        # Get credentials from environment variable
        creds_json = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
        spreadsheet_id = os.environ.get('GOOGLE_SHEETS_ID')

        if not creds_json or not spreadsheet_id:
            print("Google Sheets not configured")
            return

        # Parse credentials
        creds_dict = json.loads(creds_json)
        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )

        # Connect to Google Sheets
        client = gspread.authorize(creds)
        sheet = client.open_by_key(spreadsheet_id).sheet1

        # Append row
        sheet.append_row([timestamp, name, email, company, ip_address])

        print(f"Saved to Google Sheets: {email}")

    except Exception as e:
        print(f"Error saving to Google Sheets: {str(e)}")

@app.route('/')
def index():
    """Serve the landing page"""
    return send_from_directory('.', 'index.html')

@app.route('/api/waitlist', methods=['POST'])
def add_to_waitlist():
    """Handle waitlist signup"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('name') or not data.get('email'):
            return jsonify({'error': 'Name and email are required'}), 400
        
        # Get client IP
        ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
        
        # Prepare data
        timestamp = data.get('timestamp', datetime.utcnow().isoformat())
        name = data.get('name', '').strip()
        email = data.get('email', '').strip().lower()
        company = data.get('company', '').strip()
        
        # Check if email already exists
        if os.path.exists(WAITLIST_FILE):
            with open(WAITLIST_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['Email'].lower() == email:
                        return jsonify({'message': 'Email already registered'}), 200
        
        # Save to CSV
        with open(WAITLIST_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, name, email, company, ip_address])

        # Send email notification
        send_email_notification(name, email, company, timestamp)

        # Save to Google Sheets
        save_to_google_sheets(name, email, company, timestamp, ip_address)

        # Log signup
        print(f"New waitlist signup: {name} ({email}) from {company or 'N/A'}")

        return jsonify({
            'message': 'Successfully added to waitlist',
            'email': email
        }), 200
        
    except Exception as e:
        print(f"Error processing waitlist signup: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/waitlist/count', methods=['GET'])
def get_waitlist_count():
    """Get total number of waitlist signups"""
    try:
        if not os.path.exists(WAITLIST_FILE):
            return jsonify({'count': 0}), 200
        
        with open(WAITLIST_FILE, 'r', encoding='utf-8') as f:
            # Subtract 1 for header row
            count = sum(1 for line in f) - 1
        
        return jsonify({'count': max(0, count)}), 200
        
    except Exception as e:
        print(f"Error getting waitlist count: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

if __name__ == '__main__':
    # Get port from environment variable (Railway/Heroku) or default to 8000
    port = int(os.environ.get('PORT', 8000))

    print("=" * 60)
    print("RevaluatR Landing Page Server")
    print("=" * 60)
    print(f"Waitlist file: {WAITLIST_FILE}")
    print(f"Server starting on http://localhost:{port}")
    print("Press CTRL+C to stop")
    print("=" * 60)

    # Run the server
    app.run(host='0.0.0.0', port=port, debug=False)
