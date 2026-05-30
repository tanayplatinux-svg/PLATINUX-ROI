# Platinux ROI Calculator — Streamlit App

## Setup

1. Make sure Python 3.9+ is installed.

2. Create a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   streamlit run app.py

5. Open http://localhost:8501 in your browser.

## File structure

platinux_roi/
├── app.py            ← main app — edit this for all changes
└── requirements.txt  ← dependencies

## Making changes

All sections are clearly commented in app.py:

- HERO          → edit the headline, subtext, badge text
- ROI CALCULATOR → add/remove sliders, change formulas
- CHART SECTION  → tweak chart styles, add more series
- COMPARISON TABLE → edit rows, add columns
- PRICING SECTION  → update prices, features
- CTA SECTION    → edit the closing call to action

Every time you save app.py, Streamlit hot-reloads the page automatically.
No restart needed.

## Deploy to Streamlit Cloud (free)

1. Push this folder to a GitHub repo.
2. Go to share.streamlit.io
3. Connect your repo, set app.py as the entrypoint.
4. Deploy — you get a public URL like platinux-roi.streamlit.app

## Deploy to your own domain (e.g. platinux.net/social)

Use a reverse proxy (nginx) to serve the Streamlit app:

server {
    location /social {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

Run on server: streamlit run app.py --server.port 8501 --server.address 0.0.0.0
