import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Platinux Agency — ROI Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS & Animations ───────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
  .main { background: #f8f7f4; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

  /* Animations */
  @keyframes fadeUp {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }
  @keyframes pulseHighlight {
    0% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(74, 222, 128, 0); }
    100% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }
  }

  .animate-up { animation: fadeUp 0.6s ease-out forwards; }
  .animate-in { animation: fadeIn 0.8s ease-out forwards; }
  
  /* Delay stagger for cards */
  .delay-1 { animation-delay: 0.1s; }
  .delay-2 { animation-delay: 0.2s; }
  .delay-3 { animation-delay: 0.3s; }

  /* Hero section */
  .hero {
    background: #0f0f0f;
    color: #fff;
    padding: 80px 60px 60px;
    text-align: center;
  }
  .hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 100px;
    padding: 6px 16px;
    font-size: 13px;
    color: #ccc;
    margin-bottom: 24px;
  }
  .hero h1 {
    font-size: 52px;
    font-weight: 700;
    line-height: 1.15;
    margin: 0 0 16px;
    letter-spacing: -1px;
  }
  .hero h1 span { color: #4ade80; }
  .hero p {
    font-size: 18px;
    color: #999;
    max-width: 600px;
    margin: 0 auto 40px;
    line-height: 1.6;
  }

  /* Section */
  .section { padding: 64px 60px; }
  .section-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 8px;
  }
  .section-title {
    font-size: 36px;
    font-weight: 700;
    color: #0f0f0f;
    margin-bottom: 8px;
    letter-spacing: -.5px;
  }
  .section-sub {
    font-size: 16px;
    color: #666;
    margin-bottom: 40px;
  }

  /* Metric cards */
  .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px; }
  .metric-card {
    flex: 1;
    min-width: 140px;
    background: #fff;
    border: 1px solid #e8e6e0;
    border-radius: 12px;
    padding: 20px;
    opacity: 0; /* for animation */
    transition: transform 0.2s ease;
  }
  .metric-card:hover { transform: translateY(-3px); }
  .metric-card .m-label { font-size: 12px; color: #888; margin-bottom: 6px; }
  .metric-card .m-value { font-size: 28px; font-weight: 700; color: #0f0f0f; }
  .metric-card .m-sub { font-size: 12px; color: #aaa; margin-top: 4px; }
  .metric-card.highlight { 
    background: #0f0f0f; 
    border-color: #0f0f0f; 
    animation: fadeUp 0.6s ease-out forwards, pulseHighlight 2s infinite; 
  }
  .metric-card.highlight .m-label { color: #888; }
  .metric-card.highlight .m-value { color: #4ade80; }
  .metric-card.highlight .m-sub { color: #666; }

  /* Comparison table */
  .compare-table { background: #fff; border: 1px solid #e8e6e0; border-radius: 16px; overflow: hidden; }
  .compare-header {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    background: #0f0f0f;
    color: #fff;
    padding: 14px 24px;
    font-size: 13px;
    font-weight: 600;
  }
  .compare-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    padding: 14px 24px;
    border-bottom: 1px solid #f0eeea;
    font-size: 14px;
    align-items: center;
  }
  .compare-row:last-child { border-bottom: none; }
  .compare-row .label { color: #555; }
  .compare-row .bad { color: #e24b4a; font-weight: 500; }
  .compare-row .good { color: #16a34a; font-weight: 500; }

  /* Insight cards */
  .insight-card {
    background: #fff;
    border: 1px solid #e8e6e0;
    border-left: 3px solid #4ade80;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin-bottom: 12px;
    font-size: 14px;
    color: #444;
    line-height: 1.6;
    opacity: 0;
  }
  .insight-card b { color: #0f0f0f; font-weight: 600; }

  /* CTA section */
  .cta-section {
    background: #0f0f0f;
    color: #fff;
    padding: 80px 60px;
    text-align: center;
  }
  .cta-section h2 { font-size: 40px; font-weight: 700; margin-bottom: 16px; letter-spacing: -.5px; }
  .cta-section p { font-size: 18px; color: #888; margin-bottom: 40px; }

  /* Hide streamlit branding */
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }
  .divider { height: 1px; background: #e8e6e0; margin: 0 60px; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero animate-in">
  <div class="hero-badge animate-up delay-1">⚡ platinux.net/agency — ROI Calculator</div>
  <h1 class="animate-up delay-1">Stop scaling your sales team.<br>Scale your <span>lead flow.</span></h1>
  <p class="animate-up delay-2">Platinux tracks founders and enterprises actively requesting custom development, SaaS builds, and design overhauls. Reach high-ticket clients before they post on Upwork.</p>
</div>
""", unsafe_allow_html=True)

# ── ROI CALCULATOR SECTION ────────────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label animate-in">Agency Economics</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title animate-in">Calculate your true net profit</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub animate-in">Model your agency overhead and see what a single $199 subscription yields.</div>', unsafe_allow_html=True)

# ── Inputs ────────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown("**Your Agency Profile**")

    currency = st.selectbox("Your currency", ["USD ($)", "INR (₹)"], key="currency")
    is_inr = currency == "INR (₹)"
    sym = "₹" if is_inr else "$"
    
    # Agency Pricing
    plan_cost = 17999 if is_inr else 199

    if is_inr:
        avg_project = st.slider("Average project size (₹)", 50000, 2000000, 400000, step=50000)
    else:
        avg_project = st.slider("Average deal size ($)", 2000, 50000, 8000, step=1000)

    leads_per_month = st.slider("Platinux Leads worked per month", 20, 300, 100, step=10)
    conversion_rate = st.slider("Close rate (%)", 1, 20, 3, step=1)
    agency_margin = st.slider("Net Profit Margin (%)", 10, 80, 40, step=5)
    sdr_cost = st.slider("Current Outbound/Ad spend per month", 500, 10000, 2000, step=500) if not is_inr else st.slider("Current Outbound/Ad spend per month (₹)", 40000, 800000, 150000, step=20000)

with col_right:
    st.markdown("**Your Agency Results**")

    # Agency Core Calculations
    clients_per_month = leads_per_month * (conversion_rate / 100)
    monthly_revenue = clients_per_month * avg_project
    monthly_overhead = monthly_revenue * (1 - (agency_margin / 100))
    monthly_profit = monthly_revenue - monthly_overhead
    net_gain = monthly_profit - plan_cost
    roi_x = round((monthly_profit / plan_cost) * 100) if plan_cost > 0 else 0
    annual_profit = net_gain * 12

    def fmt(n):
        if is_inr:
            if n >= 100000:
                return f"₹{n/100000:.1f}L"
            return f"₹{int(round(n)):,}"
        else:
            if n >= 1000:
                return f"${n/1000:.1f}k"
            return f"${int(round(n)):,}"

    # Animated Metric cards
    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card highlight animate-up">
        <div class="m-label">Agency ROI</div>
        <div class="m-value">{roi_x:,}%</div>
        <div class="m-sub">return on {sym}{plan_cost:,}/mo</div>
      </div>
      <div class="metric-card animate-up delay-1">
        <div class="m-label">Gross Revenue / Mo</div>
        <div class="m-value">{fmt(monthly_revenue)}</div>
        <div class="m-sub">{clients_per_month:.1f} deals closed</div>
      </div>
    </div>
    <div class="metric-row">
      <div class="metric-card animate-up delay-2">
        <div class="m-label">Net Profit / Mo</div>
        <div class="m-value">{fmt(monthly_profit)}</div>
        <div class="m-sub">After {100-agency_margin}% dev overhead</div>
      </div>
      <div class="metric-card animate-up delay-3">
        <div class="m-label">Annual Net Profit</div>
        <div class="m-value">{fmt(annual_profit)}</div>
        <div class="m-sub">Minus Platinux fees</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    payback_clients = round(plan_cost / (avg_project * (agency_margin / 100)), 2)
    st.markdown(f"""
    <div class="insight-card animate-up delay-3">
      <b>Minimal Risk.</b> You only need to close <b>{payback_clients if payback_clients > 1 else "< 1"} deals</b> to completely cover your monthly Agency subscription from your <i>net profit</i> margin.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── CHART SECTION ─────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">12-Month Projection</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Scaling Profit, Not Headcount</div>', unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns([3, 2], gap="large")

with chart_col1:
    months = list(range(1, 13))
    # Traditional SDR/Ads: high fixed cost, slower margin growth
    sdr_monthly = [(monthly_profit * (1 + 0.02*i)) - sdr_cost for i in range(12)]
    # Platinux: high margin, compounding referrals
    platinux_monthly = [(monthly_profit * (1 + 0.05*i)) - plan_cost for i in range(12)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=[round(max(v,0)) for v in sdr_monthly],
        mode='lines+markers',
        name='Via Ads/Outbound SDR',
        line=dict(color='#e24b4a', width=2, dash='dot'),
        marker=dict(size=5),
    ))
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in platinux_monthly],
        mode='lines+markers',
        name='Via Platinux Agency',
        line=dict(color='#4ade80', width=3),
        marker=dict(size=6),
        fill='tozeroy',
        fillcolor='rgba(74,222,128,0.06)'
    ))
    fig.update_layout(
        paper_bgcolor='#ffffff', plot_bgcolor='#ffffff',
        font=dict(family='Inter', size=12, color='#555'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='left', x=0),
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis=dict(title='Month', showgrid=False, tickvals=months, ticktext=[f'M{m}' for m in months]),
        yaxis=dict(title=f'Net Profit ({sym})', showgrid=True, gridcolor='#f0eeea', tickformat=','),
        height=320
    )
    st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    # Donut chart — Agency Revenue breakdown
    labels = ['Agency Net Profit', f'Dev/Overhead ({(100-agency_margin)}%)', f'Platinux Cost']
    values = [monthly_profit - plan_cost, monthly_overhead, plan_cost]
    colors = ['#4ade80', '#e8e6e0', '#0f0f0f']

    fig2 = go.Figure(go.Pie(
        labels=labels,
        values=[max(v, 0) for v in values],
        hole=0.6,
        marker=dict(colors=colors, line=dict(color='#fff', width=2)),
        textinfo='label+percent',
        textfont=dict(size=11),
        hovertemplate='%{label}: %{value:,}<extra></extra>'
    ))
    fig2.update_layout(
        paper_bgcolor='#ffffff', showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0), height=320,
        annotations=[dict(
            text=f"{fmt(monthly_profit - plan_cost)}<br><span style='font-size:11px'>true profit</span>",
            x=0.5, y=0.5, font_size=14, showarrow=False
        )]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── COMPARISON TABLE ──────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Acquisition Comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Platinux vs Paid Acquisition</div>', unsafe_allow_html=True)

sdr_yearly = sdr_cost * 12
plat_yearly = plan_cost * 12

st.markdown(f"""
<div class="compare-table animate-up">
  <div class="compare-header">
    <span></span>
    <span>B2B Ads / Outbound SDR</span>
    <span>Platinux Agency</span>
  </div>
  <div class="compare-row">
    <span class="label">Lead Intent</span>
    <span class="bad">Cold (Interruptive)</span>
    <span class="good">Hot (Actively Asking)</span>
  </div>
  <div class="compare-row">
    <span class="label">Cost to scale</span>
    <span class="bad">Higher spend = more leads</span>
    <span class="good">Unlimited leads (Flat Rate)</span>
  </div>
  <div class="compare-row">
    <span class="label">Lead Exclusivity</span>
    <span class="bad">Bidding against competitors</span>
    <span class="good">You reach out first</span>
  </div>
  <div class="compare-row">
    <span class="label">Annual Acquisition Cost</span>
    <span class="bad">{fmt(sdr_yearly)}</span>
    <span class="good">{fmt(plat_yearly)} flat</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── PRICING SECTION ───────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Agency Plans</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">One deal covers the year.</div>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3, gap="medium")

if is_inr:
    pro_p, agency_p, scale_p = "₹1,999", "₹17,999", "Custom"
    agency_yr = "₹160,000/yr"
else:
    pro_p, agency_p, scale_p = "$79", "$199", "$499+"
    agency_yr = "$1,899/yr"

with p1:
    st.markdown(f"""
    <div class="metric-card" style="height:100%;min-height:320px">
      <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">Pro (Solo Devs)</div>
      <div style="font-size:32px;font-weight:700;color:#0f0f0f;margin-bottom:4px">{pro_p}</div>
      <div style="font-size:13px;color:#aaa;margin-bottom:20px">/ mo</div>
      <div style="font-size:13px;color:#555;line-height:2">
        ✓ Unlimited leads<br>
        ✓ Real-time alerts<br>
        ✓ 1 User Seat<br>
        — No team routing<br>
        — No CRM integrations
      </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown(f"""
    <div class="metric-card highlight animate-up" style="height:100%;min-height:320px">
      <div style="font-size:11px;color:#4ade80;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">Agency — Built for Teams</div>
      <div style="font-size:32px;font-weight:700;color:#fff;margin-bottom:4px">{agency_p}</div>
      <div style="font-size:13px;color:#666;margin-bottom:20px">/ mo · or {agency_yr}</div>
      <div style="font-size:13px;color:#ccc;line-height:2">
        ✓ Everything in Pro<br>
        ✓ 5 Team Seats (Sales/SDR)<br>
        ✓ Slack / Discord Routing<br>
        ✓ HubSpot / Salesforce Sync<br>
        ✓ API Access
      </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown(f"""
    <div class="metric-card" style="height:100%;min-height:320px">
      <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">Enterprise Scale</div>
      <div style="font-size:32px;font-weight:700;color:#0f0f0f;margin-bottom:4px">{scale_p}</div>
      <div style="font-size:13px;color:#aaa;margin-bottom:20px">/ mo</div>
      <div style="font-size:13px;color:#555;line-height:2">
        ✓ Unlimited Team Seats<br>
        ✓ Custom Data Pipelines<br>
        ✓ Dedicated Account Rep<br>
        ✓ Whitelabel Reports
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── CTA SECTION ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="cta-section">
  <h2>Feed your sales team.</h2>
  <p>At {sym}{plan_cost:,}/mo, Platinux is a fraction of the cost of a single SDR.<br>
     Fill your agency pipeline today.</p>
  <div style="font-size:14px;color:#666;margin-top:32px">
    platinux.net/agency · 14-Day Free Trial for Teams
  </div>
</div>
""", unsafe_allow_html=True)
