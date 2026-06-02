import streamlit as st
import plotly.graph_objects as go

# ── 1. GLOBAL PAGE CONFIGURATION & MARGIN CONTROL ─────────────────────────────
st.set_page_config(
    page_title="Platinux Agency - ROI Calculator",
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
  
  @supports (animation-timeline: view()) {
    .timeline-block {
      animation: fadeUp both;
      animation-timeline: view();
      animation-range: entry 5% cover 30%;
    }
    .timeline-block:hover .timeline-icon {
      border-color: #00c48c;
      background: #f0fff8;
      box-shadow: 0 0 0 6px rgba(0,196,140,.12);
    }
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


# ── 2. LANDING PAGE SECTION 1: HERO VIEWWORKSPACE ─────────────────────────────
st.markdown("""
<div class="hero animate-in">
  <div class="hero-badge animate-up delay-1">⚡ platinux.net/agency - ROI Calculator</div>
  <h1 class="animate-up delay-1">Stop scaling your sales team.<br>Scale your <span>lead flow.</span></h1>
  <p class="animate-up delay-2">Platinux tracks founders and enterprises actively requesting custom development, SaaS builds, and design overhauls. Reach high-ticket clients before they post on Upwork.</p>
</div>
""", unsafe_allow_html=True)


# ── 3. LANDING PAGE SECTION 2: THE SUCCESS ROADMAP (INTEGRATED) ──────────────
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="section-label">🗺 Your path to clients</div>
<div class="section-title">From <em>zero</em> to paid. In 6 steps.</div>
<div class="section-sub">Here's exactly how Platinux turns a business owner's post into money in your account — and why responding first is everything.</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-container">

  <div class="timeline-block">
    <div class="timeline-icon">1</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#f0fff8; color:#00875a;">🔍 Step 1</div>
        <div class="plx-step-title">Business owner posts online</div>
        <div class="plx-step-desc">Somewhere on Reddit, Facebook, LinkedIn or Threads, a real business owner types "looking for a web developer." It goes live publicly.</div>
        <div class="plx-notif">
          <div class="plx-notif-dot"></div>
          <div class="plx-notif-text"><strong>r/entrepreneur:</strong> "Need someone to build a site for my salon — budget $800, want it done this month."</div>
        </div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">2</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#fff8e6; color:#b45309;">⚡ Step 2</div>
        <div class="plx-step-title">Platinux detects it instantly</div>
        <div class="plx-step-desc">Our engine scans 7+ platforms 24/7. The second the post goes live, we capture it, verify it's a real business owner (not spam), and score its intent.</div>
        <div class="plx-step-detail"><strong>Avg detection time:</strong> under 60 seconds</div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">3</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#f0f9ff; color:#0369a1;">🔔 Step 3</div>
        <div class="plx-step-title">You get a real-time alert</div>
        <div class="plx-step-desc">Platinux sends you a direct link to the post the moment it's verified. You see the platform, the post, the budget signal — everything you need to respond.</div>
        <div class="plx-notif">
          <div class="plx-notif-dot"></div>
          <div class="plx-notif-text"><strong>🔔 New Project Alert</strong> — Salon owner · Reddit · Budget ~$800 · Posted 2 min ago → <strong style="color:#00c48c">View post</strong></div>
        </div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">4</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#fdf0ff; color:#7e22ce;">💬 Step 4</div>
        <div class="plx-step-title">You reply first</div>
        <div class="plx-step-desc">You go directly to the post and respond — as a comment, a DM, or a reply. The business owner gets your message before they've even seen 10 other pitches.</div>
        <div class="plx-step-detail">Freelancers who respond within 1 hour close at <strong>3× the rate</strong> of those who respond later.</div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon">5</div>
    <div class="timeline-pointer">
      <div class="plx-step-card">
        <div class="plx-step-tag" style="background:#fff1f0; color:#b91c1c;">🤝 Step 5</div>
        <div class="plx-step-title">Discovery call, scope, close</div>
        <div class="plx-step-desc">You have a conversation with a business owner who already said they need a developer. No cold pitching — they raised their hand first. Agree on scope, timeline, and price.</div>
        <div class="plx-step-detail">No platform middleman. No bidding wars.<br><strong>You own the client relationship directly.</strong></div>
      </div>
    </div>
  </div>

  <div class="timeline-block">
    <div class="timeline-icon" style="border-color:#00c48c; background:#0f0f0f; color:#fff;">6</div>
    <div class="timeline-pointer">
      <div class="plx-step-card plx-money-card">
        <div class="plx-step-tag" style="background:rgba(0,196,140,.15); color:#00c48c;">💰 Step 6</div>
        <div class="plx-step-title">Project delivered. Money in.</div>
        <div class="plx-step-desc">You build, deliver, and get paid. No Upwork commissions eating 20% of your income. No platform owning your client. Just you, the client, and the full project value.</div>
        <span class="plx-money-amount">+$2,400</span>
        <div class="plx-money-sub">avg first project from a Platinux lead · directly to you</div>
        <div class="plx-step-detail" style="margin-top:16px">Platinux cost: <strong>$79/mo</strong>&nbsp;&nbsp;·&nbsp;&nbsp;Your ROI: <strong>30×</strong></div>
      </div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 4. ECONOMICS & USER DATA MATRIX INTERFACE ─────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Agency Economics</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Calculate your true net profit</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Model your agency overhead and see what a single subscription yields.</div>', unsafe_allow_html=True)

calc_col_left, calc_col_right = st.columns([1, 1], gap="large")

with calc_col_left:
    st.markdown("**Your Agency Profile**")

    currency = st.selectbox("Your currency", ["USD ($)", "INR (₹)"], key="currency")
    is_inr = currency == "INR (₹)"
    sym = "₹" if is_inr else "$"
    
    plan_cost = 17999 if is_inr else 199

    if is_inr:
        avg_project = st.slider("Average project size (₹)", 50000, 2000000, 400000, step=50000)
        sdr_cost = st.slider("Current Outbound/Ad spend per month (₹)", 40000, 800000, 150000, step=20000)
    else:
        avg_project = st.slider("Average deal size ($)", 2000, 50000, 8000, step=1000)
        sdr_cost = st.slider("Current Outbound/Ad spend per month", 500, 10000, 2000, step=500)

    leads_per_month = st.slider("Leads worked per month", 20, 300, 100, step=10)
    conversion_rate = st.slider("Close rate (%)", 1, 20, 3, step=1)
    agency_margin = st.slider("Net Profit Margin (%)", 10, 80, 40, step=5)

with calc_col_right:
    st.markdown("**Your Agency Results**")

    # Math processing engines
    clients_per_month = leads_per_month * (conversion_rate / 100)
    monthly_revenue = clients_per_month * avg_project
    monthly_overhead = monthly_revenue * (1 - (agency_margin / 100))
    monthly_profit = monthly_revenue - monthly_overhead
    net_gain = monthly_profit - plan_cost
    
    # Division protection guard
    roi_x = round((monthly_profit / plan_cost) * 100) if plan_cost > 0 else 0
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
        <div class="m-label">Agency ROI</div>
        <div class="m-value">{roi_x:,}%</div>
        <div class="m-sub">return on {sym}{plan_cost:,}/mo</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Gross Revenue / Mo</div>
        <div class="m-value">{fmt(monthly_revenue)}</div>
        <div class="m-sub">{clients_per_month:.1f} deals closed</div>
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

    # Protection to safeguard against layout collapse
    denom = (avg_project * (agency_margin / 100))
    payback_clients = round(plan_cost / denom, 2) if denom > 0 else 0
    payback_str = "< 1" if payback_clients < 1 else f"{int(round(payback_clients))}"

    st.markdown(f"""
    <div class="insight-card">
      <b>Minimal Risk.</b> You only need to close <b>{payback_str} deals</b> to completely cover your monthly Agency subscription from your <i>net profit</i> margin.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 5. GRAPH VISUALIZATIONS SECTION ───────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">12-Month Projection</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Scaling Profit, Not Headcount</div>', unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns([3, 2], gap="large")

with chart_col1:
    months = list(range(1, 13))
    # Safe boundary loops to keep scales precise
    sdr_monthly = [max((monthly_profit * (1 + 0.02*i)) - sdr_cost, 0) for i in range(12)]
    platinux_monthly = [max((monthly_profit * (1 + 0.05*i)) - plan_cost, 0) for i in range(12)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in sdr_monthly],
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
    pie_net_profit = max(monthly_profit - plan_cost, 0)
    values = [pie_net_profit, max(monthly_overhead, 0), plan_cost]
    colors = ['#00c48c', '#e8e6e0', '#0f0f0f']

    fig2 = go.Figure(go.Pie(
        labels=labels,
        values=values,
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
            text=f"{fmt(pie_net_profit)}<br><span style='font-size:11px'>true profit</span>",
            x=0.5, y=0.5, font_size=14, showarrow=False
        )]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 6. DATA ACQUISITION METRIC MATRIX ─────────────────────────────────────────
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


# ── 7. PRICING PLANS WORKSPACE ────────────────────────────────────────────────
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


# ── 8. BOTTOM MARKETING CONVERSION CTA ────────────────────────────────────────
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
