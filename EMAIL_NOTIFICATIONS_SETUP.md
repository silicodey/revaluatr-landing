# 📧 Email Notifications Setup Guide
## Get Notified When Someone Joins Your Waitlist

---

## Overview

You'll configure email notifications so you receive an email every time someone signs up for your waitlist.

**Current status:** Your backend already has email notification code built-in! We just need to configure it.

---

## PART 1: Choose Email Service

You have several options:

### Option A: Gmail (Easiest, Free)
✅ **Best for:** Quick setup, personal use
✅ **Cost:** Free
⚠️ **Limit:** 500 emails/day
⚠️ **Security:** Requires "App Password"

### Option B: SendGrid (Recommended for Production)
✅ **Best for:** Professional use, scalability
✅ **Cost:** Free tier (100 emails/day)
✅ **Features:** Better deliverability, analytics
✅ **No daily limits** on free tier

### Option C: Mailgun
✅ **Best for:** Developers
✅ **Cost:** Free tier (5,000 emails/month)
✅ **Features:** API-based, reliable

**I recommend Option A (Gmail) for getting started, then upgrade to SendGrid later.**

---

## OPTION A: Gmail Setup (Easiest)

### Step 1: Enable 2-Factor Authentication

1. **Go to:** https://myaccount.google.com/security
2. **Find:** "2-Step Verification"
3. **Click:** "Get started"
4. **Follow prompts** to enable 2FA (required for App Passwords)

### Step 2: Create App Password

1. **Go to:** https://myaccount.google.com/apppasswords
2. **Select app:** "Mail"
3. **Select device:** "Other (Custom name)"
4. **Enter name:** "RevaluatR Backend"
5. **Click:** "Generate"
6. **Copy the 16-character password** (looks like: `abcd efgh ijkl mnop`)

**Important:** Save this password! You can't see it again.

### Step 3: Configure Render Environment Variables

1. **Go to Render Dashboard:** https://dashboard.render.com
2. **Select your web service:** "revaluatr-landing"
3. **Click:** Settings tab
4. **Scroll to:** "Environment Variables"
5. **Add these variables:**

```
EMAIL_ENABLED=true
SMTP_EMAIL=your-email@gmail.com
SMTP_PASSWORD=abcd efgh ijkl mnop
NOTIFICATION_EMAIL=your-email@gmail.com
```

**Replace with your actual values:**
- `SMTP_EMAIL`: Your Gmail address
- `SMTP_PASSWORD`: The 16-character app password from Step 2
- `NOTIFICATION_EMAIL`: Where you want to receive notifications (can be same or different)

6. **Click:** "Save Changes"

### Step 4: Redeploy Service

After adding environment variables, Render will automatically redeploy your service. Wait 2-3 minutes.

### Step 5: Test Email Notifications

1. **Visit your landing page:** https://revaluatr.com (or current URL)
2. **Fill out the form** with test data
3. **Submit**
4. **Check your email** - you should receive a notification!

**Email will look like:**
```
Subject: New RevaluatR Waitlist Signup: John Doe

New waitlist signup!

Name: John Doe
Email: john@example.com
Company: Example Corp
Timestamp: 2024-11-25T10:30:00

--
RevaluatR Automated Notification
```

✅ **Gmail setup complete!**

---

## OPTION B: SendGrid Setup (Professional)

### Step 1: Create SendGrid Account

1. **Go to:** https://signup.sendgrid.com
2. **Sign up** for free account
3. **Verify your email**
4. **Complete onboarding** questions

### Step 2: Verify Sender Identity

1. **Go to:** Settings → Sender Authentication
2. **Click:** "Verify a Single Sender"
3. **Fill in your details:**
   - From Name: `RevaluatR`
   - From Email: `notifications@revaluatr.com` (or your email)
   - Reply To: Your email
   - Company: Your company name
4. **Click:** "Create"
5. **Check your email** and verify

### Step 3: Create API Key

