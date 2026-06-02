import streamlit as st
import plotly.graph_objects as go

# ── 1. GLOBAL CONFIGURATION & CUSTOM DESIGN ARCHITECTURE ─────────────────────
st.set_page_config(
    page_title="Platinux - High-Intent Customer Discovery Engine",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Enterprise-grade B2B Stylesheet
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

  html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif; 
  }
  h1, h2, h3, h4, .section-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
  }
  .main { background: #fcfbf9; }
  
  /* Container Padding Configuration */
  .block-container { 
    padding-left: 6% !important; 
    padding-right: 6% !important; 
    max-width: 92% !important; 
  }

  /* Structural Components Grid & Utility classes */
  .hero-container {
    background: #09090b;
    color: #ffffff;
    padding: 90px 50px 70px;
    text-align: center;
    border-radius: 28px;
    margin-top: 20px;
    border: 1px solid #1e1e24;
    position: relative;
    overflow: hidden;
  }
  .hero-container::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 100%;
    background: radial-gradient(circle at top center, rgba(0, 196, 140, 0.12) 0%, transparent 65%);
    pointer-events: none;
  }
  .hero-tag {
    display: inline-block;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 100px;
    padding: 6px 18px;
    font-size: 13px;
    font-weight: 500;
    color: #00c48c;
    margin-bottom: 24px;
    letter-spacing: 0.05em;
  }
  .hero-container h1 {
    font-size: 56px;
    font-weight: 700;
    line-height: 1.15;
    margin: 0 0 20px;
    letter-spacing: -1.5px;
  }
  .hero-container h1 span { color: #00c48c; }
  .hero-container p {
    font-size: 19px;
    color: #a1a1aa;
    max-width: 700px;
    margin: 0 auto 30px;
    line-height: 1.6;
  }

  .section { padding: 50px 0px; }
  .section-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #71717a;
    margin-bottom: 12px;
  }
  .section-title {
    font-size: 40px;
    font-weight: 700;
    color: #09090b;
    margin-bottom: 14px;
    letter-spacing: -.8px;
  }
  .section-sub {
    font-size: 16px;
    color: #52525b;
    margin-bottom: 45px;
    max-width: 700px;
    line-height: 1.6;
  }

  /* ── FUNNELING DIAGRAM COMPONENTS ── */
  .fn-wrapper {
    background: #ffffff;
    border: 1px solid #e4e4e7;
    border-radius: 20px;
    padding: 35px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.02);
    margin: 20px 0 40px;
  }
  .fn-grid {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
  }
  .fn-stage {
    background: #f4f4f5;
    border: 1px solid #e4e4e7;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    flex: 1;
    position: relative;
  }
  .fn-stage.dark {
    background: #09090b;
    border-color: #1e1e24;
    color: #fff;
  }
  .fn-stage.active {
    background: #f0fdf4;
    border-color: #bbf7d0;
  }
  .fn-title { font-size: 14px; font-weight: 700; color: #09090b; margin-bottom: 8px; }
  .fn-stage.dark .fn-title { color: #ffffff; }
  .fn-stage.active .fn-title { color: #16a34a; }
  .fn-desc { font-size: 12px; color: #71717a; line-height: 1.4; }
  .fn-stage.dark .fn-desc { color: #a1a1aa; }
  
  .fn-arrow {
    font-size: 24px;
    color: #a1a1aa;
    font-weight: bold;
    user-select: none;
  }
  .fn-badge-row {
    display: flex; gap: 6px; justify-content: center; flex-wrap: wrap; margin-top: 10px;
  }
  .fn-badge {
    font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 4px; background: #e4e4e7; color: #3f3f46;
  }

  /* ── ROADMAP SYSTEM TRACKS ── */
  .track-container { position: relative; max-width: 1200px; margin: 40px auto; }
  .track-container::before {
    content: ''; position: absolute; width: 2px; background: #e4e4e7;
    top: 0; bottom: 0; left: 40px; z-index: 1;
  }
  .track-node {
    position: relative; display: flex; gap: 30px; margin-bottom: 35px; z-index: 2;
  }
  .track-icon-marker {
    width: 82px; height: 42px; border-radius: 100px; background: #ffffff;
    border: 2px solid #e4e4e7; display: flex; align-items: center; justify-content: center;
    font-size: 12px; font-weight: 700; color: #09090b; flex-shrink: 0; z-index: 5;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  }
  .track-node.premium .track-icon-marker {
    border-color: #00c48c; background: #09090b; color: #ffffff;
  }
  .track-content-panel {
    background: #ffffff; border: 1px solid #e4e4e7; border-radius: 16px;
    padding: 24px 30px; flex-grow: 1; box-shadow: 0 4px 12px rgba(0,0,0,0.01);
    transition: all 0.3s ease;
  }
  .track-node:hover .track-content-panel {
    border-color: #00c48c; transform: translateX(3px);
  }
  .track-node.premium .track-content-panel {
    background: #09090b; border-color: #00c48c; color: #ffffff;
  }
  .track-header-row {
    display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;
  }
  .track-label-tag {
    font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: .05em;
    color: #71717a; background: #f4f4f5; padding: 3px 10px; border-radius: 6px;
  }
  .track-node.premium .track-label-tag {
    background: rgba(0, 196, 140, 0.15); color: #00c48c;
  }
  .track-telemetry { font-size: 12px; color: #16a34a; font-family: monospace; font-weight: 600; }
  
  .track-headline { font-size: 20px; font-weight: 700; color: #09090b; margin-bottom: 6px; }
  .track-node.premium .track-headline { color: #ffffff; }
  .track-body-text { font-size: 14px; color: #52525b; line-height: 1.5; }
  .track-node.premium .track-body-text { color: #a1a1aa; }

  /* Code Blocks Inside Tracks */
  .track-code-terminal {
    background: #18181b; border: 1px solid #27272a; border-radius: 10px;
    padding: 14px; font-family: monospace; font-size: 13px; margin-top: 15px; color: #f4f4f5;
  }
  .terminal-line { display: flex; gap: 10px; margin-bottom: 4px; }
  .terminal-line.drop { color: #ef4444; }
  .terminal-line.pass { color: #22c55e; }

  /* ── METRIC DASHBOARD BLOCKS ── */
  .metrics-grid-row { display: flex; gap: 18px; flex-wrap: wrap; margin-bottom: 25px; }
  .b2b-metric-box {
    flex: 1; min-width: 180px; background: #ffffff; border: 1px solid #e4e4e7;
    border-radius: 14px; padding: 22px; transition: transform 0.2s ease;
  }
  .b2b-metric-box:hover { transform: translateY(-2px); }
  .b2b-metric-box .box-lbl { font-size: 12px; color: #71717a; text-transform: uppercase; letter-spacing: .02em; margin-bottom: 6px; }
  .b2b-metric-box .box-val { font-size: 32px; font-weight: 700; color: #09090b; }
  .b2b-metric-box.active-green { background: #09090b; border-color: #00c48c; }
  .b2b-metric-box.active-green .box-lbl { color: #a1a1aa; }
  .b2b-metric-box.active-green .box-val { color: #00c48c; }
  .b2b-metric-box .box-sub { font-size: 12px; color: #a1a1aa; margin-top: 4px; }
  .b2b-metric-box.active-green .box-sub { color: #52525b; }

  .matrix-card {
    background: #ffffff; border: 1px solid #e4e4e7; border-left: 4px solid #00c48c;
    border-radius: 0 14px 14px 0; padding: 18px 24px; margin-bottom: 15px;
    font-size: 14px; color: #3f3f46; line-height: 1.6;
  }

  /* ── STRATEGY EVALUATION TABLE ── */
  .table-box { background: #ffffff; border: 1px solid #e4e4e7; border-radius: 16px; overflow: hidden; margin-top: 20px; }
  .table-hdr {
    display: grid; grid-template-columns: 2fr 2fr 2fr; background: #09090b; color: #ffffff;
    padding: 16px 24px; font-size: 13px; font-weight: 600; letter-spacing: .02em;
  }
  .table-row-item {
    display: grid; grid-template-columns: 2fr 2fr 2fr; padding: 16px 24px;
    border-bottom: 1px solid #f4f4f5; font-size: 14px; align-items: center;
  }
  .table-row-item:last-child { border-bottom: none; }
  .table-row-item .lbl-feat { color: #09090b; font-weight: 600; }
  .table-row-item .status-negative { color: #dc2626; font-weight: 500; }
  .table-row-item .status-positive { color: #16a34a; font-weight: 600; }

  .cta-block {
    background: #09090b; color: #ffffff; padding: 80px 40px; text-align: center;
    border-radius: 28px; margin: 40px 0; border: 1px solid #1e1e24;
  }
  .cta-block h2 { font-size: 42px; font-weight: 700; margin-bottom: 14px; letter-spacing: -1px; }
  .cta-block p { font-size: 18px; color: #a1a1aa; margin-bottom: 35px; max-width: 600px; margin-left: auto; margin-right: auto; }

  .divider-line { height: 1px; background: #e4e4e7; margin: 50px 0px; }

  /* Responsive Fixes */
  @media (max-width: 768px) {
    .fn-grid { flex-direction: column; }
    .fn-arrow { transform: rotate(90deg); margin: 5px 0; }
    .track-container::before { left: 20px; }
    .track-icon-marker { width: 50px; height: 36px; font-size: 11px; }
    .track-node { gap: 15px; }
    .table-hdr, .table-row-item { grid-template-columns: 1fr; gap: 10px; }
  }

  /* Core UI Cleanups */
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── 2. HERO SECTION ───────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-container animate-in">
  <div class="hero-tag">⚡ PLATINUX FOR ENTERPRISE & BRANDS</div>
  <h1>Turn Public Social Conversations into <br><span>Filtered, High-Intent Sales Pipelines</span></h1>
  <p>Stop paying for passive keyword monitoring that dumps thousands of noisy mentions on your plate. Platinux scrapes the internet, isolates active buyers explicitly seeking your product categories, and routes clean data straight to your desk.</p>
</div>
""", unsafe_allow_html=True)


# ── 3. DATA FUNNELING DIAGRAM SECTION ─────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">The Data Funnel</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">The High-Intent Ingestion Pipeline</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Here is how our infrastructure extracts active purchasers directly from raw social data streams.</div>', unsafe_allow_html=True)

st.markdown("""
<div class="fn-wrapper">
  <div class="fn-grid">
    <!-- Stage 1 -->
    <div class="fn-stage">
      <div class="fn-title">1. Raw Social Web Ingestion</div>
      <div class="fn-desc">Continuous multi-node scraping monitoring text strings across social platforms.</div>
      <div class="fn-badge-row">
        <span class="fn-badge">Reddit API/Streams</span>
        <span class="fn-badge">X Firehose</span>
        <span class="fn-badge">BlueSky</span>
      </div>
    </div>
    
    <div class="fn-arrow">➔</div>
    
    <!-- Stage 2 -->
    <div class="fn-stage dark">
      <div class="fn-title" style="color:#00c48c;">2. LLM Intent Parser</div>
      <div class="fn-desc" style="color:#a1a1aa;">Proprietary semantic filters scrub the data, deleting casual chitchat, news updates, and generic terms.</div>
      <div class="fn-badge-row">
        <span class="fn-badge" style="background:#27272a; color:#f4f4f5;">Context Filters</span>
        <span class="fn-badge" style="background:#27272a; color:#f4f4f5;">De-Noising Layer</span>
      </div>
    </div>
    
    <div class="fn-arrow">➔</div>
    
    <!-- Stage 3 -->
    <div class="fn-stage active">
      <div class="fn-title">3. Actionable Qualified Lead</div>
      <div class="fn-desc">Verified buyer profiles, intent metrics, and source URLs mapped out with complete transparency.</div>
      <div class="fn-badge-row">
        <span class="fn-badge" style="background:#bbf7d0; color:#16a34a;">100% Retained</span>
        <span class="fn-badge" style="background:#bbf7d0; color:#16a34a;">Zero Noise</span>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── 4. 5-TRACK OPERATIONAL ROADMAP ────────────────────────────────────────────
st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Operational Architecture</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">How we identify and deliver your market</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">A transparent breakdown of how our infrastructure monitors, filters, qualifies, and bridges leads directly into your workspace pipelines.</div>', unsafe_allow_html=True)

st.markdown("""
<div class="track-container">

  <!-- Track 1 -->
  <div class="track-node">
    <div class="track-icon-marker">TRACK 01</div>
    <div class="track-content-panel">
      <div class="track-header-row">
        <span class="track-label-tag">Data Acquisition</span>
        <span class="track-telemetry">Telemetry: Ingesting ~4,200 posts/min</span>
      </div>
      <div class="track-headline">Global Social Scraping Engine</div>
      <div class="track-body-text">Our globally distributed nodes run continuous extraction jobs across developer forums, tech subreddits, consumer communities, and conversational public nodes. We monitor active textual sequences without reliance on delayed standard web indexes.</div>
    </div>
  </div>

  <!-- Track 2 -->
  <div class="track-node">
    <div class="track-icon-marker">TRACK 02</div>
    <div class="track-content-panel">
      <div class="track-header-row">
        <span class="track-label-tag">Algorithmic Processing</span>
        <span class="track-telemetry" style="color:#2563eb;">NLP Parsing Status: Active</span>
      </div>
      <div class="track-headline">AI Intent Filtering & De-noising</div>
      <div class="track-body-text">Standard tools alert you every time your keyword is mentioned, creating massive administrative debt. Platinux passes every sentence through structural context models to measure explicit purchase timelines and immediate requirements.</div>
      
      <div class="track-code-terminal">
        <div class="terminal-line drop"><span>[-] Mentions:</span> "I am reading a case study about enterprise CRMs." ➔ <strong>[Dropped: Zero Buying Action]</strong></div>
        <div class="terminal-line pass"><span>[+] Mentions:</span> "Outgrowing our current HubSpot setup for 45 reps. Need a system supporting custom lifecycle stages by next month. Recommendations?" ➔ <strong>[Passed: High-Intent Intent Detected]</strong></div>
      </div>
    </div>
  </div>

  <!-- Track 3 -->
  <div class="track-node">
    <div class="track-icon-marker">TRACK 03</div>
    <div class="track-content-panel">
      <div class="track-header-row">
        <span class="track-label-tag">Segmentation Layer</span>
        <span class="track-telemetry">Matching Engine: Sync Clear</span>
      </div>
      <div class="track-headline">Brand Matrix Matching</div>
      <div class="track-body-text">Filtered high-intent threads are instantly cataloged against your brand matrix variables: targeted industry verticals, product capabilities, serving geo-locations, and baseline budget capacities to ensure sales qualification.</div>
    </div>
  </div>

  <!-- Track 4 -->
  <div class="track-node">
    <div class="track-icon-marker">TRACK 04</div>
    <div class="track-content-panel">
      <div class="track-header-row">
        <span class="track-label-tag">Infrastructure Delivery</span>
        <span class="track-telemetry" style="color:#ea580c;">Delivery Lag: &lt; 14 Seconds</span>
      </div>
      <div class="track-headline">Instant Pipeline Syncing</div>
      <div class="track-body-text">Say goodbye to complex analytics portals that require hours of browsing. Platinux routes verified buyer data payloads—complete with exact text content, origin profiles, and direct URLs—straight to your systems via dedicated Slack channels, webhooks, or direct CRM feeds.</div>
    </div>
  </div>

  <!-- Track 5 -->
  <div class="track-style-connector"></div>

  <!-- Track 5 Premium Card -->
  <div class="track-node premium">
    <div class="track-icon-marker">TRACK 05</div>
    <div class="track-content-panel">
      <div class="track-header-row">
        <span class="track-label-tag">Conversion Action</span>
        <span class="track-telemetry" style="color:#00c48c;">Conversion Velocity: +320%</span>
      </div>
      <div class="track-headline">Frictionless Inbound Interception</div>
      <div class="track-body-text">Your sales development or growth marketing teams click the direct origin link and post an organic, contextual response directly inside the source discussion thread. By positioning your brand as a helpful expert exactly when the query is live, you intercept the prospect before they ever navigate to search engines or contact legacy options.</div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── 5. ENTERPRISE BRAND ROI CALCULATOR ────────────────────────────────────────
st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Financial Architecture</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Brand ROI & Yield Modeling</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Calculate how intercepting organic market intent drops your overall Customer Acquisition Costs (CAC) compared to hyper-inflated traditional ad network structures.</div>', unsafe_allow_html=True)

calc_l, calc_r = st.columns([1, 1], gap="large")

with calc_l:
    st.markdown("#### **Brand Settings**")
    
    currency_choice = st.selectbox("Operating Corporate Currency", ["USD ($)", "INR (₹)"], key="corp_currency")
    is_corp_inr = currency_choice == "INR (₹)"
    b_sym = "₹" if is_corp_inr else "$"
    
    # Dynamic setup bases on corporate scale
    base_saas_fee = 75000 if is_corp_inr else 850
    
    if is_corp_inr:
        val_ltv = st.slider("Customer Contract Value / LTV (₹)", 50000, 2000000, 450000, step=50000)
        estimated_avg_cpc = st.slider("Comparable Ad Channel CPC (₹)", 50, 800, 180, step=10)
    else:
        val_ltv = st.slider("Customer Contract Value / LTV ($)", 500, 50000, 6500, step=500)
        estimated_avg_cpc = st.slider("Comparable Ad Channel CPC ($)", 1.0, 25.0, 4.5, step=0.5)
        
    volume_leads = st.slider("Monthly Filtered High-Intent Leads Routed", 50, 1000, 300, step=50)
    team_close_rate = st.slider("Sales Conversion Close Rate (%)", 1, 15, 4, step=1)

with calc_r:
    st.markdown("#### **Performance Forecasts**")
    
    # Financial modeling math definitions
    total_conversions = volume_leads * (team_close_rate / 100)
    gross_new_revenue = total_conversions * val_ltv
    net_software_yield = gross_new_revenue - base_saas_fee
    
    # Ad channel equivalent value generation (assuming it takes ~15 clicks on a search network to hit comparable intent)
    comparable_ad_saved = volume_leads * 15 * estimated_avg_cpc
    brand_roi_pct = round((gross_new_revenue / base_saas_fee) * 100) if base_saas_fee > 0 else 0

    def format_brand_num(v):
        if is_corp_inr:
            if v >= 100000: return f"₹{v/100000:.2f}L"
            return f"₹{int(round(v)):,}"
        else:
            if v >= 1000: return f"${v/1000:.1f}k"
            return f"${int(round(v)):,}"

    st.markdown(f"""
    <div class="metrics-grid-row">
      <div class="b2b-metric-box active-green">
        <div class="box-lbl">Pipeline ROI Return</div>
        <div class="box-val">{brand_roi_pct:,}%</div>
        <div class="box-sub">Yield multiple on tools package</div>
      </div>
      <div class="b2b-metric-box">
        <div class="box-lbl">Attributed Gross Revenue</div>
        <div class="box-val">{format_brand_num(gross_new_revenue)}</div>
        <div class="box-sub">{total_conversions:.1f} pipeline deals won</div>
      </div>
    </div>
    <div class="metrics-grid-row">
      <div class="b2b-metric-box">
        <div class="box-lbl">Net Pipeline Yield</div>
        <div class="box-val">{format_brand_num(net_software_yield)}</div>
        <div class="box-sub">Net after tool expenses</div>
      </div>
      <div class="b2b-metric-box">
        <div class="box-lbl">Ad Spend Equivalent Value</div>
        <div class="box-val">{format_brand_num(comparable_ad_saved)}</div>
        <div class="box-sub">Clicks asset value saved</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    
    breakeven_units = base_saas_fee / val_ltv
    if breakeven_units < 1:
        be_string = f"just <b>1 single contract conversion</b> (clears {100/breakeven_units:.0f}% of cost boundaries)"
    else:
        be_string = f"only <b>{int(round(breakeven_units))} closed conversions</b>"

    st.markdown(f"""
    <div class="matrix-card">
      🎯 <b>Strategic Profitability Status:</b> Your marketing team needs to convert {be_string} out of the <b>{volume_leads} monthly mapped leads</b> to hit a total software cost break-even point.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 6. DYNAMIC PERFORMANCE VISUALIZATIONS ────────────────────────────────────
st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

chart_l, chart_r = st.columns([3, 2], gap="large")

with chart_l:
    st.markdown("##### Mapped Inbound Revenue Growth Over 12 Months")
    # Compound metric layout for monthly progress scaling
    months_series = list(range(1, 13))
    compounded_growth = [max((gross_new_revenue * (1 + 0.05 * i)) - base_saas_fee, 0) for i in range(12)]
    
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=months_series, y=[round(y) for y in compounded_growth],
        mode='lines+markers',
        name='Net Attributed Intent Value Curve',
        line=dict(color='#00c48c', width=4),
        marker=dict(size=7, color='#09090b', line=dict(color='#00c48c', width=2)),
        fill='tozeroy',
        fillcolor='rgba(0,196,140,0.04)'
    ))
    fig_line.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter', size=11, color='#71717a'),
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis=dict(showgrid=False, tickvals=months_series, ticktext=[f'Month {m}' for m in months_series]),
        yaxis=dict(showgrid=True, gridcolor='#f4f4f5', tickformat=','),
        height=320
    )
    st.plotly_chart(fig_line, use_container_width=True)

with chart_r:
    st.markdown("##### Capital Allocations Distribution")
    labels_pie = ['Net Revenue Yielded', 'Platinux Tool Investment']
    retained_margin = max(gross_new_revenue - base_saas_fee, 0)
    values_pie = [retained_margin, base_saas_fee]
    
    fig_pie = go.Figure(go.Pie(
        labels=labels_pie, values=values_pie, hole=0.65,
        marker=dict(colors=['#00c48c', '#09090b'], line=dict(color='#ffffff', width=2)),
        textinfo='percent', textfont=dict(size=12, family='Inter')
    ))
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', showlegend=True,
        legend=dict(orientation='h', yanchor='top', y=-0.05, xanchor='center', x=0.5),
        margin=dict(l=10, r=10, t=10, b=10), height=320
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 7. STRATEGY COMPARISON MATRIX ─────────────────────────────────────────────
st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Market Calibration</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Intent Acquisition vs Legacy Solutions</div>', unsafe_allow_html=True)

st.markdown("""
<div class="table-box">
  <div class="table-hdr">
    <span>OPERATIONAL VECTOR</span>
    <span>TRADITIONAL SOCIAL LISTENING SFW</span>
    <span>PLATINUX INTENT ENGINE</span>
  </div>
  <div class="table-row-item">
    <span class="lbl-feat">Targeting Strategy</span>
    <span class="status-negative">Vague keywords, trend graphs, and sentiment dashboards.</span>
    <span class="status-positive">Direct conversational parsing matching explicit buyer intent.</span>
  </div>
  <div class="table-row-item">
    <span class="lbl-feat">Data Delivery Model</span>
    <span class="status-negative">Requires your team to sift manually through thousands of noisy mentions.</span>
    <span class="status-positive">Actionable filtered customer payloads with direct text source links.</span>
  </div>
  <div class="table-row-item">
    <span class="lbl-feat">Cost Efficiency (CAC)</span>
    <span class="status-negative">High labor overhead needed to research data pools and build dashboards.</span>
    <span class="status-positive">Zero setup delays. Pushes verified active conversations directly to Slack.</span>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── 8. FIXED ENTERPRISE PRICING PLAN WORKSPACE ────────────────────────────────
st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

col_p1, col_p2 = st.columns([2, 3], gap="large")

with col_p1:
    st.markdown(f"""
    <div class="b2b-metric-box active-green" style="padding: 35px 30px;">
      <div style="font-size:12px; color:#00c48c; font-weight:600; text-transform:uppercase; letter-spacing:.06em; margin-bottom:8px">ENTERPRISE CORE INFRASTRUCTURE</div>
      <div style="font-size:44px; font-weight:700; color:#ffffff; margin-bottom:2px">{b_sym}{base_saas_fee:,}</div>
      <div style="font-size:13px; color:#a1a1aa; margin-bottom:25px">/ fixed monthly flat fee</div>
      <div style="font-size:13px; color:#e4e4e7; line-height:2.2; font-weight:500;">
        ✓ Complete real-time social open-web scraping access<br>
        ✓ Multi-layer conversational AI Intent Parsing models<br>
        ✓ Advanced context-de-noising data loops<br>
        ✓ Direct system integrations (Slack, Webhooks, CRM)<br>
        ✓ Unlimited marketing seat expansion allocations<br>
        ✓ Full commercial link mapping & profile data outputs
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.markdown(f"""
    <div style="padding: 15px 0px;">
      <h3 style="margin-bottom:15px; color:#09090b; font-weight:700;">Scale your customer pipeline without ad platform dependencies</h3>
      <p style="font-size:15px; color:#52525b; line-height:1.7;">
        Relying exclusively on paid ad platforms forced you into bidding cycles where Click Prices (CPC) continually climb while conversion ratios collapse. You end up burning huge marketing budgets just to attract passive researchers.
        <br><br>
        <b>Platinux switches your pipeline to active capture mode.</b> Instead of praying that a prospect sees your banner ad, we alert your growth team the exact minute a qualified buyer raises their hand inside a public community. For a single flat monthly infrastructure subscription fee, you capture high-intent accounts before they enter your competitors' standard tracking loops.
      </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── 9. CALL TO ACTION CONVERSION ZONE ─────────────────────────────────────────
st.markdown(f"""
<div class="cta-block">
  <h2>Intercept Active Buyers in Real Time</h2>
  <p>Stop monitoring keywords. Start landing verified customers where they speak on the internet.</p>
  <div style="font-size:14px; color:#71717a; margin-top:30px; font-family: monospace;">
    platinux.net · Dedicated Enterprise Node Sandboxes Available
  </div>
</div>
""", unsafe_allow_html=True)