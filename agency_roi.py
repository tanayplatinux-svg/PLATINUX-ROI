import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import streamlit.components.v1 as components

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


# ── UNMODIFIED SECTION 2: SUCCESS ROADMAP (HTML INJECTION) ──────────────────
roadmap_html = """
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap">
<style>
  body { margin: 0; background: #f8f7f4; }
  .plx-road-section {
    background: #f8f7f4;
    padding: 60px 0 60px;
    overflow: hidden;
    font-family: 'DM Sans', sans-serif;
    position: relative;
  }
  .plx-road-inner { max-width: 1100px; margin: 0 auto; padding: 0 24px; }
  .plx-road-header { max-width: 560px; margin-bottom: 80px; }
  .plx-road-title { font-size: clamp(30px, 4.5vw, 50px); font-weight: 700; color: #0a0a0a; letter-spacing: -1.5px; line-height: 1.1; margin: 0 0 16px; }
  .plx-road-title em { font-style: normal; background: #b8fce8; border-radius: 6px; padding: 0 8px; }
  .plx-road-sub { font-size: 17px; color: #666; line-height: 1.65; margin: 0; }
  .plx-timeline { position: relative; }
  .plx-timeline-track { position: absolute; left: 50%; transform: translateX(-50%); top: 0; bottom: 0; width: 2px; background: #e4e4e4; overflow: hidden; }
  .plx-timeline-progress { width: 100%; background: linear-gradient(to bottom, #00c48c, #00c48c88); height: 0%; transition: height .1s linear; }
  .plx-step { display: grid; grid-template-columns: 1fr 80px 1fr; align-items: center; margin-bottom: 64px; position: relative; opacity: 0; transition: opacity .6s ease, transform .6s ease; }
  .plx-step:nth-child(odd) { transform: translateX(-30px); }
  .plx-step:nth-child(even) { transform: translateX(30px); }
  .plx-step.visible { opacity: 1; transform: translateX(0) !important; }
  .plx-step-node { display: flex; align-items: center; justify-content: center; position: relative; z-index: 2; }
  .plx-node-circle { width: 56px; height: 56px; border-radius: 50%; border: 2px solid #e4e4e4; background: #f8f7f4; display: flex; align-items: center; justify-content: center; font-size: 22px; position: relative; transition: border-color .4s, box-shadow .4s, background .4s; }
  .plx-step.visible .plx-node-circle { border-color: #00c48c; background: #fff; box-shadow: 0 0 0 6px rgba(0,196,140,.12), 0 0 0 12px rgba(0,196,140,.05); }
  .plx-node-num { position: absolute; top: -8px; right: -8px; width: 20px; height: 20px; background: #000; color: #fff; border-radius: 50%; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; border: 2px solid #f7f7f5; }
  .plx-step-card { background: #fff; border: 1.5px solid #e4e4e4; border-radius: 16px; padding: 24px 28px; position: relative; transition: border-color .3s, box-shadow .3s, transform .3s; }
  .plx-step-card:hover { border-color: #00c48c; box-shadow: 0 8px 32px rgba(0,196,140,.12); transform: translateY(-2px); }
  .plx-step-card::after { content: ''; position: absolute; top: 50%; width: 20px; height: 2px; background: #e4e4e4; transform: translateY(-50%); transition: background .4s; }
  .plx-step.visible .plx-step-card::after { background: #00c48c; }
  .plx-step:nth-child(odd) .plx-step-card { grid-column: 1; }
  .plx-step:nth-child(odd) .plx-step-node { grid-column: 2; }
  .plx-step:nth-child(odd) .plx-step-empty { grid-column: 3; }
  .plx-step:nth-child(odd) .plx-step-card::after { right: -22px; }
  .plx-step:nth-child(even) .plx-step-empty { grid-column: 1; }
  .plx-step:nth-child(even) .plx-step-node { grid-column: 2; }
  .plx-step:nth-child(even) .plx-step-card { grid-column: 3; }
  .plx-step:nth-child(even) .plx-step-card::after { left: -22px; }
  .plx-step-tag { display: inline-flex; align-items: center; gap: 5px; font-size: 11px; font-weight: 700; letter-spacing: .07em; text-transform: uppercase; padding: 3px 10px; border-radius: 100px; margin-bottom: 10px; }
  .plx-step-title { font-size: 18px; font-weight: 700; color: #0a0a0a; margin-bottom: 8px; letter-spacing: -.3px; }
  .plx-step-desc { font-size: 14px; color: #666; line-height: 1.6; }
  .plx-step-detail { display: flex; align-items: center; gap: 8px; margin-top: 14px; font-size: 13px; color: #888; }
  .plx-step-detail strong { color: #0a0a0a; font-weight: 600; }
  .plx-notif { display: flex; align-items: flex-start; gap: 10px; background: #f7f7f5; border: 1.5px solid #e4e4e4; border-radius: 10px; padding: 10px 12px; margin-top: 14px; }
  .plx-notif-dot { width: 8px; height: 8px; border-radius: 50%; background: #00c48c; margin-top: 4px; flex-shrink: 0; }
  .plx-notif-text { font-size: 12px; color: #555; line-height: 1.4; }
  .plx-notif-text strong { color: #000; }
  .plx-money-card { background: #0a0a0a; border: 1.5px solid #00c48c; position: relative; overflow: hidden; }
  .plx-money-card::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse at top left, rgba(0,196,140,.2) 0%, transparent 60%); }
  .plx-money-card .plx-step-title { color: #fff; }
  .plx-money-card .plx-step-desc { color: #888; }
  .plx-money-card .plx-step-detail { color: #666; }
  .plx-money-card .plx-step-detail strong { color: #00c48c; }
  .plx-money-amount { font-size: 36px; font-weight: 700; color: #00c48c; letter-spacing: -1px; margin-top: 12px; display: block; }
  .plx-money-sub { font-size: 12px; color: #555; margin-top: 2px; }
  .plx-road-cta { text-align: center; margin-top: 80px; opacity: 0; transform: translateY(30px); transition: opacity .6s .2s, transform .6s .2s; }
  .plx-road-cta.visible { opacity: 1; transform: translateY(0); }
  .plx-road-cta-title { font-size: 32px; font-weight: 700; color: #0a0a0a; letter-spacing: -1px; margin-bottom: 8px; }
  .plx-road-cta-sub { font-size: 16px; color: #888; margin-bottom: 28px; }
  .plx-road-cta-btn { display: inline-flex; align-items: center; gap: 8px; background: #000; color: #fff; font-size: 15px; font-weight: 600; padding: 14px 28px; border-radius: 100px; text-decoration: none; border: none; cursor: pointer; transition: background .2s, transform .2s; font-family: 'DM Sans', sans-serif; }
  .plx-road-cta-btn:hover { background: #00c48c; color: #000; transform: translateY(-2px); }

  @media (max-width: 768px) {
    .plx-timeline-track { left: 28px; }
    .plx-step { grid-template-columns: 56px 1fr !important; grid-template-rows: auto; }
    .plx-step:nth-child(odd) .plx-step-node, .plx-step:nth-child(even) .plx-step-node { grid-column: 1; grid-row: 1; }
    .plx-step:nth-child(odd) .plx-step-card, .plx-step:nth-child(even) .plx-step-card { grid-column: 2; grid-row: 1; }
    .plx-step:nth-child(odd) .plx-step-empty, .plx-step:nth-child(even) .plx-step-empty { display: none; }
    .plx-step:nth-child(odd) .plx-step-card::after, .plx-step:nth-child(even) .plx-step-card::after { left: -22px; right: auto; }
  }
</style>

<section class="plx-road-section" id="plx-roadmap">
  <div class="plx-road-inner">
    <div class="plx-road-header">
      <div style="font-size:13px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:#888; margin-bottom:20px;">🗺 Your path to clients</div>
      <h2 class="plx-road-title">From <em>zero</em> to paid.<br>In 6 steps.</h2>
      <p class="plx-road-sub">Here's exactly how Platinux turns a business owner's post into money in your account — and why responding first is everything.</p>
    </div>

    <div class="plx-timeline" id="plx-timeline">
      <div class="plx-timeline-track"><div class="plx-timeline-progress" id="plx-track-fill"></div></div>

      <div class="plx-step" data-step="1">
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#f0fff8; color:#00875a;">🔍 Step 1</div>
          <div class="plx-step-title">Business owner posts online</div>
          <div class="plx-step-desc">Somewhere on Reddit, Facebook, LinkedIn or Threads, a real business owner types "looking for a web developer." It goes live publicly.</div>
          <div class="plx-notif">
            <div class="plx-notif-dot"></div>
            <div class="plx-notif-text"><strong>r/entrepreneur:</strong> "Need someone to build a site for my salon — budget $800, want it done this month."</div>
          </div>
        </div>
        <div class="plx-step-node"><div class="plx-node-circle">📝<div class="plx-node-num">1</div></div></div>
        <div class="plx-step-empty"></div>
      </div>

      <div class="plx-step" data-step="2">
        <div class="plx-step-empty"></div>
        <div class="plx-step-node"><div class="plx-node-circle">⚡<div class="plx-node-num">2</div></div></div>
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#fff8e6; color:#b45309;">⚡ Step 2</div>
          <div class="plx-step-title">Platinux detects it instantly</div>
          <div class="plx-step-desc">Our engine scans 7+ platforms 24/7. The second the post goes live, we capture it, verify it's a real business owner (not spam), and score its intent.</div>
          <div class="plx-step-detail"><strong>Avg detection time:</strong> under 60 seconds</div>
        </div>
      </div>

      <div class="plx-step" data-step="3">
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#f0f9ff; color:#0369a1;">🔔 Step 3</div>
          <div class="plx-step-title">You get a real-time alert</div>
          <div class="plx-step-desc">Platinux sends you a direct link to the post the moment it's verified. You see the platform, the post, the budget signal — everything you need to respond.</div>
          <div class="plx-notif">
            <div class="plx-notif-dot"></div>
            <div class="plx-notif-text"><strong>🔔 New Project Alert</strong> — Salon owner · Reddit · Budget ~$800 · Posted 2 min ago → <strong style="color:#00c48c">View post</strong></div>
          </div>
        </div>
        <div class="plx-step-node"><div class="plx-node-circle">🔔<div class="plx-node-num">3</div></div></div>
        <div class="plx-step-empty"></div>
      </div>

      <div class="plx-step" data-step="4">
        <div class="plx-step-empty"></div>
        <div class="plx-step-node"><div class="plx-node-circle">💬<div class="plx-node-num">4</div></div></div>
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#fdf0ff; color:#7e22ce;">💬 Step 4</div>
          <div class="plx-step-title">You reply first</div>
          <div class="plx-step-desc">You go directly to the post and respond — as a comment, a DM, or a reply. The business owner gets your message before they've even seen 10 other pitches.</div>
          <div class="plx-step-detail">Freelancers who respond within 1 hour close at <strong>3× the rate</strong> of those who respond later.</div>
        </div>
      </div>

      <div class="plx-step" data-step="5">
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#fff1f0; color:#b91c1c;">🤝 Step 5</div>
          <div class="plx-step-title">Discovery call, scope, close</div>
          <div class="plx-step-desc">You have a conversation with a business owner who already said they need a developer. No cold pitching — they raised their hand first. Agree on scope, timeline, and price.</div>
          <div class="plx-step-detail">No platform middleman. No bidding wars.<br><strong>You own the client relationship directly.</strong></div>
        </div>
        <div class="plx-step-node"><div class="plx-node-circle">🤝<div class="plx-node-num">5</div></div></div>
        <div class="plx-step-empty"></div>
      </div>

      <div class="plx-step" data-step="6">
        <div class="plx-step-empty"></div>
        <div class="plx-step-node"><div class="plx-node-circle" style="font-size:26px;">💰<div class="plx-node-num" style="background:#00c48c; color:#000">6</div></div></div>
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

    <div class="plx-road-cta" id="plx-road-cta">
      <div class="plx-road-cta-title">Ready to start Step 1?</div>
      <div class="plx-road-cta-sub">Your next client posted today. Get the alert before anyone else does.</div>
      <a href="/signin" class="plx-road-cta-btn">Start Finding Clients →</a>
    </div>
  </div>
</section>

<script>
  // Simplified scroll activation for safety inside inside Streamlit components
  setTimeout(function() {
    var cards = document.querySelectorAll('.plx-step');
    cards.forEach(function(c) { c.classList.add('visible'); });
    var cta = document.getElementById('plx-road-cta');
    if(cta) cta.classList.add('visible');
    var fill = document.getElementById('plx-track-fill');
    if(fill) fill.style.height = '100%';
  }, 400);
</script>
"""

# Render the interactive section template natively safely into the app stream
components.html(roadmap_html, height=1380, scrolling=False)


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

    # Agency Core
