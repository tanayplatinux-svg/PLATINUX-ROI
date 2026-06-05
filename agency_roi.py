import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Platinux Agency - ROI Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "currency" not in st.session_state:
    st.session_state.currency = "USD ($)"

if "prev_currency" not in st.session_state:
    st.session_state.prev_currency = st.session_state.currency

if "avg_project" not in st.session_state:
    st.session_state.avg_project = 8000

if st.session_state.currency != st.session_state.prev_currency:
    if st.session_state.currency == "INR (₹)":
        st.session_state.avg_project = 400000
    else:
        st.session_state.avg_project = 8000
    st.session_state.prev_currency = st.session_state.currency

is_inr = st.session_state.currency == "INR (₹)"
sym = "₹" if is_inr else "$"
plan_cost = 17999 if is_inr else 199

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap');

  html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #ffffff;
    color: #0f0f0f;
  }
  .main { background: #ffffff; }

  .block-container {
    padding-left: 5% !important;
    padding-right: 5% !important;
    max-width: 90% !important;
  }

  @keyframes fadeUp {
    0%  { opacity: 0; transform: translateY(24px); }
    100%{ opacity: 1; transform: translateY(0);    }
  }
  @keyframes fadeIn {
    0%  { opacity: 0; }
    100%{ opacity: 1; }
  }
  @keyframes pulseHighlight {
    0%  { box-shadow: 0 0 0 0   rgba(0,196,140,0.4); }
    70% { box-shadow: 0 0 0 10px rgba(0,196,140,0);   }
    100%{ box-shadow: 0 0 0 0   rgba(0,196,140,0);   }
  }

  .animate-up { animation: fadeUp 0.8s cubic-bezier(0.16,1,0.3,1) forwards; }
  .animate-in { animation: fadeIn 1s ease-out forwards; }
  .delay-1 { animation-delay: 100ms; }
  .delay-2 { animation-delay: 220ms; }

  /* ── HERO (white bg, black text) ── */
  .hero {
    background: #ffffff;
    color: #0f0f0f;
    padding: 72px 40px 64px;
    text-align: center;
    border-radius: 24px;
    margin-top: 24px;
    border: 1.5px solid #e4e4e4;
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
  }
  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #f4f4f0;
    border: 1px solid #e4e4e4;
    border-radius: 100px;
    padding: 6px 18px;
    font-size: 12px;
    font-weight: 600;
    color: #555;
    letter-spacing: .04em;
    margin-bottom: 28px;
  }
  .hero h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 50px;
    font-weight: 400;
    line-height: 1.15;
    color: #0f0f0f;
    margin: 0 0 18px;
    letter-spacing: -.5px;
  }
  .hero h1 span { color: #00c48c; font-style: italic; }
  .hero p {
    font-size: 17px;
    color: #555;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.65;
  }

  /* ── SECTIONS ── */
  .section { padding: 40px 0; }
  .section-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #00c48c;
    margin-bottom: 8px;
  }
  .section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 36px;
    font-weight: 400;
    color: #0f0f0f;
    margin-bottom: 12px;
    letter-spacing: -.3px;
  }
  .section-title em {
    font-style: italic;
    background: rgba(0,196,140,0.15);
    border-radius: 6px;
    padding: 0 6px;
  }
  .section-sub {
    font-size: 15.5px;
    color: #555;
    margin-bottom: 40px;
    max-width: 620px;
    line-height: 1.65;
  }

  /* ── TIMELINE ── */
  .timeline-container {
    position: relative;
    max-width: 1100px;
    margin: 40px auto;
    padding: 20px 0;
  }
  .timeline-container::after {
    content: '';
    position: absolute;
    width: 2px;
    background: #e4e4e4;
    top: 0; bottom: 0;
    left: 50%;
    margin-left: -1px;
    z-index: 1;
  }
  .timeline-block {
    position: relative;
    margin-bottom: 40px;
    width: 100%;
    display: flex;
    justify-content: flex-start;
    z-index: 2;
  }
  .timeline-block:nth-child(even) { justify-content: flex-end; }
  .timeline-pointer {
    width: 50%;
    padding-right: 40px;
    box-sizing: border-box;
  }
  .timeline-block:nth-child(even) .timeline-pointer {
    padding-right: 0;
    padding-left: 40px;
  }
  .timeline-icon {
    position: absolute;
    width: 40px; height: 40px;
    left: 50%; top: 24px;
    margin-left: -20px;
    background: #fff;
    border: 2px solid #e4e4e4;
    border-radius: 50%;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 14px;
    color: #0f0f0f;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }

  .plx-step-card {
    background: #fff;
    border: 1.5px solid #e4e4e4;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.02);
    transition: all 0.35s cubic-bezier(0.16,1,0.3,1);
  }
  .plx-step-card:hover {
    border-color: #00c48c;
    box-shadow: 0 12px 30px rgba(0,196,140,0.10);
    transform: translateY(-2px);
  }
  .plx-step-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .05em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 100px;
    margin-bottom: 14px;
  }
  .plx-step-title {
    font-size: 20px;
    font-weight: 700;
    color: #0f0f0f;
    margin-bottom: 8px;
    letter-spacing: -.3px;
  }
  .plx-step-desc {
    font-size: 14.5px;
    color: #4b5563;
    line-height: 1.65;
  }
  .plx-step-detail {
    margin-top: 14px;
    font-size: 13px;
    color: #6b7280;
    line-height: 1.55;
  }
  .plx-step-detail strong { color: #0f0f0f; }

  .plx-notif {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    background: #f9f9f7;
    border: 1px solid #e4e4e4;
    border-radius: 12px;
    padding: 12px 16px;
    margin-top: 16px;
  }
  .plx-notif-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #00c48c;
    margin-top: 5px;
    flex-shrink: 0;
  }
  .plx-notif-text { font-size: 13px; color: #4b5563; line-height: 1.55; }

  /* VIP dark card */
  .plx-money-card {
    background: #0f0f0f;
    border: 2px solid #00c48c !important;
    position: relative;
    overflow: hidden;
  }
  .plx-money-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at top left, rgba(0,196,140,0.15) 0%, transparent 70%);
    pointer-events: none;
  }
  .plx-money-card .plx-step-title { color: #fff; }
  .plx-money-card .plx-step-desc  { color: #d1d5db; }
  .plx-money-card .plx-step-detail { color: #9ca3af; }
  .plx-money-card .plx-step-detail strong { color: #00c48c; }
  .plx-money-amount {
    font-size: 36px;
    font-weight: 700;
    color: #00c48c;
    letter-spacing: -1px;
    margin-top: 12px;
    display: block;
  }

  /* ── METRIC CARDS ── */
  .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 20px; }
  .metric-card {
    flex: 1;
    min-width: 140px;
    background: #fff;
    border: 1.5px solid #e4e4e4;
    border-radius: 16px;
    padding: 22px;
    transition: all 0.3s ease;
  }
  .metric-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.05); }
  .metric-card .m-label { font-size: 13px; color: #6b7280; font-weight: 500; margin-bottom: 6px; }
  .metric-card .m-value { font-size: 28px; font-weight: 700; color: #0f0f0f; }
  .metric-card .m-sub   { font-size: 12px; color: #9ca3af; margin-top: 4px; }
  .metric-card.highlight {
    background: #0f0f0f;
    border-color: #0f0f0f;
    animation: pulseHighlight 2.5s infinite;
  }
  .metric-card.highlight .m-label { color: #9ca3af; }
  .metric-card.highlight .m-value { color: #00c48c; }
  .metric-card.highlight .m-sub   { color: #4b5563; }

  /* Insight card */
  .insight-card {
    background: #fff;
    border: 1.5px solid #e4e4e4;
    border-left: 4px solid #00c48c;
    border-radius: 0 14px 14px 0;
    padding: 18px 20px;
    margin-top: 8px;
    font-size: 14px;
    color: #4b5563;
    line-height: 1.65;
  }
  .insight-card b { color: #0f0f0f; font-weight: 700; }

  /* Pricing card inside ROI */
  .pricing-pill {
    background: #ecfdf5;
    border: 1.5px solid rgba(0,196,140,0.35);
    border-radius: 12px;
    padding: 18px 20px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 18px;
  }
  .pricing-pill-label { font-size: 13px; font-weight: 600; color: #0f0f0f; }
  .pricing-pill-sub   { font-size: 12px; color: #555; margin-top: 2px; }
  .pricing-pill-price {
    font-size: 26px;
    font-weight: 700;
    color: #00c48c;
    white-space: nowrap;
  }

  /* ── CTA / FOOTER (white bg, black text) ── */
  .cta-section {
    background: #ffffff;
    color: #0f0f0f;
    padding: 72px 40px;
    text-align: center;
    border-radius: 24px;
    margin-bottom: 40px;
    border: 1.5px solid #e4e4e4;
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
  }
  .cta-section h2 {
    font-family: 'DM Serif Display', serif;
    font-size: 40px;
    font-weight: 400;
    color: #0f0f0f;
    margin-bottom: 16px;
    letter-spacing: -.5px;
  }
  .cta-section p { font-size: 17px; color: #555; margin-bottom: 24px; line-height: 1.65; }
  .cta-accent { color: #00c48c; font-weight: 700; }

  .divider { height: 1.5px; background: #e4e4e4; margin: 40px 0; }

  @media (max-width: 768px) {
    .hero h1 { font-size: 32px; }
    .section-title { font-size: 26px; }
    .timeline-container::after { left: 24px !important; }
    .timeline-block { justify-content: flex-start !important; }
    .timeline-pointer { width: calc(100% - 60px) !important; margin-left: auto !important; padding-right: 0 !important; }
    .timeline-icon { left: 24px !important; margin-left: -20px !important; }
  }

  #MainMenu { visibility: hidden; }
  footer     { visibility: hidden; }
  header     { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero animate-in">
  <div class="hero-badge animate-up delay-1">⚡ platinux.net/agency — ROI Calculator</div>
  <h1 class="animate-up delay-1">Your next client is already<br>looking for someone like <span>you.</span></h1>
  <p class="animate-up delay-2">Platinux finds businesses in your niche that need development, design, or a full site rebuild — and gets you in front of them before anyone else does.</p>
</div>
""", unsafe_allow_html=True)

# ── ROADMAP ───────────────────────────────────────────────────────────────────
timeline_template = """
<div class="section">
<div class="section-label">How it works</div>
<div class="section-title">From a cold list to a <em>paying client.</em></div>
<div class="section-sub">Here is the exact process Platinux uses to find businesses that need your help — and put them right in your inbox, ready to hear from you.</div>

<div class="timeline-container">

  <div class="timeline-block">
    <div class="timeline-icon">1</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#e6fcf5; color:#087f5b;">🔍 Finding Leads</div>
        <div class="plx-step-title">We scan for businesses in your space</div>
        <div class="plx-step-desc">Tell us what kind of work you do — web dev, design, SaaS builds, whatever — and Platinux scans thousands of live websites in that space every day. We look for signs that a business is overdue for a site refresh: broken layouts, slow pages, outdated design, poor mobile experience.</div>
        <div class="plx-notif">
          <div class="plx-notif-dot"></div>
          <div class="plx-notif-text"><strong>Example:</strong> 12,450 local B2B sites scanned in your niche → 1,000 flagged as strong prospects.</div>
        </div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">2</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#fff9db; color:#f08c00;">🎯 Narrowing Down</div>
        <div class="plx-step-title">We cut the noise — you get the best 100</div>
        <div class="plx-step-desc">Not every flagged site is worth your time. So we rank them by how likely they are to actually convert — based on site quality signals, business size, and niche fit. You end up with a tight list of 100 real prospects each month, not a messy spreadsheet of thousands to sort through yourself.</div>
        <div class="plx-step-detail">This means your sales team spends time talking to people, not hunting for people to talk to.</div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">3</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#e7f5ff; color:#1c7ed6;">📄 Personalised Audit Report</div>
        <div class="plx-step-title">Each lead gets their own audit — automatically</div>
        <div class="plx-step-desc">For every lead on your list, Platinux builds a custom audit report showing exactly what is wrong with their site. You send it as part of your outreach — and instead of a cold pitch, you are leading with something genuinely useful.</div>
        <div class="plx-step-detail">Agencies that send personalised audits see 3× more replies than those sending generic outreach messages.</div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon" style="border-color:#00c48c; background:#0f0f0f; color:#fff;">4</div>
    <div class="timeline-pointer">
      <div class="plx-step-card plx-money-card">
        <div class="plx-step-tag" style="background:rgba(0,196,140,.15); color:#00c48c;">💰 Getting Paid</div>
        <div class="plx-step-title">Send the audit. Book the call. Close the deal.</div>
        <div class="plx-step-desc">You reach out with a report that already shows you understand their business. No gatekeepers, no generic pitches. Just a practical conversation about fixing something they already know is broken.</div>
        <span class="plx-money-amount">+[SYM][VAL_DEMO]</span>
        <div class="plx-step-detail" style="margin-top:16px">Platinux cost: <strong>[SYM][PLAN_COST]/mo</strong> &nbsp;·&nbsp; Close one deal. The tool pays for itself.</div>
      </div>
    </div>
  </div>

</div>
</div>
"""

val_demo = "8,000" if not is_inr else "4,00,000"
st.markdown(
    timeline_template
        .replace("[SYM]", sym)
        .replace("[PLAN_COST]", f"{plan_cost:,}")
        .replace("[VAL_DEMO]", val_demo),
    unsafe_allow_html=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── ROI CALCULATOR ────────────────────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Agency Economics</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">See what the numbers look like for your agency</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Model your returns based on a steady stream of <strong>100 verified leads per month</strong>.</div>', unsafe_allow_html=True)

calc_left, calc_right = st.columns([1, 1], gap="large")

with calc_left:
    st.markdown("### Your Agency Profile")

    currency_choice = st.selectbox(
        "Currency",
        ["USD ($)", "INR (₹)"],
        key="currency",
        label_visibility="visible"
    )

    # Pricing parameter shown here inside the ROI section
    if is_inr:
        plan_options = {"Starter — ₹999/mo": 999, "Agency — ₹17,999/mo": 17999, "Scale — ₹39,999/mo": 39999}
    else:
        plan_options = {"Starter — $49/mo": 49, "Agency — $199/mo": 199, "Scale — $499/mo": 499}

    selected_plan_label = st.selectbox("Platinux Plan", list(plan_options.keys()))
    plan_cost = plan_options[selected_plan_label]

    st.markdown(f"""
    <div class="pricing-pill">
      <div>
        <div class="pricing-pill-label">{selected_plan_label.split("—")[0].strip()}</div>
        <div class="pricing-pill-sub">100 verified leads/mo · Audit reports included</div>
      </div>
      <div class="pricing-pill-price">{sym}{plan_cost:,}<span style="font-size:14px;color:#888;font-weight:500">/mo</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f4f4f0; border-radius:12px; padding:14px 18px; display:flex; align-items:center; gap:14px; margin-bottom:20px;">
      <div style="background:#00c48c; color:#fff; font-weight:700; font-size:18px; width:40px; height:40px; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">100</div>
      <div>
        <div style="font-size:13px; font-weight:700; color:#0f0f0f;">Leads per month — fixed</div>
        <div style="font-size:12px; color:#555; margin-top:2px;">We keep the model conservative. Platinux typically delivers more.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if is_inr:
        avg_project = st.slider("Average deal size (₹)", 50000, 2000000, key="avg_project", step=50000)
    else:
        avg_project = st.slider("Average deal size ($)", 2000, 50000, key="avg_project", step=1000)

    conversion_rate = st.slider("Lead close rate (%)", 1, 20, 3, key="conversion_rate", step=1)
    agency_margin   = st.slider("Net profit margin (%)", 10, 80, 40, key="agency_margin", step=5)

# ── CALCULATIONS ──────────────────────────────────────────────────────────────
leads_per_month   = 100
clients_per_month = leads_per_month * (conversion_rate / 100)
monthly_revenue   = clients_per_month * avg_project
monthly_overhead  = monthly_revenue * (1 - (agency_margin / 100))
monthly_profit    = monthly_revenue - monthly_overhead
net_gain          = monthly_profit - plan_cost
roi_x             = round((monthly_profit / plan_cost) * 100) if plan_cost > 0 else 0
annual_profit     = net_gain * 12

def fmt(n):
    if is_inr:
        if n >= 100000: return f"₹{n/100000:.1f}L"
        return f"₹{int(round(n)):,}"
    else:
        if n >= 1000: return f"${n/1000:.1f}k"
        return f"${int(round(n)):,}"

deals_str = f"{clients_per_month:.1f}" if clients_per_month % 1 != 0 else f"{int(clients_per_month)}"

with calc_right:
    st.markdown("### Your Monthly Results")

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card highlight">
        <div class="m-label">Agency ROI</div>
        <div class="m-value">{roi_x:,}%</div>
        <div class="m-sub">Return on {sym}{plan_cost:,}/mo</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Gross Revenue / Mo</div>
        <div class="m-value">{fmt(monthly_revenue)}</div>
        <div class="m-sub">{deals_str} deals closed</div>
      </div>
    </div>
    <div class="metric-row">
      <div class="metric-card">
        <div class="m-label">Net Profit / Mo</div>
        <div class="m-value">{fmt(monthly_profit)}</div>
        <div class="m-sub">After {100 - agency_margin}% overhead</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Annual Net Profit</div>
        <div class="m-value">{fmt(annual_profit)}</div>
        <div class="m-sub">Minus Platinux fees</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    payback_clients = plan_cost / (avg_project * (agency_margin / 100)) if avg_project > 0 and agency_margin > 0 else 0
    payback_str = "less than 1 deal" if payback_clients < 1 else f"{payback_clients:.2f} deals"

    st.markdown(f"""
    <div class="insight-card">
      <b>Very low risk.</b> At your current deal size and margin, you only need to close <b>{payback_str}</b> to cover your entire monthly Platinux subscription. Everything after that is profit.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── CTA / FOOTER (white bg, black text) ───────────────────────────────────────
st.markdown(f"""
<div class="cta-section">
  <h2>Your next client is out there right now.</h2>
  <p>At <span class="cta-accent">{sym}{plan_cost:,}/mo</span>, Platinux costs less than one hour of an SDR's time — and works around the clock.<br>Start your 14-day free trial and see who is ready to hire your agency today.</p>
  <div style="font-size:13px; color:#999; margin-top:28px; letter-spacing:.04em;">
    platinux.net/agency &nbsp;·&nbsp; 14-Day Free Trial &nbsp;·&nbsp; No credit card required
  </div>
</div>
""", unsafe_allow_html=True)
