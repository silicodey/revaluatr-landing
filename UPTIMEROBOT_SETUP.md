# ⏰ UptimeRobot Setup Guide
## Keep Your Backend Warm (Always Fast)

---

## Overview

**The Problem:**
Render's free tier "spins down" your backend after 15 minutes of inactivity. The first request after spin-down takes ~30 seconds to wake up.

**The Solution:**
UptimeRobot pings your backend every 5 minutes, keeping it awake 24/7.

**Benefits:**
- ✅ Instant form submissions (no 30-second wait)
- ✅ Better user experience
- ✅ Professional appearance
- ✅ 100% free
- ✅ Bonus: Uptime monitoring + alerts

---

## PART 1: Create UptimeRobot Account

### Step 1: Sign Up

1. **Go to:** https://uptimerobot.com
2. **Click:** "Free Sign Up"
3. **Enter:**
   - Email address
   - Password
4. **Click:** "Sign up for free"
5. **Verify your email** (check inbox)

### Step 2: Confirm Email

1. **Check your email** for verification link
2. **Click the link** to activate account
3. **Log in** to UptimeRobot dashboard

---

## PART 2: Add Your Backend Monitor

### Step 1: Create New Monitor

1. **In dashboard, click:** "+ Add New Monitor"

2. **Configure monitor:**

   **Monitor Type:** `HTTP(s)`
   
   **Friendly Name:** `RevaluatR Backend`
   
   **URL (or IP):** `https://revaluatr-landing.onrender.com/api/health`
   
   (Or use `https://api.revaluatr.com/api/health` if you set up custom domain)
   
   **Monitoring Interval:** `5 minutes`
   
   **Monitor Timeout:** `30 seconds`
   
   **HTTP Method:** `GET`

3. **Click:** "Create Monitor"

### Step 2: Verify Monitor is Working

1. **Wait 1-2 minutes** for first check
2. **You should see:**
   - Status: **Up** (green checkmark)
   - Response time: ~200-500ms
   - Uptime: 100%

✅ **Your backend will now stay warm!**

---

## PART 3: Set Up Alerts (Optional but Recommended)

### Why Set Up Alerts?

Get notified if your backend goes down (e.g., Render issues, deployment problems).

### Step 1: Add Alert Contact

1. **Click:** "My Settings" (top right)
2. **Go to:** "Alert Contacts" tab
3. **Click:** "Add Alert Contact"

### Step 2: Configure Email Alerts

**Type:** `E-mail`

**Friendly Name:** `My Email`

**Email to Alert:** Your email address

**Click:** "Create Alert Contact"

**Check your email** and verify the alert contact

### Step 3: Assign Alert to Monitor

1. **Go back to:** "Dashboard"
2. **Click on your monitor:** "RevaluatR Backend"
3. **Click:** "Edit"
4. **Scroll to:** "Alert Contacts to Notify"
5. **Select:** Your email
6. **Click:** "Save Changes"

### What You'll Get Alerted About:

- ✅ **Down:** Backend is unreachable
- ✅ **Up:** Backend is back online
- ✅ **Response time:** If it's unusually slow

---

## PART 4: Advanced Configuration (Optional)

### Add Multiple Endpoints

Monitor multiple parts of your backend:

**Monitor 1: Health Check**
- URL: `https://api.revaluatr.com/api/health`
- Purpose: Check if backend is alive

**Monitor 2: Waitlist Count**
- URL: `https://api.revaluatr.com/api/waitlist/count`
- Purpose: Check if database is working

**Monitor 3: Frontend**
- URL: `https://revaluatr.com`
- Purpose: Check if GitHub Pages is up

### Keyword Monitoring

Make sure the response contains expected content:

1. **Edit monitor**
2. **Scroll to:** "Advanced Settings"
3. **Keyword Type:** `Keyword exists`
4. **Keyword Value:** `healthy`
5. **Save**

Now it checks that `/api/health` returns `{"status": "healthy", ...}`

### Custom HTTP Headers

If you add authentication later:

1. **Edit monitor**
2. **Custom HTTP Headers:**
   ```
   Authorization: Bearer your-token
   ```

---

## What UptimeRobot Does

### Every 5 Minutes:

1. **Sends GET request** to your backend
2. **Checks response:**
   - Status code (should be 200)
   - Response time
   - Optional: Keyword check
3. **Keeps backend awake** (prevents spin-down)
4. **Records uptime statistics**

### If Backend is Down:

1. **Tries again** immediately
2. **If still down:** Sends you an alert
3. **Keeps trying** every 5 minutes
4. **Sends "back up" alert** when recovered

---

## Dashboard Overview

### Key Metrics You'll See:

**Uptime Percentage:**
- 100% = Perfect (goal!)
- 99.9% = Very good
- < 99% = Investigate issues

**Response Time:**
- < 500ms = Excellent
- 500ms - 1s = Good
- > 1s = Slow (investigate)

**Down Events:**
- Shows when backend was unreachable
- Click for details (duration, reason)

**Logs:**
- Complete history of all checks
- Response codes, times, etc.

---

## Free Tier Limits

### What You Get for Free:

✅ **50 monitors** (you only need 1-3)
✅ **5-minute intervals** (perfect for keeping warm)
✅ **2-month log retention**
✅ **Email alerts** (unlimited)
✅ **SMS alerts** (10/month)
✅ **Public status pages**