1. **Go to:** Settings → API Keys
2. **Click:** "Create API Key"
3. **Name:** `RevaluatR Backend`
4. **Permissions:** "Full Access" (or "Mail Send" only)
5. **Click:** "Create & View"
6. **Copy the API key** (starts with `SG.`)

**Important:** Save this key! You can't see it again.

### Step 4: Update Backend Code

The current code uses SMTP (Gmail). For SendGrid, we need to update it.

**I'll create an updated version of `server.py` that supports both Gmail and SendGrid.**

### Step 5: Configure Render Environment Variables

```
EMAIL_ENABLED=true
EMAIL_PROVIDER=sendgrid
SENDGRID_API_KEY=SG.your-api-key-here
NOTIFICATION_EMAIL=your-email@example.com
FROM_EMAIL=notifications@revaluatr.com
FROM_NAME=RevaluatR
```

### Step 6: Update requirements.txt

Add SendGrid to dependencies:
```
sendgrid>=6.10.0
```

---

## OPTION C: Mailgun Setup

### Step 1: Create Mailgun Account

1. **Go to:** https://signup.mailgun.com
2. **Sign up** for free account
3. **Verify email**

### Step 2: Get API Credentials

1. **Go to:** Settings → API Keys
2. **Copy:** Private API Key
3. **Note:** Your domain (e.g., `sandboxXXX.mailgun.org`)

### Step 3: Configure Environment Variables

```
EMAIL_ENABLED=true
EMAIL_PROVIDER=mailgun
MAILGUN_API_KEY=your-api-key
MAILGUN_DOMAIN=sandboxXXX.mailgun.org
NOTIFICATION_EMAIL=your-email@example.com
FROM_EMAIL=notifications@sandboxXXX.mailgun.org
```

---

## Email Notification Features

### What's Included

Your backend already sends:
- ✅ **Name** of person who signed up
- ✅ **Email address**
- ✅ **Company name** (if provided)
- ✅ **Timestamp** of signup
- ✅ **IP address** (for fraud detection)

### Customize Email Template

**Edit `server.py` lines 54-64** to customize the email:

```python
body = f"""
New waitlist signup! 🎉

Name: {name}
Email: {email}
Company: {company or 'N/A'}
Timestamp: {timestamp}

Total signups: [You can add count here]

--
RevaluatR Automated Notification
"""
```

**Make it fancier with HTML:**

```python
body_html = f"""
<html>
<body style="font-family: Arial, sans-serif;">
  <h2 style="color: #0018A8;">New Waitlist Signup! 🎉</h2>
  <table style="border-collapse: collapse; width: 100%;">
    <tr>
      <td style="padding: 10px; border: 1px solid #ddd;"><strong>Name:</strong></td>
      <td style="padding: 10px; border: 1px solid #ddd;">{name}</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #ddd;"><strong>Email:</strong></td>
      <td style="padding: 10px; border: 1px solid #ddd;">{email}</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #ddd;"><strong>Company:</strong></td>
      <td style="padding: 10px; border: 1px solid #ddd;">{company or 'N/A'}</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #ddd;"><strong>Time:</strong></td>
      <td style="padding: 10px; border: 1px solid #ddd;">{timestamp}</td>
    </tr>
  </table>
  <p style="color: #666; font-size: 12px; margin-top: 20px;">
    RevaluatR Automated Notification
  </p>
</body>
</html>
"""
```

---

## Advanced Features

### 1. Send Welcome Email to User

Add this function to `server.py`:

```python
def send_welcome_email(user_email, user_name):
    """Send welcome email to new signup"""
    if not EMAIL_ENABLED:
        return
    
    try:
        msg = MIMEMultipart()
        msg['From'] = os.environ.get('SMTP_EMAIL')
        msg['To'] = user_email
        msg['Subject'] = 'Welcome to RevaluatR!'
        
        body = f"""
Hi {user_name},

Thank you for joining the RevaluatR waitlist!

We're building an institutional-grade automated valuation engine for German commercial real estate. You'll be among the first to know when we launch.

In the meantime:
- Follow us on LinkedIn: [your link]
- Visit our website: https://revaluatr.com
- Questions? Reply to this email

Best regards,
The RevaluatR Team
"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(os.environ.get('SMTP_EMAIL'), os.environ.get('SMTP_PASSWORD'))
            server.send_message(msg)
        
        print(f"Welcome email sent to: {user_email}")
    except Exception as e:
        print(f"Error sending welcome email: {str(e)}")
```

