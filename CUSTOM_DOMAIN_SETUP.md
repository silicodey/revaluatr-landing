# 🌐 Custom Domain Setup Guide
## Configure revaluatr.com for GitHub Pages + Render

---

## Overview

You'll set up:
- **revaluatr.com** → GitHub Pages (frontend)
- **api.revaluatr.com** → Render (backend API)

---

## PART 1: Configure revaluatr.com for GitHub Pages

### Step 1: Add Custom Domain in GitHub

1. **Go to your GitHub repository:**
   - Visit: https://github.com/silicodey/revaluatr-landing

2. **Navigate to Settings:**
   - Click **Settings** → **Pages** (left sidebar)

3. **Add custom domain:**
   - Under "Custom domain", enter: `revaluatr.com`
   - Click **Save**
   - GitHub will check DNS configuration

4. **Enable HTTPS:**
   - Wait for DNS check to complete (may take a few minutes)
   - Check the box: **"Enforce HTTPS"**
   - Click **Save**

### Step 2: Configure DNS Records

**Where to do this:** Your domain registrar (e.g., GoDaddy, Namecheap, Google Domains, Cloudflare)

1. **Log in to your domain registrar**

2. **Find DNS settings:**
   - Look for "DNS Management", "DNS Settings", or "Nameservers"

3. **Add these DNS records:**

#### Option A: Using A Records (Recommended)
```
Type: A
Name: @
Value: 185.199.108.153
TTL: 3600

Type: A
Name: @
Value: 185.199.109.153
TTL: 3600

Type: A
Name: @
Value: 185.199.110.153
TTL: 3600

Type: A
Name: @
Value: 185.199.111.153
TTL: 3600
```

#### Add www subdomain:
```
Type: CNAME
Name: www
Value: silicodey.github.io
TTL: 3600
```

#### Option B: Using CNAME (Alternative)
If your registrar doesn't support APEX domain A records:
```
Type: CNAME
Name: @
Value: silicodey.github.io
TTL: 3600
```

### Step 3: Create CNAME File in Repository

1. **Create CNAME file:**
   ```bash
   echo "revaluatr.com" > CNAME
   ```

2. **Commit and push:**
   ```bash
   git add CNAME
   git commit -m "Add custom domain CNAME"
   git push origin main
   ```

### Step 4: Wait for DNS Propagation

- **Time required:** 5 minutes to 48 hours (usually 15-30 minutes)
- **Check status:** https://www.whatsmydns.net/#A/revaluatr.com

### Step 5: Verify Setup

1. **Visit:** http://revaluatr.com
2. **Should redirect to:** https://revaluatr.com (with HTTPS)
3. **Should show:** Your RevaluatR landing page

✅ **Frontend domain configured!**

---

## PART 2: Configure api.revaluatr.com for Render

### Step 1: Add Custom Domain in Render

1. **Go to Render Dashboard:**
   - Visit: https://dashboard.render.com

2. **Select your web service:**
   - Click on "revaluatr-landing" (or whatever you named it)

3. **Go to Settings:**
   - Click **Settings** tab
   - Scroll to **Custom Domains** section

4. **Add custom domain:**
   - Click **Add Custom Domain**
   - Enter: `api.revaluatr.com`
   - Click **Save**

5. **Copy DNS instructions:**
   - Render will show you the CNAME record to add
   - It will look like: `revaluatr-landing-xxxx.onrender.com`

### Step 2: Add DNS Record for API Subdomain

**In your domain registrar's DNS settings:**

```
Type: CNAME
Name: api
Value: revaluatr-landing-xxxx.onrender.com
TTL: 3600
```

**Important:** Replace `revaluatr-landing-xxxx.onrender.com` with the actual value Render gives you!

### Step 3: Wait for Verification

- Render will automatically verify the DNS record
- This usually takes 5-15 minutes
- You'll see a green checkmark when verified

### Step 4: Update Frontend to Use New API Domain

1. **Edit index.html and index-github.html:**
   
   Find this line (around line 361):
   ```javascript
   const API_URL = 'https://revaluatr-landing.onrender.com';
   ```

   Replace with:
   ```javascript
   const API_URL = 'https://api.revaluatr.com';
   ```

2. **Commit and push:**
   ```bash
   git add index.html index-github.html
   git commit -m "Update API URL to custom domain"
   git push origin main
   ```

### Step 5: Test API Domain

1. **Visit:** https://api.revaluatr.com/api/health
2. **Should see:**
   ```json
   {"status": "healthy", "timestamp": "..."}
   ```

✅ **Backend domain configured!**

---

## Final Architecture

```
┌─────────────────────────────────────┐
│         revaluatr.com               │
│    (GitHub Pages - Frontend)        │
│  • Landing page                     │
│  • Static HTML/CSS/JS               │
│  • Free SSL certificate             │
└──────────────┬──────────────────────┘
               │
               │ API Calls
               ▼
┌─────────────────────────────────────┐
│      api.revaluatr.com              │
│      (Render - Backend)             │
│  • Flask API                        │
│  • Handles form submissions         │
│  • Stores waitlist data             │
└─────────────────────────────────────┘
```

---

## Troubleshooting

### "DNS check failed" in GitHub
- **Wait longer:** DNS can take up to 48 hours
- **Check records:** Use https://www.whatsmydns.net
- **Clear cache:** Try incognito mode

### "Not Secure" warning
- **Wait for HTTPS:** Can take 24 hours after DNS propagation
- **Force HTTPS:** Make sure "Enforce HTTPS" is checked in GitHub

### API domain not working
- **Check CNAME:** Make sure you copied the exact value from Render
- **Wait for verification:** Can take 15-30 minutes
- **Check Render logs:** Look for SSL certificate errors

### www not working
- **Add CNAME:** Make sure you added the www CNAME record
- **Wait:** DNS propagation takes time

---

## DNS Record Summary

**At your domain registrar, you should have:**

| Type | Name | Value | Purpose |
|------|------|-------|---------|
| A | @ | 185.199.108.153 | GitHub Pages (1/4) |
| A | @ | 185.199.109.153 | GitHub Pages (2/4) |
| A | @ | 185.199.110.153 | GitHub Pages (3/4) |
| A | @ | 185.199.111.153 | GitHub Pages (4/4) |
| CNAME | www | silicodey.github.io | www subdomain |
| CNAME | api | [your-render-url].onrender.com | Backend API |

---

## Email Configuration (Optional)

If you want to use email@revaluatr.com, you'll need to add MX records from your email provider (Google Workspace, Microsoft 365, etc.)

**Example for Google Workspace:**
```
Type: MX
Name: @
Value: ASPMX.L.GOOGLE.COM
Priority: 1
```

---

## Testing Checklist

- [ ] http://revaluatr.com redirects to https://revaluatr.com
- [ ] https://revaluatr.com shows landing page
- [ ] https://www.revaluatr.com works
- [ ] https://api.revaluatr.com/api/health returns JSON
- [ ] Form submission works with new API domain
- [ ] SSL certificate is valid (green padlock)

---

## 🎉 Done!

Your professional setup:
- **Landing Page:** https://revaluatr.com
- **API:** https://api.revaluatr.com
- **Both with SSL certificates**
- **Professional, branded URLs**

Perfect for sharing with Deutsche Bank and investors! 🚀
