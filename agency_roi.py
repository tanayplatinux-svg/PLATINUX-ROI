import streamlit as st
import plotly.graph_objects as go

# Set up page configurations for an immersive, premium, responsive layout
st.set_page_config(
    page_title="Platinux Agency - ROI Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# We use a standard triple-quoted string without f-prefix to prevent curly brace SyntaxErrors
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif; 
    background-color: #f8f7f4;
    color: #0f0f0f;
  }
  .main { background: #f8f7f4; }
  
  /* Responsive margins for content container */
  .block-container { 
    padding-left: 5% !important; 
    padding-right: 5% !important; 
    max-width: 90% !important; 
  }

  /* Keyframe animations */
  @keyframes fadeUp {
    0% { opacity: 0; transform: translateY(30px); }
    100% { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }
  @keyframes pulseHighlight {
    0% { box-shadow: 0 0 0 0 rgba(0, 196, 140, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(0, 196, 140, 0); }
    100% { box-shadow: 0 0 0 0 rgba(0, 196, 140, 0); }
  }

  .animate-up { animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
  .animate-in { animation: fadeIn 1s ease-out forwards; }
  .delay-1 { animation-delay: 100ms; }
  .delay-2 { animation-delay: 200ms; }

  /* Hero Banner section styling */
  .hero {
    background: #0f0f0f;
    color: #fff;
    padding: 80px 40px;
    text-align: center;
    border-radius: 24px;
    margin-top: 24px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
  }
  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 100px;
    padding: 6px 16px;
    font-size: 13px;
    color: #e5e7eb;
    margin-bottom: 24px;
  }
  .hero h1 {
    font-size: 52px;
    font-weight: 700;
    line-height: 1.15;
    margin: 0 0 16px;
    letter-spacing: -1.5px;
  }
  .hero h1 span { color: #00c48c; }
  .hero p {
    font-size: 18px;
    color: #9ca3af;
    max-width: 650px;
    margin: 0 auto 10px;
    line-height: 1.6;
  }

  /* Section text styling */
  .section { padding: 40px 0px; }
  .section-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #6b7280;
    margin-bottom: 8px;
  }
  .section-title {
    font-size: 38px;
    font-weight: 700;
    color: #0f0f0f;
    margin-bottom: 12px;
    letter-spacing: -.5px;
  }
  .section-title em {
    font-style: normal;
    background: rgba(0, 196, 140, 0.2);
    border-radius: 6px;
    padding: 0 8px;
  }
  .section-sub {
    font-size: 16px;
    color: #4b5563;
    margin-bottom: 40px;
    max-width: 650px;
    line-height: 1.6;
  }

  /* ── 4-STEP PERFECT TIMELINE GRAPHICS ── */
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
    top: 0;
    bottom: 0;
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
  .timeline-block:nth-child(even) {
    justify-content: flex-end;
  }
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
    width: 40px;
    height: 40px;
    left: 50%;
    top: 24px;
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
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .plx-step-card:hover {
    border-color: #00c48c;
    box-shadow: 0 12px 30px rgba(0,196,140,0.12);
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
    letter-spacing: -.4px;
  }
  .plx-step-desc {
    font-size: 14.5px;
    color: #4b5563;
    line-height: 1.6;
  }
  .plx-step-detail {
    margin-top: 14px;
    font-size: 13px;
    color: #6b7280;
    line-height: 1.5;
  }
  .plx-step-detail strong {
    color: #0f0f0f;
  }

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
  .plx-notif-text {
    font-size: 13px;
    color: #4b5563;
    line-height: 1.5;
  }

  /* Premium highlight callout card */
  .plx-money-card {
    background: #0f0f0f;
    border: 2.5px solid #00c48c;
    position: relative;
    overflow: hidden;
  }
  .plx-money-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at top left, rgba(0,196,140,0.18) 0%, transparent 70%);
    pointer-events: none;
  }
  .plx-money-card .plx-step-title { color: #fff; }
  .plx-money-card .plx-step-desc { color: #d1d5db; }
  .plx-money-card .plx-step-detail { color: #9ca3af; }
  .plx-money-card .plx-step-detail strong { color: #00c48c; }
  .plx-money-amount {
    font-size: 38px;
    font-weight: 700;
    color: #00c48c;
    letter-spacing: -1px;
    margin-top: 12px;
    display: block;
  }

  /* Dynamic highlight styling for dashboard indicators */
  .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px; }
  .metric-card {
    flex: 1;
    min-width: 140px;
    background: #fff;
    border: 1.5px solid #e4e4e4;
    border-radius: 16px;
    padding: 24px;
    transition: all 0.3s ease;
  }
  .metric-card:hover { transform: translateY(-3px); }
  .metric-card .m-label { font-size: 13px; color: #6b7280; font-weight: 500; margin-bottom: 6px; }
  .metric-card .m-value { font-size: 30px; font-weight: 700; color: #0f0f0f; }
  .metric-card .m-sub { font-size: 12px; color: #9ca3af; margin-top: 4px; }
  .metric-card.highlight { 
    background: #0f0f0f; 
    border-color: #0f0f0f; 
    animation: pulseHighlight 2.5s infinite; 
  }
  .metric-card.highlight .m-label { color: #9ca3af; }
  .metric-card.highlight .m-value { color: #00c48c; }
  .metric-card.highlight .m-sub { color: #4b5563; }

  /* Grid matrix design for comparison blocks */
  .compare-table { background: #fff; border: 1.5px solid #e4e4e4; border-radius: 20px; overflow: hidden; }
  .compare-header {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    background: #0f0f0f;
    color: #fff;
    padding: 18px 24px;
    font-size: 14px;
    font-weight: 600;
  }
  .compare-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    padding: 18px 24px;
    border-bottom: 1px solid #e4e4e4;
    font-size: 14px;
    align-items: center;
  }
  .compare-row:last-child { border-bottom: none; }
  .compare-row .label { color: #4b5563; font-weight: 500; }
  .compare-row .bad { color: #e24b4a; font-weight: 600; }
  .compare-row .good { color: #16a34a; font-weight: 600; }

  .insight-card {
    background: #fff;
    border: 1.5px solid #e4e4e4;
    border-left: 4px solid #00c48c;
    border-radius: 0 16px 16px 0;
    padding: 20px;
    margin-bottom: 12px;
    font-size: 14.5px;
    color: #4b5563;
    line-height: 1.6;
    box-shadow: 0 2px 10px rgba(0,0,0,0.01);
  }
  .insight-card b { color: #0f0f0f; font-weight: 700; }

  /* Call-to-action details */
  .cta-section {
    background: #0f0f0f;
    color: #fff;
    padding: 80px 40px;
    text-align: center;
    border-radius: 24px;
    margin-bottom: 40px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
  }
  .cta-section h2 { font-size: 40px; font-weight: 700; margin-bottom: 16px; letter-spacing: -1px; }
  .cta-section p { font-size: 18px; color: #9ca3af; margin-bottom: 40px; }

  .divider { height: 1.5px; background: #e4e4e4; margin: 40px 0px; }

  /* ── RESPONSIVE MOBILE HANDLERS ── */
  @media (max-width: 768px) {
    .timeline-container::after { left: 24px !important; }
    .timeline-block { justify-content: flex-start !important; }
    .timeline-pointer { width: calc(100% - 60px) !important; margin-left: auto !important; padding-right: 0 !important; }
    .timeline-icon { left: 24px !important; margin-left: -20px !important; }
  }

  /* Unclutter standard Streamlit frame margins */
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero animate-in">
  <div class="hero-badge animate-up delay-1">⚡ platinux.net/agency - ROI Calculator</div>
  <h1 class="animate-up delay-1">Stop scaling your sales team.<br>Scale your <span>lead flow.</span></h1>
  <p class="animate-up delay-2">Platinux tracks founders and enterprises actively requesting custom development, SaaS builds, and design overhauls. Reach high-ticket clients before they post on Upwork.</p>
</div>
""", unsafe_allow_html=True)

# We use replace() systematically inside standard Python strings to avoid format/braces issues
timeline_template = """
<div class="section">
<div class="section-label">🗺 Your path to clients</div>
<div class="section-title">From <em>zero</em> to paid. In 4 steps.</div>
<div class="section-sub">Here's exactly how Platinux turns a business owner's post into money in your account — and why responding first is everything.</div>

<div class="timeline-container">

  <!-- Step 1: Left -->
  <div class="timeline-block">
    <div class="timeline-icon">1</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#e6fcf5; color:#087f5b;">🔍 Intent</div>
        <div class="plx-step-title">Business owner posts online</div>
        <div class="plx-step-desc">Somewhere on Reddit, LinkedIn, or Twitter, a real business owner types "looking for a web developer." It goes live publicly.</div>
        <div class="plx-notif">
          <div class="plx-notif-dot"></div>
          <div class="plx-notif-text"><strong>r/entrepreneur:</strong> "Need someone to build a site for my salon — budget [SYM]2,000, want it done this month."</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Step 2: Right -->
  <div class="timeline-block">
    <div class="timeline-icon">2</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#fff9db; color:#f08c00;">⚡ Speed</div>
        <div class="plx-step-title">Platinux alerts you instantly</div>
        <div class="plx-step-desc">Our engine scans 7+ platforms 24/7. The second the post goes live, we capture it, verify it's a real business, and send you a real-time ping.</div>
        <div class="plx-notif">
          <div class="plx-notif-dot"></div>
          <div class="plx-notif-text"><strong>🔔 Alert:</strong> Salon owner · Reddit · Budget ~[SYM]2k · Posted 45s ago → <span style="color:#00c48c; font-weight:600; cursor:pointer;">View post</span></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Step 3: Left -->
  <div class="timeline-block">
    <div class="timeline-icon">3</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#e7f5ff; color:#1c7ed6;">💬 Action</div>
        <div class="plx-step-title">You reply first</div>
        <div class="plx-step-desc">You go directly to the post and respond. The business owner gets your message before they've even seen 10 other pitches. No platform middleman.</div>
        <div class="plx-step-detail">Agencies who respond within 1 hour close at <strong>3× the rate</strong>.</div>
      </div>
    </div>
  </div>

  <!-- Step 4: Right (Premium Highlight) -->
  <div class="timeline-block">
    <div class="timeline-icon" style="border-color:#00c48c; background:#0f0f0f; color:#fff;">4</div>
    <div class="timeline-pointer">
      <div class="plx-step-card plx-money-card">
        <div class="plx-step-tag" style="background:rgba(0,196,140,.15); color:#00c48c;">💰 ROI</div>
        <div class="plx-step-title">Project delivered. Money in.</div>
        <div class="plx-step-desc">You build, deliver, and get paid. No Upwork commissions eating 20% of your income. Just you, the client, and the full project value.</div>
        <span class="plx-money-amount">+[SYM]3,200</span>
        <div class="plx-step-detail" style="margin-top:16px">Platinux cost: <strong>[SYM][PLAN_COST]/mo</strong>&nbsp;&nbsp;·&nbsp;&nbsp;Your ROI: <strong>Massive</strong></div>
      </div>
    </div>
  </div>

</div>
</div>
"""

currency_choice = st.selectbox("Currency Selection", ["USD ($)", "INR (₹)"], label_visibility="collapsed")
is_inr = currency_choice == "INR (₹)"
sym = "₹" if is_inr else "$"
plan_cost = 17999 if is_inr else 199
sdr_cost = 150000 if is_inr else 2000

# Render the custom-rendered responsive HTML timeline
st.markdown(
    timeline_template.replace("[SYM]", sym).replace("[PLAN_COST]", f"{plan_cost:,}"), 
    unsafe_allow_html=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Agency Economics</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Calculate your true net profit</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Model your agency overhead based on a steady stream of <strong>100 verified hot leads per month</strong>.</div>', unsafe_allow_html=True)

calc_col_left, calc_col_right = st.columns([1, 1], gap="large")

with calc_col_left:
    st.markdown("### **Your Agency Profile**")
    
    # 100 Leads Month Fixed Marker Indicator (no longer a slider)
    st.markdown(f"""
    <div style="background-color: #ecfdf5; border: 1.5px solid rgba(0, 196, 140, 0.3); border-radius: 12px; padding: 16px; display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">
        <div style="background-color: #00c48c; color: white; font-weight: 700; font-size: 20px; width: 44px; height: 44px; border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">100</div>
        <div>
            <h4 style="margin: 0; font-size: 14px; font-weight: 700; color: #0f0f0f;">Hot Leads per Month</h4>
            <p style="margin: 4px 0 0 0; font-size: 12px; color: #4b5563; line-height: 1.4;">Platinux delivers hundreds of leads. We are modeling your ROI conservatively on just 100 leads worked per month.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Set up slider configurations dynamically based on currency choice
    if is_inr:
        avg_project = st.slider("Average deal size (₹)", 50000, 2000000, 400000, step=50000)
    else:
        avg_project = st.slider("Average deal size ($)", 2000, 50000, 8000, step=1000)

    conversion_rate = st.slider("Lead Close Rate (%)", 1, 20, 3, step=1)
    agency_margin = st.slider("Net Profit Margin (%)", 10, 80, 40, step=5)

leads_per_month = 100
clients_per_month = leads_per_month * (conversion_rate / 100)
monthly_revenue = clients_per_month * avg_project
monthly_overhead = monthly_revenue * (1 - (agency_margin / 100))
monthly_profit = monthly_revenue - monthly_overhead
net_gain = monthly_profit - plan_cost
roi_x = round((monthly_profit / plan_cost) * 100) if plan_cost > 0 else 0
annual_profit = net_gain * 12

def fmt(n):
    if is_inr:
        if n >= 100000: return f"₹{n/100000:.1f}L"
        return f"₹{int(round(n)):,}"
    else:
        if n >= 1000: return f"${n/1000:.1f}k"
        return f"${int(round(n)):,}"

deals_closed_str = f"{clients_per_month:.1f}" if clients_per_month % 1 != 0 else f"{int(clients_per_month)}"

with calc_col_right:
    st.markdown("### **Your Monthly Results**")
    
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
        <div class="m-sub">{deals_closed_str} deals closed</div>
      </div>
    </div>
    <div class="metric-row">
      <div class="metric-card">
        <div class="m-label">Net Profit / Mo</div>
        <div class="m-value">{fmt(monthly_profit)}</div>
        <div class="m-sub">After {100-agency_margin}% dev overhead</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Annual Net Profit</div>
        <div class="m-value">{fmt(annual_profit)}</div>
        <div class="m-sub">Minus Platinux fees</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    payback_clients = plan_cost / (avg_project * (agency_margin / 100))
    payback_str = "< 1 deal" if payback_clients < 1 else f"{payback_clients:.2f} deals"
    
    st.markdown(f"""
    <div class="insight-card">
      <b>Minimal Risk.</b> You only need to close <b>{payback_str}</b> to completely cover your monthly Agency subscription from your <i>net profit</i> margin alone.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">12-Month Projection</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Scaling Profit, Not Headcount</div>', unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns([3, 2], gap="large")

with chart_col1:
    months = list(range(1, 13))
    sdr_monthly = [max(0, (monthly_profit * (1 + 0.02*i)) - sdr_cost) for i in range(12)]
    platinux_monthly = [max(0, (monthly_profit * (1 + 0.05*i)) - plan_cost) for i in range(12)]

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
        line=dict(color='#00c48c', width=3),
        marker=dict(size=6),
        fill='tozeroy',
        fillcolor='rgba(0,196,140,0.06)'
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
    labels = ['Agency Net Profit', f'Dev/Overhead ({(100-agency_margin)}%)', f'Platinux Cost']
    true_profit = max(0, monthly_profit - plan_cost)
    values = [true_profit, monthly_overhead, plan_cost]
    colors = ['#00c48c', '#e4e4e4', '#0f0f0f']

    fig2 = go.Figure(go.Pie(
        labels=labels,
        values=values,
        hole=0.6,
        marker=dict(colors=colors, line=dict(color='#fff', width=2)),
        textinfo='percent',
        textfont=dict(size=11),
        hovertemplate='%{label}: %{value:,}<extra></extra>'
    ))
    fig2.update_layout(
        paper_bgcolor='#ffffff', showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0), height=320,
        annotations=[dict(
            text=f"<b>{fmt(true_profit)}</b><br><span style='font-size:10px;color:#888;font-weight:600;'>TRUE PROFIT</span>",
            x=0.5, y=0.5, font_size=15, font_family='Inter', showarrow=False
        )]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Acquisition Comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Platinux vs Paid Acquisition</div>', unsafe_allow_html=True)

sdr_yearly = sdr_cost * 12
plat_yearly = plan_cost * 12

st.markdown(f"""
<div class="compare-table">
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
    <span class="label">Cost to Scale</span>
    <span class="bad">Higher spend = more leads</span>
    <span class="good">100+ leads (Flat Rate)</span>
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

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Agency Plans</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">One deal covers the year.</div>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3, gap="medium")

if is_inr:
    pro_p, agency_p, scale_p = "₹1,999", f"₹{plan_cost:,}", "Custom"
    agency_yr = "₹160,000/yr"
else:
    pro_p, agency_p, scale_p = "$79", f"${plan_cost}", "$499+"
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
    <div class="metric-card highlight" style="height:100%;min-height:320px">
      <div style="font-size:11px;color:#00c48c;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">Agency — Built for Teams</div>
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
