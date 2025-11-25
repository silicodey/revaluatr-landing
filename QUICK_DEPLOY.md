# 🚀 Quick Deployment Steps

## BACKEND (Render) - Do This First!

1. **Go to**: https://render.com
2. **Sign up** with GitHub
3. **New Web Service** → Connect your repo
4. **Configure**:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn --bind 0.0.0.0:$PORT server:app`
   - Instance: Free
5. **Deploy** → Copy your URL (e.g., `https://revaluatr-backend.onrender.com`)

---

## FRONTEND (GitHub Pages) - Do This Second!

1. **Update API URL** in `index-github.html` line 382:
   ```javascript
   const API_URL = 'https://YOUR-RENDER-URL.onrender.com';
   ```

2. **Replace index.html**:
   ```bash
   mv index-github.html index.html
   ```

3. **Push to GitHub**:
   ```bash
   git add index.html
   git commit -m "Deploy to GitHub Pages"
   git push origin main
   ```

4. **Enable GitHub Pages**:
   - GitHub repo → Settings → Pages
   - Source: main branch, / (root)
   - Save

5. **Done!** Your site will be at:
   `https://[username].github.io/[repo-name]/`

---

## Test It!

✅ Visit your GitHub Pages URL
✅ Submit the form
✅ Check Render logs for confirmation

---

**Full guide**: See DEPLOYMENT_GUIDE.md