Then call it in the `/api/waitlist` endpoint:
```python
# After saving to CSV
send_welcome_email(email, name)
```

### 2. Daily Summary Email

Send a daily digest of all signups:

```python
def send_daily_summary():
    """Send daily summary of signups"""
    # Count today's signups
    # Send email with summary
    pass
```

Set up a cron job on Render to run this daily.

### 3. Slack Notifications

Instead of (or in addition to) email, send to Slack:

```python
import requests

def send_slack_notification(name, email, company):
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if not webhook_url:
        return
    
    message = {
        "text": f"🎉 New waitlist signup!",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*New Signup*\n*Name:* {name}\n*Email:* {email}\n*Company:* {company or 'N/A'}"
                }
            }
        ]
    }
    
    requests.post(webhook_url, json=message)
```

---

## Troubleshooting

### Emails not sending

**Check Render logs:**
1. Render Dashboard → Your Service → Logs
2. Look for errors like:
   - `Error sending email: ...`
   - `Email credentials not configured`

**Common issues:**
- ❌ **Wrong password:** Make sure you used App Password, not regular password
- ❌ **2FA not enabled:** Required for Gmail App Passwords
- ❌ **Environment variables not set:** Check Render settings
- ❌ **Typo in email:** Double-check SMTP_EMAIL

### Emails going to spam

**For Gmail:**
- Use your actual Gmail address as sender
- Don't send too many emails too fast

**For SendGrid:**
- Verify your sender identity
- Set up domain authentication (SPF, DKIM)
- Warm up your sending (start slow)

### Gmail blocking login

- **Enable "Less secure app access"** (not recommended)
- **Use App Password** (recommended)
- **Check Google account security alerts**

---

## Email Delivery Best Practices

### 1. Don't Send Too Many
- **Gmail limit:** 500/day
- **SendGrid free:** 100/day
- **Mailgun free:** 5,000/month

### 2. Use Professional From Address
- ✅ `notifications@revaluatr.com`
- ❌ `noreply@gmail.com`

### 3. Include Unsubscribe Link
For welcome emails to users:
```
To unsubscribe, click here: [link]
```

### 4. Monitor Bounce Rate
- High bounce rate = bad sender reputation
- Keep email list clean
- Remove invalid addresses

---

## Testing Checklist

- [ ] Environment variables set in Render
- [ ] Service redeployed after adding variables
- [ ] Test signup on landing page
- [ ] Email received within 1 minute
- [ ] Email not in spam folder
- [ ] Email contains correct information
- [ ] Render logs show "Email notification sent"

---

## 🎉 You're All Set!

After setup, you'll receive an email every time someone joins your waitlist!

**What you get:**
- ✅ Instant notifications
- ✅ All signup details
- ✅ No need to check Render dashboard
- ✅ Professional appearance

**Next steps:**
1. Choose email provider (Gmail or SendGrid)
2. Set up environment variables
3. Test with a signup
4. Customize email template (optional)

---

## Quick Reference

### Gmail Environment Variables
```bash
EMAIL_ENABLED=true
SMTP_EMAIL=your-email@gmail.com
SMTP_PASSWORD=your-app-password
NOTIFICATION_EMAIL=your-email@gmail.com
```

### SendGrid Environment Variables
```bash
EMAIL_ENABLED=true
EMAIL_PROVIDER=sendgrid
SENDGRID_API_KEY=SG.your-key
NOTIFICATION_EMAIL=your-email@example.com
FROM_EMAIL=notifications@revaluatr.com
FROM_NAME=RevaluatR
```

### Test Command
```bash
curl -X POST https://api.revaluatr.com/api/waitlist \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","company":"Test Co"}'
```