### Paid Tier ($7/month):

- 1-minute intervals
- More monitors
- Longer log retention
- More alert options

**For your use case, free tier is perfect!**

---

## Alternative: Cron-job.org

If you prefer an alternative to UptimeRobot:

### Cron-job.org Setup

1. **Go to:** https://cron-job.org
2. **Sign up** for free
3. **Create cronjob:**
   - Title: `RevaluatR Backend`
   - URL: `https://api.revaluatr.com/api/health`
   - Schedule: Every 5 minutes
   - Enabled: Yes
4. **Save**

**Pros:**
- Simple interface
- Reliable
- Free

**Cons:**
- No uptime monitoring
- No alerts
- Just keeps backend warm

---

## Monitoring Best Practices

### 1. Monitor the Right Endpoint

✅ **Good:** `/api/health` (lightweight, fast)
❌ **Bad:** `/` (loads entire HTML page)

### 2. Don't Ping Too Often

✅ **5 minutes:** Perfect balance
❌ **1 minute:** Wastes resources
❌ **15 minutes:** Backend might spin down

### 3. Set Up Alerts

- Know when things break
- Fix issues before users notice
- Track uptime trends

### 4. Check Dashboard Weekly

- Review uptime percentage
- Look for patterns (slow times, outages)
- Optimize if needed

---

## Troubleshooting

### Monitor Shows "Down"

**Check:**
1. **Visit URL manually** in browser
2. **Check Render dashboard** - is service running?
3. **Check Render logs** - any errors?
4. **Verify URL** - typo in UptimeRobot?

**Common causes:**
- Render deployment in progress
- Render service crashed
- Network issues (rare)
- Wrong URL in UptimeRobot

### High Response Time

**Normal:**
- First request after spin-down: 20-30 seconds
- Subsequent requests: 200-500ms

**If consistently slow:**
- Check Render logs for errors
- Optimize backend code
- Consider upgrading Render plan

### Too Many Alerts

**Adjust alert settings:**
1. Edit monitor
2. Change "Alert When Down For:" to `5 minutes`
3. Prevents alerts for brief hiccups

---

## Testing Your Setup

### Step 1: Verify Monitor is Active

1. **Go to UptimeRobot dashboard**
2. **Check status:** Should be "Up" (green)
3. **Check last check:** Should be < 5 minutes ago

### Step 2: Test Spin-Down Prevention

1. **Don't visit your site** for 20 minutes
2. **Then visit:** https://revaluatr.com
3. **Submit form**
4. **Should be instant** (not 30-second wait)

### Step 3: Test Alerts (Optional)

1. **Temporarily stop Render service:**
   - Render Dashboard → Your Service → Manual Deploy → Suspend
2. **Wait 5-10 minutes**
3. **Check email** - should receive "Down" alert
4. **Resume service**
5. **Check email** - should receive "Up" alert

---

## Status Page (Bonus Feature)

### Create Public Status Page

Show your uptime to users/investors:

1. **UptimeRobot Dashboard**
2. **Click:** "Public Status Pages"
3. **Click:** "Add New Status Page"
4. **Configure:**
   - Name: `RevaluatR Status`
   - Monitors: Select your backend
   - Custom domain: `status.revaluatr.com` (optional)
5. **Save**

**You get a URL like:**
`https://stats.uptimerobot.com/your-page`

**Shows:**
- Current status (Up/Down)
- Uptime percentage (30/60/90 days)
- Response time graph
- Incident history

**Use cases:**
- Share with investors
- Include in pitch deck
- Link from footer of website

---

## Integration with Slack (Advanced)

### Get Alerts in Slack

1. **Create Slack webhook:**
   - Slack → Apps → Incoming Webhooks
   - Add to channel
   - Copy webhook URL

2. **Add to UptimeRobot:**
   - My Settings → Alert Contacts
   - Type: Web-Hook
   - URL: Your Slack webhook
   - POST Value:
   ```json
   {
     "text": "*monitorFriendlyName* is *alertTypeFriendlyName*"
   }
   ```

3. **Assign to monitor**

Now you get Slack notifications when backend goes down!

---

## 🎉 You're All Set!

After setup, your backend will:
- ✅ **Stay awake 24/7** (no spin-down delays)
- ✅ **Respond instantly** to form submissions
- ✅ **Alert you** if something breaks
- ✅ **Track uptime** automatically

**Benefits:**
- Better user experience
- Professional reliability
- Peace of mind
- Free monitoring

---

## Quick Reference

### UptimeRobot Settings

```
Monitor Type: HTTP(s)
Friendly Name: RevaluatR Backend
URL: https://api.revaluatr.com/api/health
Interval: 5 minutes
Timeout: 30 seconds
Method: GET
```

### Expected Results

```
Status: Up ✓
Response Time: 200-500ms
Uptime: 99.9%+
```

### Alert Settings

```
Alert When: Down
Alert After: 5 minutes
Notify: Your email
```

---

## Next Steps

1. ✅ **Sign up** for UptimeRobot
2. ✅ **Add monitor** for your backend
3. ✅ **Set up alerts** (optional)
4. ✅ **Test** by submitting form
5. ✅ **Check dashboard** weekly

**That's it! Your backend will now stay warm and fast.** 🚀
