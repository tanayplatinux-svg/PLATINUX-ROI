import streamlit as st
import math

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Platinux | Agency Infrastructure",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. STATIC CSS DESIGN SYSTEM
# Wrapped in a raw string to prevent any f-string {} brace parsing errors
STATIC_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Default Elements for Landing Page look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding-top: 2rem; max-width: 1200px; }

    /* Custom Streamlit Slider Colors */
    .stSlider > div > div > div > div { background-color: #10b981 !important; }

    /* Hero Section */
    .plx-hero {
        background-color: #020617;
        color: white;
        padding: 6rem 2rem;
        text-align: center;
        border-radius: 1.5rem;
        position: relative;
        overflow: hidden;
        margin-bottom: 4rem;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    }
    .plx-hero-glow {
        position: absolute;
        top: -50%; left: 50%;
        transform: translateX(-50%);
        width: 800px; height: 400px;
        background: rgba(16, 185, 129, 0.15);
        filter: blur(80px);
        border-radius: 50%;
        pointer-events: none;
    }
    .plx-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1.25rem;
        border-radius: 9999px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        color: #34d399;
        font-size: 0.875rem;
        font-weight: 500;
        margin-bottom: 2rem;
        position: relative;
        z-index: 10;
    }
    .plx-title {
        font-size: 3.5rem;
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 10;
    }
    .plx-gradient-text {
        background: linear-gradient(to right, #34d399, #22d3ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .plx-subtitle {
        color: #94a3b8;
        font-size: 1.25rem;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.6;
        position: relative;
        z-index: 10;
    }

    /* Section Titles */
    .section-head { text-align: center; margin-bottom: 4rem; margin-top: 2rem; }
    .section-head h2 { color: #059669; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; margin-bottom: 0.5rem; }
    .section-head h3 { font-size: 2.5rem; font-weight: 700; color: #0f172a; margin-bottom: 1rem; }
    .section-head p { color: #64748b; font-size: 1.125rem; max-width: 650px; margin: 0 auto; }

    /* Timeline Workflow */
    .workflow-wrap { position: relative; max-width: 1000px; margin: 0 auto 5rem auto; }
    .timeline-line { position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; background: #e2e8f0; transform: translateX(-50%); z-index: 0; }
    .step-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem; position: relative; z-index: 10; }
    .step-number {
        position: absolute; left: 50%; transform: translateX(-50%);
        width: 3rem; height: 3rem; background: white; border: 4px solid #e2e8f0;
        border-radius: 50%; display: flex; align-items: center; justify-content: center;
        font-weight: 700; font-size: 1.25rem;
    }
    .step-content { width: 45%; }
    .step-row:nth-child(odd) .step-content { text-align: right; }
    .step-row:nth-child(even) .step-content { margin-left: auto; text-align: left; }
    
    .step-tag { display: inline-block; padding: 0.25rem 0.75rem; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; border-radius: 9999px; margin-bottom: 1rem; }
    .tag-blue { background: #eff6ff; color: #1d4ed8; }
    .tag-amber { background: #fffbeb; color: #b45309; }
    .tag-indigo { background: #eef2ff; color: #4338ca; }
    .tag-emerald { background: rgba(16,185,129,0.2); color: #34d399; border: 1px solid rgba(16,185,129,0.3); }

    .step-content h4 { font-size: 1.5rem; font-weight: 700; color: #0f172a; margin-bottom: 0.75rem; }
    .step-content p { color: #475569; line-height: 1.6; }

    .step-vip { background: #0f172a; border: 2px solid #10b981; padding: 2rem; border-radius: 1rem; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); text-align: left !important; }
    .step-vip h4 { color: white; }
    .step-vip p { color: #94a3b8; margin-bottom: 1.5rem; }

    /* Info Box */
    .info-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 1rem; text-align: left; display: inline-block; }
    .info-box span { font-weight: 600; color: #0f172a; font-size: 0.875rem; display: block; margin-bottom: 0.25rem; }
    .info-box p { color: #64748b !important; font-size: 0.875rem; margin: 0 !important; }

    /* Audits Section */
    .audits-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; background: #f8fafc; padding: 4rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 5rem; }
    .audit-feat { display: flex; gap: 1rem; margin-bottom: 2rem; }
    .audit-icon { width: 3rem; height: 3rem; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.25rem; flex-shrink: 0; }
    .icon-green { background: #d1fae5; color: #059669; }
    .icon-blue { background: #dbeafe; color: #2563eb; }
    .icon-purple { background: #f3e8ff; color: #9333ea; }
    .audit-feat h4 { font-size: 1.25rem; font-weight: 700; color: #0f172a; margin: 0 0 0.25rem 0;}
    .audit-feat p { color: #475569; margin: 0; line-height: 1.5;}

    .mock-card { background: white; padding: 2rem; border-radius: 1rem; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); border: 1px solid #f1f5f9; }
    .mock-header { background: #0f172a; margin: -2rem -2rem 2rem -2rem; padding: 1rem 1.5rem; display: flex; gap: 0.5rem; align-items: center; border-radius: 1rem 1rem 0 0;}
    .mock-dot { width: 12px; height: 12px; border-radius: 50%; }
    .mock-title { font-family: monospace; color: #94a3b8; font-size: 0.75rem; margin-left: 1rem; }
    .mock-metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem; }
    .mock-metric { border: 1px solid #f1f5f9; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid #ef4444; }
    .mock-metric:nth-child(2) { border-left-color: #f59e0b; }
    .mock-label { font-size: 0.75rem; font-weight: 700; color: #64748b; text-transform: uppercase; margin-bottom: 0.25rem; }
    .mock-val { font-size: 1.5rem; font-weight: 700; color: #0f172a; }

    /* Calculator Cards */
    .lead-box { background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 1rem; padding: 1rem 1.5rem; display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; }
    .lead-num { background: #10b981; color: white; width: 3rem; height: 3rem; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.25rem; }
    
    .calc-out-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem; }
    .out-card { background: white; padding: 1.5rem; border-radius: 1rem; border: 1px solid #e2e8f0; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .out-label { font-size: 0.75rem; text-transform: uppercase; font-weight: 600; color: #64748b; letter-spacing: 0.05em; margin-bottom: 0.5rem; }
    .out-val { font-size: 2.25rem; font-weight: 700; color: #0f172a; margin-bottom: 0.25rem; }
    .out-sub { font-size: 0.875rem; color: #64748b; }
    
    .out-card-vip { background: #020617; border: 2px solid #10b981; box-shadow: 0 10px 30px rgba(16,185,129,0.2); }
    .out-card-vip .out-label { color: #94a3b8; }
    .out-card-vip .out-val { color: #34d399; }
    .out-card-vip .out-sub { color: #64748b; }
    
    .out-card-annual { background: #f0fdf4; border-color: #bbf7d0; }
    .out-card-annual .out-label { color: #15803d; }
    .out-card-annual .out-val { color: #16a34a; }

    /* Comparison Table */
    .compare-wrap { max-width: 900px; margin: 5rem auto; background: white; border-radius: 1rem; overflow: hidden; border: 1px solid #e2e8f0; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
    .compare-row { display: grid; grid-template-columns: 1.2fr 1fr 1fr; padding: 1.5rem; border-bottom: 1px solid #f1f5f9; align-items: center;}
    .compare-header { background: #0f172a; color: white; font-weight: 600; text-transform: uppercase; font-size: 0.875rem; letter-spacing: 0.05em; }
    .comp-label { font-weight: 500; color: #334155; }
    .comp-bad { color: #ef4444; font-weight: 600; }
    .comp-good { color: #059669; font-weight: 600; }
    
    /* Pricing */
    .pricing-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; max-width: 1100px; margin: 0 auto; padding-bottom: 4rem; }
    .price-card { background: white; padding: 2.5rem 2rem; border-radius: 1.5rem; border: 1px solid #e2e8f0; display: flex; flex-direction: column; }
    .price-name { font-size: 0.875rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem; }
    .price-val { font-size: 3.5rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; }
    .price-sub { color: #64748b; margin-bottom: 2rem; }
    .price-features { list-style: none; padding: 0; margin: 0 0 2rem 0; flex-grow: 1; }
    .price-features li { margin-bottom: 1rem; color: #475569; font-size: 0.95rem; }
    
    .price-card-vip { background: #0f172a; border: 2px solid #10b981; box-shadow: 0 20px 40px -10px rgba(16,185,129,0.3); transform: translateY(-1rem); position: relative; }
    .price-card-vip .price-name { color: #34d399; }
    .price-card-vip .price-val { color: white; }
    .price-card-vip .price-sub { color: #94a3b8; }
    .price-card-vip .price-features li { color: #cbd5e1; }
    
    .popular-tag { position: absolute; top: 0; right: 0; background: #10b981; color: #0f172a; font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.75rem; border-radius: 0 1rem 0 1rem; text-transform: uppercase; }
</style>
"""

# Inject CSS
st.markdown(STATIC_CSS, unsafe_allow_html=True)

# 3. HTML LAYOUT SECTIONS
st.markdown("""
<div class="plx-hero">
    <div class="plx-hero-glow"></div>
    <div class="plx-badge">
        <span style="display:inline-block; width:8px; height:8px; background:#10b981; border-radius:50%; margin-right:4px;"></span>
        Platinux Agency Infrastructure Live
    </div>
    <h1 class="plx-title">Stop scaling your sales team.<br><span class="plx-gradient-text">Scale your lead flow.</span></h1>
    <p class="plx-subtitle">Platinux tracks founders and enterprises actively requesting custom development, SaaS builds, and design overhauls. Reach high-ticket clients before they ever post on Upwork.</p>
</div>

<div class="section-head">
    <h2>Your Path to Clients</h2>
    <h3>From zero to paid. In 4 steps.</h3>
    <p>Here is exactly how Platinux turns a business owner's technical debt into money in your agency's account.</p>
</div>

<div class="workflow-wrap">
    <div class="timeline-line"></div>
    
    <div class="step-row">
        <div class="step-content">
            <span class="step-tag tag-blue">🔍 Scanning</span>
            <h4>Deep Web Intent Scanning</h4>
            <p>Platinux automatically scans millions of live websites 24/7, flagging broken designs, mobile layout issues, and outdated landing pages that desperately need an agency's touch.</p>
            <div class="info-box mt-4">
                <span>System Scan Fact:</span>
                <p>12,450 local B2B sites audited resulted in 1,000 flagged with high technical debt.</p>
            </div>
        </div>
        <div class="step-number" style="border-color: #dbeafe; color: #2563eb;">1</div>
        <div class="step-content"></div>
    </div>

    <div class="step-row">
        <div class="step-content"></div>
        <div class="step-number" style="border-color: #fef3c7; color: #d97706;">2</div>
        <div class="step-content">
            <span class="step-tag tag-amber">🎯 Filtering</span>
            <h4>Sifting 1,000 to 100 Hot Leads</h4>
            <p>Instead of wasting team hours cold-outreaching blindly to 10,000 sites, Platinux's machine learning filters the technical flags down to the <strong>100 high-potential leads</strong> with the highest conversion probability and budget signals.</p>
        </div>
    </div>

    <div class="step-row">
        <div class="step-content">
            <span class="step-tag tag-indigo">📄 Auditing</span>
            <h4>Automated Audit Reports</h4>
            <p>For each of the 100 narrowed leads, Platinux instantly generates a bespoke, stunning Website Audit Report highlighting real conversion friction. This goes direct to your SDR's outreach workflow.</p>
        </div>
        <div class="step-number" style="border-color: #e0e7ff; color: #4f46e5;">3</div>
        <div class="step-content"></div>
    </div>

    <div class="step-row">
        <div class="step-content"></div>
        <div class="step-number" style="border-color: #10b981; color: #10b981; background: #020617;">4</div>
        <div class="step-content step-vip">
            <span class="step-tag tag-emerald">💰 Acquisition</span>
            <h4>Outreach & Close.</h4>
            <p>Your team sends value-first messages with the audit attached. Prospects see exactly what is broken, bypassing gatekeepers and filling your agency calendar.</p>
            <div style="border-top: 1px solid #1e293b; padding-top: 1rem; margin-top: 1rem;">
                <span style="display:block; color:#64748b; font-size:0.875rem; margin-bottom:0.25rem;">Average Deal Value Created:</span>
                <strong style="font-size:2rem; color:#34d399;">+$8,000</strong><span style="color:#64748b; font-size:1rem;">/client</span>
            </div>
        </div>
    </div>
</div>

<div class="audits-grid">
    <div>
        <h2 style="font-size: 2.25rem; font-weight: 700; color: #0f172a; margin-bottom: 1.5rem; line-height: 1.2;">Why the "Audit First" approach guarantees responses.</h2>
        <p style="color: #475569; font-size: 1.125rem; margin-bottom: 2.5rem; line-height: 1.6;">Cold pitching "web design services" to a CEO yields a sub-1% response rate. Showing a CEO exactly how their current site is bleeding revenue yields a totally different result.</p>
        
        <div class="audit-feat">
            <div class="audit-icon icon-green">3x</div>
            <div>
                <h4>Triple your response rate</h4>
                <p>Agencies using our custom PDF audits in their outreach experience a documented 300% increase in positive reply rates.</p>
            </div>
        </div>
        <div class="audit-feat">
            <div class="audit-icon icon-blue">📈</div>
            <div>
                <h4>Revenue-focused framing</h4>
                <p>We don't just flag "bad code." The audits translate Core Web Vitals failures into projected lost traffic and lost revenue.</p>
            </div>
        </div>
        <div class="audit-feat">
            <div class="audit-icon icon-purple">🔑</div>
            <div>
                <h4>Bypass Gatekeepers</h4>
                <p>A generic email goes to the trash. An attached report titled "Performance Vulnerabilities" gets forwarded directly to leadership.</p>
            </div>
        </div>
    </div>
    
    <div>
        <div class="mock-card">
            <div class="mock-header">
                <div class="mock-dot dot-r"></div>
                <div class="mock-dot dot-y"></div>
                <div class="mock-dot dot-g"></div>
                <div class="mock-title">audit_report_target_client.pdf</div>
            </div>
            <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 1.5rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; display: inline-block;">Technical Audit Overview</h3>
            <div class="mock-metrics">
                <div class="mock-metric">
                    <div class="mock-label">LCP Time</div>
                    <div class="mock-val" style="color: #ef4444;">4.2s <span style="font-size: 0.875rem; color: #94a3b8; font-weight: 400;">(Poor)</span></div>
                </div>
                <div class="mock-metric">
                    <div class="mock-label">Mobile UX</div>
                    <div class="mock-val" style="color: #f59e0b;">Flagged</div>
                </div>
            </div>
            <div style="background: #f8fafc; padding: 1.5rem; border-radius: 0.5rem; border: 1px solid #e2e8f0;">
                <div style="font-weight: 700; margin-bottom: 0.75rem;">Executive Summary</div>
                <div style="height: 10px; background: #e2e8f0; border-radius: 4px; margin-bottom: 8px;"></div>
                <div style="height: 10px; background: #e2e8f0; border-radius: 4px; margin-bottom: 8px;"></div>
                <div style="height: 10px; background: #e2e8f0; border-radius: 4px; width: 80%; margin-bottom: 16px;"></div>
                <div style="font-weight: 700; color: #059669; border-top: 1px solid #e2e8f0; padding-top: 1rem;">Estimated Revenue Leak: $12,500/mo</div>
            </div>
        </div>
    </div>
</div>

<div class="section-head">
    <h2>Agency Economics</h2>
    <h3>Calculate your true net profit.</h3>
    <p>Model your agency overhead based on a steady stream of <strong>100 verified hot leads</strong> delivered by Platinux per month.</p>
</div>
""", unsafe_allow_html=True)

# 4. INTERACTIVE CALCULATOR (Streamlit Native Columns)
col1, col2 = st.columns([5, 7], gap="large")

with col1:
    st.markdown("""
    <div class="lead-box">
        <div class="lead-num">100</div>
        <div>
            <strong style="display:block; color:#0f172a;">Hot Leads per Month</strong>
            <span style="color:#64748b; font-size:0.875rem;">Conservative model based on standard monthly delivery.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    deal_size = st.slider("Average Deal Size ($)", 2000, 50000, 8000, step=1000)
    close_rate = st.slider("Lead Close Rate (%)", 1, 20, 3, step=1)
    margin = st.slider("Net Profit Margin (%)", 10, 80, 40, step=5)

# Python Financial Logic
leads_per_month = 100
sub_cost = 199

clients_per_month = leads_per_month * (close_rate / 100.0)
monthly_revenue = clients_per_month * deal_size
monthly_profit = monthly_revenue * (margin / 100.0)

net_gain_monthly = monthly_profit - sub_cost
annual_profit = max(0, net_gain_monthly * 12)

roi = math.floor((monthly_profit / sub_cost) * 100) if sub_cost > 0 else 0
profit_per_client = deal_size * (margin / 100.0)
payback_clients = (sub_cost / profit_per_client) if profit_per_client > 0 else 0

if payback_clients < 1:
    payback_str = "&lt; 1 deal"
else:
    payback_str = f"{payback_clients:.2f} deals"

with col2:
    # Inject dynamically calculated data into the styled HTML container
    output_html = f"""
    <div class="calc-out-grid">
        <div class="out-card out-card-vip">
            <div class="out-label">Monthly Agency ROI</div>
            <div class="out-val">{roi:,}%</div>
            <div class="out-sub">Return on $199/mo subscription</div>
        </div>
        <div class="out-card">
            <div class="out-label">Gross Revenue / Mo</div>
            <div class="out-val">${monthly_revenue:,.0f}</div>
            <div class="out-sub">Based on {clients_per_month:g} deals closed</div>
        </div>
        <div class="out-card">
            <div class="out-label">Net Profit / Mo</div>
            <div class="out-val">${monthly_profit:,.0f}</div>
            <div class="out-sub">After {100 - margin}% dev/team overhead</div>
        </div>
        <div class="out-card out-card-annual">
            <div class="out-label">Annual Net Profit</div>
            <div class="out-val">${annual_profit:,.0f}</div>
            <div class="out-sub">Minus Platinux platform fees</div>
        </div>
    </div>
    
    <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 1.25rem; border-radius: 0 0.5rem 0.5rem 0; margin-top: 1.5rem;">
        <p style="color: #1e40af; margin: 0; font-size: 0.95rem; line-height: 1.5;">
            <strong>Minimal Risk:</strong> You only need to close <strong style="text-decoration:underline;">{payback_str}</strong> to completely cover your yearly Platinux subscription from your <em>net profit margin</em> alone.
        </p>
    </div>
    """
    st.markdown(output_html, unsafe_allow_html=True)


# 5. BOTTOM SECTIONS (Comparison & Pricing)
st.markdown("""
<div class="compare-wrap">
    <div class="compare-row compare-header">
        <div>Feature</div>
        <div>B2B Ads / SDR Team</div>
        <div class="comp-header-good">Platinux Agency</div>
    </div>
    <div class="compare-row">
        <div class="comp-label">Lead Intent</div>
        <div class="comp-bad">Cold (Interruptive)</div>
        <div class="comp-good">✓ Hot (Actively Needs Fix)</div>
    </div>
    <div class="compare-row">
        <div class="comp-label">Cost to Scale</div>
        <div class="comp-bad">Higher spend = more leads</div>
        <div class="comp-good">✓ Flat Rate</div>
    </div>
    <div class="compare-row" style="background: #f8fafc;">
        <div class="comp-label">Annual Acquisition Cost</div>
        <div class="comp-bad">~$60,000+ (Ad Spend/Salary)</div>
        <div class="comp-good" style="font-size: 1.25rem;">✓ $2,388/yr</div>
    </div>
</div>

<div class="section-head">
    <h3 style="font-size: 2.5rem; margin-bottom:0.5rem;">One deal covers the year.</h3>
    <p>Transparent pricing. Cancel anytime.</p>
</div>

<div class="pricing-grid">
    <div class="price-card">
        <div class="price-name">Pro (Solo Devs)</div>
        <div class="price-val">$79</div>
        <div class="price-sub">/ month</div>
        <ul class="price-features">
            <li>✓ Unlimited Lead Access</li>
            <li>✓ Real-time Alerts</li>
            <li>✓ 1 User Seat</li>
            <li style="color:#94a3b8;">— No CRM Integration</li>
        </ul>
        <div class="price-btn">Start Free Trial</div>
    </div>

    <div class="price-card price-card-vip">
        <div class="popular-tag">Most Popular</div>
        <div class="price-name">Agency (Built for Teams)</div>
        <div class="price-val">$199</div>
        <div class="price-sub">/ month</div>
        <ul class="price-features">
            <li>✓ Everything in Pro</li>
            <li>✓ 5 Team Seats (Sales/SDR)</li>
            <li>✓ Automated PDF Audits</li>
            <li>✓ HubSpot / Salesforce Sync</li>
        </ul>
        <div class="price-btn price-btn-vip">Scale Agency Now</div>
    </div>

    <div class="price-card">
        <div class="price-name">Enterprise Scale</div>
        <div class="price-val">Custom</div>
        <div class="price-sub">Billed Annually</div>
        <ul class="price-features">
            <li>✓ Unlimited Team Seats</li>
            <li>✓ Custom Data Pipelines</li>
            <li>✓ Dedicated Account Rep</li>
            <li>✓ Whitelabel Reports</li>
        </ul>
        <div class="price-btn">Contact Sales</div>
    </div>
</div>
""", unsafe_allow_html=True)