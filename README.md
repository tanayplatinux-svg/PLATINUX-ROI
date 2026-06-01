# Platinux — Streamlit Cloud Deployment Guide

## Deploy to Streamlit Cloud (free, 5 mins)

### Step 1 — Push to GitHub

### Step 2 — Deploy App 1 (Freelancer)

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repo: `platinux-roi`
5. Branch: `main`
6. Main file path: `freelancer_roi.py`
7. App URL: set to `platinux-freelancer` (gives you platinux-freelancer.streamlit.app)
8. Click Deploy


### Step 3 — Deploy App 2 (Agency)

1. On share.streamlit.io click "New app" again
2. Same repo: `platinux-roi`
3. Branch: `main`
4. Main file path: `agency_roi.py`
5. App URL: set to `platinux-agency`
6. Click Deploy


### Step 4 — Point your domains (optional)

In your domain DNS settings add CNAME records:

  social.platinux.net   →  platinux-freelancer.streamlit.app
  agency.platinux.net   →  platinux-agency.streamlit.app

Or use nginx reverse proxy if self-hosting:

  location /social {
    proxy_pass http://localhost:8501;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
  }

  location /agency {
    proxy_pass http://localhost:8502;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
  }


## Run locally (test before deploying)

# Install deps
pip install streamlit plotly

# Run freelancer app
streamlit run freelancer_roi.py --server.port 8501

# Run agency app (separate terminal)
streamlit run agency_roi.py --server.port 8502


## Theme differences (intentional)

FREELANCER (freelancer_roi.py)
- Background: warm off-white #faf9f6
- Accent: forest green #16a34a
- Feel: personal, approachable, Notion-like
- Hero: light background (not dark)
- Best plan card: green tinted background

AGENCY (agency_roi.py)
- Background: pure white #ffffff
- Accent: indigo #4f46e5
- Feel: sharp, corporate, data-driven, McKinsey-ish
- Hero: left-aligned (not centered)
- Best plan card: dark #0f172a background

## Making changes

Edit either .py file directly — Streamlit Cloud auto-redeploys
on every git push to main. No manual redeploy needed.

Common edits:
- Prices: search for `plan_cost =` in each file
- Hero text: find `<div class="hero">`
- Add a slider: copy any st.slider() line, add to formula
- Colors: change hex values in the <style> block
