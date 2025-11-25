# 🚀 RevaluatR Deployment Guide
## Frontend: GitHub Pages | Backend: Render

---

## 📋 Overview

This guide will help you deploy:
- **Frontend** (HTML/CSS/JS) → GitHub Pages (free, static hosting)
- **Backend** (Flask API) → Render (free tier, supports Python)

---

## PART 1: Deploy Backend to Render (Do This First!)

### Step 1.1: Sign Up for Render
1. Go to [https://render.com](https://render.com)
2. Click "Get Started for Free"
3. Sign up with your GitHub account (recommended)

### Step 1.2: Create a New Web Service
1. In Render dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository:
   - Click "Connect account" if not already connected
   - Find and select your `RevaluatR Landing` repository
3. Configure the service:
   - **Name**: `revaluatr-backend` (or any name you prefer)
   - **Region**: Choose closest to your users (e.g., Frankfurt for Europe)
   - **Branch**: `main`
   - **Root Directory**: Leave blank
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT server:app`
   - **Instance Type**: `Free`

### Step 1.3: Add Environment Variables (Optional)
In the "Environment" section, you can add:
- `EMAIL_ENABLED=false` (set to true if you want email notifications)
- `SHEETS_ENABLED=false` (set to true if you want Google Sheets integration)

### Step 1.4: Deploy!
1. Click **"Create Web Service"**
2. Wait 2-5 minutes for deployment to complete
3. Once deployed, you'll see a URL like: `https://revaluatr-backend.onrender.com`
4. **COPY THIS URL** - you'll need it for the frontend!

### Step 1.5: Test Your Backend
Open your browser and visit:
```
https://your-backend-url.onrender.com/api/health
```
You should see:
```json
{"status": "healthy", "timestamp": "..."}
```

✅ **Backend is now live!**

---

## PART 2: Deploy Frontend to GitHub Pages

### Step 2.1: Update Frontend with Backend URL
1. Open `index-github.html` in your editor
2. Find line 382 where it says:
   ```javascript
   const API_URL = 'YOUR_RENDER_BACKEND_URL_HERE';
   ```
3. Replace with your actual Render URL (from Step 1.4):
   ```javascript
   const API_URL = 'https://revaluatr-backend.onrender.com';
   ```
4. Save the file

### Step 2.2: Rename File for GitHub Pages
```bash
mv index-github.html index.html
```
This replaces your local version with the GitHub Pages version.

### Step 2.3: Commit and Push to GitHub
```bash
git add index.html
git commit -m "Deploy to GitHub Pages with Render backend"
git push origin main
```

### Step 2.4: Enable GitHub Pages
1. Go to your GitHub repository in the browser
2. Click **Settings** → **Pages** (in left sidebar)
3. Under "Source", select:
   - **Branch**: `main`
   - **Folder**: `/ (root)`
4. Click **Save**
5. Wait 1-2 minutes for deployment

### Step 2.5: Get Your Live URL
GitHub will show your URL at the top:
```
Your site is live at https://[your-username].github.io/[repo-name]/
```

✅ **Frontend is now live!**

---

## PART 3: Test Everything

### Test 1: Visit Your Live Site
Open your GitHub Pages URL in a browser.

### Test 2: Submit the Form
1. Fill in name, email, and company
2. Click "Join Waitlist"
3. You should see a green success message

### Test 3: Check Backend Logs (Render)
1. Go to Render dashboard
2. Click on your web service
3. Click "Logs" tab
4. You should see: `New waitlist signup: [name] ([email]) from [company]`

### Test 4: Download Waitlist Data
The waitlist is stored in `waitlist.csv` on Render. To access it:
1. In Render dashboard, go to your service
2. Click "Shell" tab
3. Run: `cat waitlist.csv`
4. You'll see all signups!

---

## 🎯 Your Live URLs

After deployment, you'll have:

| Service | URL | Purpose |
|---------|-----|---------|
| **Frontend** | `https://[username].github.io/[repo]/` | Public landing page |
| **Backend API** | `https://revaluatr-backend.onrender.com` | Handles form submissions |
| **Health Check** | `https://revaluatr-backend.onrender.com/api/health` | Verify backend is running |
| **Waitlist Count** | `https://revaluatr-backend.onrender.com/api/waitlist/count` | See total signups |

---

## 🔧 Important Notes

### Free Tier Limitations

**Render Free Tier:**
- ✅ Unlimited requests
- ✅ 750 hours/month (plenty for a landing page)
- ⚠️ Spins down after 15 minutes of inactivity
- ⚠️ First request after spin-down takes ~30 seconds

**GitHub Pages:**
- ✅ Unlimited bandwidth
- ✅ Always fast (CDN)
- ✅ Custom domain support

### Handling Render Spin-Down
When backend spins down, the first form submission might timeout. Solutions:
1. **Keep it warm**: Use a service like [UptimeRobot](https://uptimerobot.com) to ping your backend every 5 minutes
2. **Show loading message**: The frontend already has a loader, users just need to wait
3. **Upgrade to paid**: $7/month keeps it always-on

---

## 📊 Accessing Your Waitlist Data

### Option 1: Via Render Shell
1. Render Dashboard → Your Service → Shell
2. Run: `cat waitlist.csv`
3. Copy/paste into Excel

### Option 2: Download via API (Advanced)
Add this endpoint to `server.py`:
```python
@app.route('/api/waitlist/export', methods=['GET'])
def export_waitlist():
    return send_file(WAITLIST_FILE, as_attachment=True)
```
Then visit: `https://your-backend.onrender.com/api/waitlist/export`

### Option 3: Set Up Google Sheets (Recommended)
Follow the instructions in the original README to enable Google Sheets sync.

---

## 🎨 Custom Domain (Optional)

### For GitHub Pages:
1. Buy domain (e.g., revaluatr.com)
2. Add CNAME record pointing to `[username].github.io`
3. In GitHub Settings → Pages, add custom domain
4. Enable HTTPS

### For Render Backend:
1. In Render dashboard, go to Settings
2. Add custom domain (e.g., api.revaluatr.com)
3. Update DNS with provided CNAME

---

## 🐛 Troubleshooting

### Frontend loads but form doesn't work
- Check browser console for errors
- Verify API_URL is correct in index.html
- Check Render backend is running (visit /api/health)

### Backend shows "Application failed to respond"
- Check Render logs for errors
- Verify requirements.txt has all dependencies
- Ensure start command is correct

### CORS errors in browser
- Backend already has CORS enabled
- If issues persist, check Render logs

---

## ✅ Deployment Checklist

- [ ] Backend deployed to Render
- [ ] Backend health check works
- [ ] Frontend updated with backend URL
- [ ] Frontend pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Live site loads correctly
- [ ] Form submission works
- [ ] Success message appears
- [ ] Data appears in waitlist.csv (check Render shell)

---

## 🎉 You're Live!

Share your landing page:
- **Landing Page**: `https://[username].github.io/[repo]/`
- **Email**: Include in Deutsche Bank communications
- **Social**: Share on LinkedIn, Twitter, etc.

---

## 📞 Need Help?

If you run into issues:
1. Check Render logs (most common issues show here)
2. Check browser console for frontend errors
3. Test backend health endpoint
4. Review this guide step-by-step

**Questions?** Contact: agon.aliu@spinp.tech
