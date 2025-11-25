# 📊 Deployment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         USERS                                │
│                  (Visit your website)                        │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │      GITHUB PAGES (Frontend)       │
        │  https://silicodey.github.io/      │
        │      revaluatr-landing/            │
        │                                    │
        │  • Serves index.html               │
        │  • Static HTML/CSS/JS              │
        │  • Free, fast CDN                  │
        │  • Always online                   │
        └────────────────┬───────────────────┘
                         │
                         │ API Calls
                         │ (Form Submission)
                         ▼
        ┌────────────────────────────────────┐
        │      RENDER (Backend API)          │
        │  https://revaluatr-backend         │
        │         .onrender.com              │
        │                                    │
        │  • Flask Python server             │
        │  • Handles /api/waitlist           │
        │  • Stores data in waitlist.csv     │
        │  • Free tier (spins down)          │
        └────────────────┬───────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │       DATA STORAGE                 │
        │                                    │
        │  • waitlist.csv (on Render)        │
        │  • Optional: Google Sheets         │
        │  • Optional: Email notifications   │
        └────────────────────────────────────┘
```

---

## 🔄 How It Works

1. **User visits** `https://silicodey.github.io/revaluatr-landing/`
2. **GitHub Pages** serves the static HTML page (fast!)
3. **User fills form** and clicks "Join Waitlist"
4. **JavaScript sends** POST request to Render backend
5. **Render backend** validates and saves to `waitlist.csv`
6. **Success message** shows on frontend
7. **You can access** waitlist data via Render dashboard

---

## 💰 Costs

| Service | Cost | Limits |
|---------|------|--------|
| **GitHub Pages** | FREE | Unlimited |
| **Render (Free Tier)** | FREE | 750 hrs/month, spins down after 15min |
| **Total** | **$0/month** | Perfect for landing page! |

---

## 🎯 Your URLs

After deployment:

**Public Landing Page:**
```
https://silicodey.github.io/revaluatr-landing/
```

**Backend API:**
```
https://revaluatr-backend.onrender.com
```

**API Endpoints:**
- Health: `/api/health`
- Submit: `/api/waitlist` (POST)
- Count: `/api/waitlist/count` (GET)

---

## 📁 Files You Need

### For GitHub Pages:
- ✅ `index.html` (updated with Render URL)

### For Render:
- ✅ `server.py` (Flask backend)
- ✅ `requirements.txt` (Python dependencies)
- ✅ `Procfile` (already exists)
- ✅ `runtime.txt` (already exists)

---

## 🚀 Deployment Order

**IMPORTANT: Deploy in this order!**

1. **First**: Deploy backend to Render → Get URL
2. **Second**: Update frontend with backend URL
3. **Third**: Deploy frontend to GitHub Pages

Why? Because frontend needs to know backend URL!

---

## 🔐 Security Notes

✅ **What's secure:**
- HTTPS on both frontend and backend
- CORS properly configured
- Email validation
- No sensitive data exposed

⚠️ **Production improvements:**
- Add rate limiting (prevent spam)
- Add reCAPTCHA (prevent bots)
- Use PostgreSQL instead of CSV
- Set up automated backups

---

## 📈 Monitoring

**Check backend health:**
```
https://revaluatr-backend.onrender.com/api/health
```

**Check signup count:**
```
https://revaluatr-backend.onrender.com/api/waitlist/count
```

**View logs:**
- Render Dashboard → Your Service → Logs

**Download data:**
- Render Dashboard → Your Service → Shell → `cat waitlist.csv`

---

## 🎉 Next Steps After Deployment

1. ✅ Test form submission
2. ✅ Share URL with Deutsche Bank
3. ✅ Set up UptimeRobot to keep backend warm
4. ✅ Add Google Analytics (optional)
5. ✅ Configure custom domain (optional)
6. ✅ Set up email notifications (optional)

---

**Ready to deploy? Follow QUICK_DEPLOY.md!**
