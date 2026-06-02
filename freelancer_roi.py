import streamlit as st
import plotly.graph_objects as go

# ── 1. GLOBAL CONFIGURATION & MARGIN CONTROL ──────────────────────────────────
st.set_page_config(
    page_title="Platinux - Freelancer ROI Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom layout and spacing utilities
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif; 
  }
  .main { background: #f8f7f4; }
  
  /* FIXED MARGINS: Absolute padding configuration on left and right-hand side of the page */
  .block-container { 
    padding-left: 5% !important; 
    padding-right: 5% !important; 
    max-width: 90% !important; 
  }

  /* Global Layout Animations */
  @keyframes fadeUp {
    0% { opacity: 0; transform: translateY(40px); }
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

  .animate-up { animation: fadeUp 0.6s ease-out forwards; }
  .animate-in { animation: fadeIn 0.8s ease-out forwards; }
  .delay-1 { animation-delay: 0.1s; }
  .delay-2 { animation-delay: 0.2s; }

  /* Hero Banner Workspace */
  .hero {
    background: #0f0f0f;
    color: #fff;
    padding: 80px 40px 60px;
    text-align: center;
    border-radius: 24px;
    margin-top: 24px;
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
  .hero h1 span { color: #00c48c; }
  .hero p {
    font-size: 18px;
    color: #999;
    max-width: 600px;
    margin: 0 auto 40px;
    line-height: 1.6;
  }

  /* Core Structural Sections */
  .section { padding: 40px 0px; }
  .section-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 12px;
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
    background: #b8fce8;
    border-radius: 6px;
    padding: 0 8px;
  }
  .section-sub {
    font-size: 16px;
    color: #666;
    margin-bottom: 40px;
    max-width: 650px;
    line-height: 1.6;
  }

  /* Alternating Timeline Center Track Line */
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
    transition: background-color 0.4s, border-color 0.4s;
  }

  /* Roadmap Visual Component Cards */
  .plx-step-card {
    background: #fff;
    border: 1.5px solid #e4e4e4;
    border-radius: 16px;
    padding: 24px 28px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.01);
    transition: border-color .3s, box-shadow .3s, transform .3s;
  }
  .plx-step-card:hover {
    border-color: #00c48c;
    box-shadow: 0 8px 32px rgba(0,196,140,.12);
    transform: translateY(-2px);
  }
  .plx-step-tag {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .07em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 100px;
    margin-bottom: 12px;
  }
  .plx-step-title {
    font-size: 18px;
    font-weight: 700;
    color: #0a0a0a;
    margin-bottom: 8px;
    letter-spacing: -.3px;
  }
  .plx-step-desc {
    font-size: 14px;
    color: #666;
    line-height: 1.6;
  }
  .plx-step-detail {
    margin-top: 14px;
    font-size: 13px;
    color: #888;
    line-height: 1.5;
  }
  .plx-step-detail strong {
    color: #0a0a0a;
    font-weight: 600;
  }

  .plx-notif {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    background: #f7f7f5;
    border: 1.5px solid #e4e4e4;
    border-radius: 10px;
    padding: 10px 12px;
    margin-top: 14px;
  }
  .plx-notif-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #00c48c;
    margin-top: 4px;
    flex-shrink: 0;
  }
  .plx-notif-text {
    font-size: 12px;
    color: #555;
    line-height: 1.4;
  }
  .plx-notif-text strong { color: #000; }

  /* Highlight Premium Milestone Step 6 Callout Card */
  .plx-money-card {
    background: #0a0a0a;
    border: 1.5px solid #00c48c;
    position: relative;
    overflow: hidden;
  }
  .plx-money-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at top left, rgba(0,196,140,.2) 0%, transparent 60%);
  }
  .plx-money-card .plx-step-title { color: #fff; }
  .plx-money-card .plx-step-desc { color: #888; }
  .plx-money-card .plx-step-detail { color: #666; }
  .plx-money-card .plx-step-detail strong { color: #00c48c; }
  .plx-money-amount {
    font-size: 36px;
    font-weight: 700;
    color: #00c48c;
    letter-spacing: -1px;
    margin-top: 12px;
    display: block;
  }
  .plx-money-sub { font-size: 12px; color: #555; margin-top: 2px; }

  /* Dashboard Core Metric Blocks */
  .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px; }
  .metric-card {
    flex: 1;
    min-width: 140px;
    background: #fff;
    border: 1px solid #e8e6e0;
    border-radius: 12px;
    padding: 20px;
    transition: transform 0.2s ease;
  }
  .metric-card:hover { transform: translateY(-3px); }
  .metric-card .m-label { font-size: 12px; color: #888; margin-bottom: 6px; }
  .metric-card .m-value { font-size: 28px; font-weight: 700; color: #0f0f0f; }
  .metric-card .m-sub { font-size: 12px; color: #aaa; margin-top: 4px; }
  .metric-card.highlight { 
    background: #0f0f0f; 
    border-color: #0f0f0f; 
    animation: pulseHighlight 2s infinite; 
  }
  .metric-card.highlight .m-label { color: #888; }
  .metric-card.highlight .m-value { color: #00c48c; }
  .metric-card.highlight .m-sub { color: #666; }

  /* Comparative Analytics Grid */
  .compare-table { background: #fff; border: 1px solid #e8e6e0; border-radius: 16px; overflow: hidden; }
  .compare-header {
    display: grid;
    grid-template-columns: 2fr 1fr;
    background: #0f0f0f;
    color: #fff;
    padding: 14px 24px;
    font-size: 13px;
    font-weight: 600;
  }
  .compare-row {
    display: grid;
    grid-template-columns: 2fr 1fr;
    padding: 14px 24px;
    border-bottom: 1px solid #f0eeea;
    font-size: 14px;
    align-items: center;
  }
  .compare-row:last-child { border-bottom: none; }
  .compare-row .label { color: #555; }
  .compare-row .bad { color: #e24b4a; font-weight: 500; }
  .compare-row .good { color: #16a34a; font-weight: 500; }

  .insight-card {
    background: #fff;
    border: 1px solid #e8e6e0;
    border-left: 3px solid #00c48c;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin-bottom: 12px;
    font-size: 14px;
    color: #444;
    line-height: 1.6;
  }
  .insight-card b { color: #0f0f0f; font-weight: 600; }

  .cta-section {
    background: #0f0f0f;
    color: #fff;
    padding: 80px 60px;
    text-align: center;
    border-radius: 24px;
    margin-bottom: 40px;
  }
  .cta-section h2 { font-size: 40px; font-weight: 700; margin-bottom: 16px; letter-spacing: -.5px; }
  .cta-section p { font-size: 18px; color: #888; margin-bottom: 40px; }

  .divider { height: 1px; background: #e8e6e0; margin: 40px 0px; }

  /* RESPONSIVE MOBILE COMPRESSION ADJUSTMENTS */
  @media (max-width: 768px) {
    .timeline-container::after { left: 20px; }
    .timeline-block { justify-content: flex-start !important; }
    .timeline-pointer { width: 100% !important; padding-left: 50px !important; padding-right: 0 !important; }
    .timeline-icon { left: 20px !important; margin-left: -20px !important; }
  }

  /* Framework Cleanup Elements */
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── 2. HERO SECTION ───────────────────────────────────────────────────────────
st.markdown("""
<div class="hero animate-in">
  <div class="hero-badge animate-up delay-1">⚡ platinux.net - Freelancer Lead Engine</div>
  <h1 class="animate-up delay-1">Stop chasing low-ballers.<br>Get high-ticket <span>direct leads.</span></h1>
  <p class="animate-up delay-2">Platinux tracks founders and small businesses actively looking for software developers, web designers, and SaaS builders across platforms. Send your pitch before anyone else.</p>
</div>
""", unsafe_allow_html=True)


# ── 3. SIX-STEP ROADMAP SECTION ───────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="section-label">🗺 Your Blueprint</div>
<div class="section-title">From lead alert to payout.</div>
<div class="section-sub">See how simple individual lead tracking is. Respond first, stand out, and secure 100% of the project value.</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-container">

  <div class="timeline-block">
    <div class="timeline-icon">1</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#f0fff8; color:#00875a;">🔍 Step 1</div>
        <div class="plx-step-title">Client asks for a dev online</div>
        <div class="plx-step-desc">A real client posts on tech subreddits or developer networks stating they need a custom platform built.</div>
        <div class="plx-notif">
          <div class="plx-notif-dot"></div>
          <div class="plx-notif-text"><strong>r/Freelance:</strong> "Looking for full-stack developer to finish an MVP. Budget $2,500."</div>
        </div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">2</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#fff8e6; color:#b45309;">⚡ Step 2</div>
        <div class="plx-step-title">Instant AI verification</div>
        <div class="plx-step-desc">Our bots catch the thread in under a minute, filters out agency noise, and confirms it's a direct client.</div>
        <div class="plx-step-detail">No scraping delay · verified status checks</div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">3</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#f0f9ff; color:#0369a1;">🔔 Step 3</div>
        <div class="plx-step-title">Direct ping to you</div>
        <div class="plx-step-desc">You get a clean notification with a direct link to hop onto the project source immediately.</div>
        <div class="plx-notif">
          <div class="plx-notif-dot"></div>
          <div class="plx-notif-text"><strong>🔔 Platinux Feed:</strong> MVP Build · Budget $2.5k · Posted 1 min ago → <strong style="color:#00c48c">Open Thread</strong></div>
        </div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">4</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#fdf0ff; color:#7e22ce;">💬 Step 4</div>
        <div class="plx-step-title">Drop your personalized pitch</div>
        <div class="plx-step-desc">You contact them directly before hundreds of automated applications flood their job posts on traditional boards.</div>
        <div class="plx-step-detail">First responders get <strong>80% higher engagement rates</strong>.</div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">5</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#fff1f0; color:#b91c1c;">🤝 Step 5</div>
        <div class="plx-step-title">Lock down contract details</div>
        <div class="plx-step-desc">Talk details via DM/Email, negotiate terms, and sign contracts without giving up any platform fees.</div>
        <div class="plx-step-detail">Keep 100% of your earnings. No platform cut.</div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon" style="border-color:#00c48c; background:#0f0f0f; color:#fff;">6</div>
    <div class="timeline-pointer">
      <div class="plx-step-card plx-money-card">
        <div class="plx-step-tag" style="background:rgba(0,196,140,.15); color:#00c48c;">💰 Step 6</div>
        <div class="plx-step-title">Full payment directly to you</div>
        <div class="plx-step-desc">Deliver the project and bank the clean profit. No Upwork/Fiverr commissions draining your balance.</div>
        <span class="plx-money-amount">+$2,500</span>
        <div class="plx-money-sub">100% net earnings went directly to your bank account</div>
        <div class="plx-step-detail" style="margin-top:16px">Platinux cost: <strong>$79/mo</strong>&nbsp;&nbsp;·&nbsp;&nbsp;ROI: <strong>31×</strong></div>
      </div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 4. INDEPENDENT FREELANCER ECONOMICS CALC ─────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Freelancer Economics</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Run your individual numbers</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">See how much net income you retain by shifting away from traditional platforms.</div>', unsafe_allow_html=True)

calc_col_left, calc_col_right = st.columns([1, 1], gap="large")

with calc_col_left:
    st.markdown("**Your Settings**")

    currency = st.selectbox("Currency Setup", ["USD ($)", "INR (₹)"], key="currency")
    is_inr = currency == "INR (₹)"
    sym = "₹" if is_inr else "$"
    
    plan_cost = 6999 if is_inr else 79

    if is_inr:
        avg_project = st.slider("Average deal size (₹)", 10000, 500000, 120000, step=10000)
    else:
        avg_project = st.slider("Average deal size ($)", 500, 15000, 3500, step=500)

    leads_per_month = st.slider("Leads pitched per month", 10, 150, 40, step=5)
    conversion_rate = st.slider("Close rate (%)", 1, 20, 5, step=1)

with calc_col_right:
    st.markdown("**Your Income Projections**")

    # Freelancer business logic calculations
    deals_closed = leads_per_month * (conversion_rate / 100)
    monthly_income = deals_closed * avg_project
    net_gain = monthly_income - plan_cost
    
    roi_x = round((monthly_income / plan_cost) * 100) if plan_cost > 0 else 0
    annual_profit = net_gain * 12

    def fmt(n):
        if is_inr:
            if n >= 100000: return f"₹{n/100000:.1f}L"
            return f"₹{int(round(n)):,}"
        else:
            if n >= 1000: return f"${n/1000:.1f}k"
            return f"${int(round(n)):,}"

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card highlight">
        <div class="m-label">Subscription ROI</div>
        <div class="m-value">{roi_x:,}%</div>
        <div class="m-sub">return on {sym}{plan_cost}/mo plan</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Monthly Retained Income</div>
        <div class="m-value">{fmt(monthly_income)}</div>
        <div class="m-sub">{deals_closed:.1f} jobs finished</div>
      </div>
    </div>
    <div class="metric-row">
      <div class="metric-card">
        <div class="m-label">Net Monthly Profit</div>
        <div class="m-value">{fmt(net_gain)}</div>
        <div class="m-sub">After subscription deductions</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Annual Extra Revenue</div>
        <div class="m-value">{fmt(annual_profit)}</div>
        <div class="m-sub">Yearly individual runway</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    payback_needed = round(plan_cost / avg_project, 2) if avg_project > 0 else 0
    payback_str = "< 1" if payback_needed < 1 else f"{int(round(payback_needed))}"

    st.markdown(f"""
    <div class="insight-card">
      <b>Break-even Status:</b> You need just <b>{payback_str} client contract</b> to clear the costs of your subscription completely.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 5. GRAPH VISUALIZATIONS SECTION ───────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Performance Breakdown</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Your 12-Month Profit Roadmap</div>', unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns([3, 2], gap="large")

with chart_col1:
    months = list(range(1, 13))
    # Core freelancer path chart arrays
    platinux_monthly = [max((monthly_income * (1 + 0.04*i)) - plan_cost, 0) for i in range(12)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in platinux_monthly],
        mode='lines+markers',
        name='Net Income via Platinux',
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
        xaxis=dict(title='Month Timeline', showgrid=False, tickvals=months, ticktext=[f'M{m}' for m in months]),
        yaxis=dict(title=f'Net Balance ({sym})', showgrid=True, gridcolor='#f0eeea', tickformat=','),
        height=300
    )
    st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    labels = ['Take-home Pay', 'Subscription Costs']
    pie_income = max(monthly_income - plan_cost, 0)
    values = [pie_income, plan_cost]
    colors = ['#00c48c', '#0f0f0f']

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
        paper_bgcolor='#ffffff', showlegend=True,
        margin=dict(l=0, r=0, t=10, b=0), height=300
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 6. COMPARATIVE VALUE MATRIX ───────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Strategy Evaluation</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Direct Inbound Channels vs Platforms</div>', unsafe_allow_html=True)

st.markdown("""
<div class="compare-table">
  <div class="compare-header">
    <span>Feature Check</span>
    <span>Traditional Freelance Boards</span>
  </div>
  <div class="compare-row">
    <span class="label">Platform Commissions</span>
    <span class="bad">Takes 10% to 20% slice out of your billings</span>
  </div>
  <div class="compare-row">
    <span class="label">Bidding System</span>
    <span class="bad">Forced price-drops against automated global applications</span>
  </div>
  <div class="compare-row">
    <span class="label">Client Retention</span>
    <span class="bad">Strict rules block off-platform direct communications</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 7. SOLO PRICING WORKSPACE ─────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Plans & Billing</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Simple flat fee. Cancel anytime.</div>', unsafe_allow_html=True)

col_p1, col_p2 = st.columns([1, 2], gap="medium")

with col_p1:
    st.markdown(f"""
    <div class="metric-card highlight" style="height:100%;">
      <div style="font-size:11px;color:#00c48c;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">Pro Freelancer</div>
      <div style="font-size:36px;font-weight:700;color:#fff;margin-bottom:4px">{sym}{plan_cost}</div>
      <div style="font-size:13px;color:#666;margin-bottom:20px">/ month</div>
      <div style="font-size:13px;color:#ccc;line-height:2">
        ✓ 100% Real-time lead engine access<br>
        ✓ Instant text alert system<br>
        ✓ Clean verified job alerts feed<br>
        ✓ Zero platform commission cuts<br>
        ✓ Full commercial link redirection
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.markdown("""
    <div style="padding: 20px 0px;">
      <h4 style="margin-bottom:12px; color:#0f0f0f;">Why a fixed monthly sub beats regular bidding:</h4>
      <p style="font-size:14px; color:#666; line-height:1.6;">
        Traditional freelance boards treat you like a line-item. They charge you money to buy tokens just to submit proposals, and then take up to 20% of your hard-earned invoice amount when you deliver. 
        <br><br>
        Platinux changes this balance. For one simple monthly investment, you get access to the actual target threads before everyone else, establishing a secure direct-to-client pipeline.
      </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 8. CONVERSION MARKETING CALLOUT ───────────────────────────────────────────
st.markdown(f"""
<div class="cta-section">
  <h2>Secure your independent workflow pipelines.</h2>
  <p>Start tracking authentic high-intent client interactions without platform restrictions.</p>
  <div style="font-size:14px;color:#666;margin-top:32px">
    platinux.net · Risk Free Subscription Trial Available
  </div>
</div>
""", unsafe_allow_html=True)
