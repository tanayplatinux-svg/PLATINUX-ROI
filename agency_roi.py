import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Platinux Agency — ROI & Roadmap",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS & Animations (Agency Theme) ────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
  .main { background: #f8f7f4; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

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
  .delay-1 { animation-delay: 0.1s; }
  .delay-2 { animation-delay: 0.2s; }
  .delay-3 { animation-delay: 0.3s; }

  .hero { background: #0f0f0f; color: #fff; padding: 80px 60px 60px; text-align: center; }
  .hero-badge { display: inline-block; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 100px; padding: 6px 16px; font-size: 13px; color: #ccc; margin-bottom: 24px; }
  .hero h1 { font-size: 52px; font-weight: 700; line-height: 1.15; margin: 0 0 16px; letter-spacing: -1px; }
  .hero h1 span { color: #4ade80; }
  .hero p { font-size: 18px; color: #999; max-width: 600px; margin: 0 auto 40px; line-height: 1.6; }

  .section { padding: 64px 60px; }
  .section-label { font-size: 12px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: #888; margin-bottom: 8px; }
  .section-title { font-size: 36px; font-weight: 700; color: #0f0f0f; margin-bottom: 8px; letter-spacing: -.5px; }
  .section-sub { font-size: 16px; color: #666; margin-bottom: 40px; }

  .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px; }
  .metric-card { flex: 1; min-width: 140px; background: #fff; border: 1px solid #e8e6e0; border-radius: 12px; padding: 20px; opacity: 0; transition: transform 0.2s ease; }
  .metric-card:hover { transform: translateY(-3px); }
  .metric-card .m-label { font-size: 12px; color: #888; margin-bottom: 6px; }
  .metric-card .m-value { font-size: 28px; font-weight: 700; color: #0f0f0f; }
  .metric-card .m-sub { font-size: 12px; color: #aaa; margin-top: 4px; }
  .metric-card.highlight { background: #0f0f0f; border-color: #0f0f0f; animation: fadeUp 0.6s ease-out forwards, pulseHighlight 2s infinite; }
  .metric-card.highlight .m-label { color: #888; }
  .metric-card.highlight .m-value { color: #4ade80; }
  .metric-card.highlight .m-sub { color: #666; }

  .compare-table { background: #fff; border: 1px solid #e8e6e0; border-radius: 16px; overflow: hidden; }
  .compare-header { display: grid; grid-template-columns: 2fr 1fr 1fr; background: #0f0f0f; color: #fff; padding: 14px 24px; font-size: 13px; font-weight: 600; }
  .compare-row { display: grid; grid-template-columns: 2fr 1fr 1fr; padding: 14px 24px; border-bottom: 1px solid #f0eeea; font-size: 14px; align-items: center; }
  .compare-row:last-child { border-bottom: none; }
  .compare-row .label { color: #555; }
  .compare-row .bad { color: #e24b4a; font-weight: 500; }
  .compare-row .good { color: #16a34a; font-weight: 500; }

  .insight-card { background: #fff; border: 1px solid #e8e6e0; border-left: 3px solid #4ade80; border-radius: 0 12px 12px 0; padding: 16px 20px; margin-bottom: 12px; font-size: 14px; color: #444; line-height: 1.6; opacity: 0; }
  .insight-card b { color: #0f0f0f; font-weight: 600; }

  .cta-section { background: #0f0f0f; color: #fff; padding: 80px 60px; text-align: center; }
  .cta-section h2 { font-size: 40px; font-weight: 700; margin-bottom: 16px; letter-spacing: -.5px; }
  .cta-section p { font-size: 18px; color: #888; margin-bottom: 40px; }

  #MainMenu { visibility: hidden; } footer { visibility: hidden; } header { visibility: hidden; }
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

# ── ROADMAP SECTION (Integrated Code) ─────────────────────────────────────────
ROADMAP_HTML = """
<style>
  .plx-road-section { background: #f7f7f5; padding: 100px 0 120px; overflow: hidden; font-family: 'DM Sans', sans-serif; position: relative; }
  .plx-road-section::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px; background: #e4e4e4; }
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
  .plx-node-circle { width: 56px; height: 56px; border-radius: 50%; border: 2px solid #e4e4e4; background: #f7f7f5; display: flex; align-items: center; justify-content: center; font-size: 22px; position: relative; transition: border-color .4s, box-shadow .4s, background .4s; }
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
  .plx-notif-dot { width: 8px; height: 8px; border-radius: 50%; background: #00c48c; margin-top: 4px; flex-shrink: 0; animation: plx-live 1s ease-in-out infinite; }
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
      <div class="plx-eyebrow" style="margin-bottom:20px"><span>🗺</span> Your path to clients</div>
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
          <div class="plx-notif"><div class="plx-notif-dot"></div><div class="plx-notif-text"><strong>r/entrepreneur:</strong> "Need someone to build a site for my salon — budget $800, want it done this month."</div></div>
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
          <div class="plx-step-desc">Our engine scans 7+ platforms 24/7. The second the post goes live, we capture it, verify it's a real business owner, and score its intent.</div>
          <div class="plx-step-detail"><strong>Avg detection time:</strong> under 60 seconds</div>
        </div>
      </div>
      
      <div class="plx-step" data-step="3">
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#f0f9ff; color:#0369a1;">🔔 Step 3</div>
          <div class="plx-step-title">You get a real-time alert</div>
          <div class="plx-step-desc">Platinux sends you a direct link to the post the moment it's verified. You see the platform, the post, the budget signal — everything you need to respond.</div>
          <div class="plx-notif"><div class="plx-notif-dot"></div><div class="plx-notif-text"><strong>🔔 New Project Alert</strong> — Salon owner · Reddit · Budget ~$800 · Posted 2 min ago → <strong style="color:#00c48c">View post</strong></div></div>
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
          <div class="plx-step-detail">Agencies who respond within 1 hour close at <strong>3× the rate</strong> of those who respond later.</div>
        </div>
      </div>
      
      <div class="plx-step" data-step="5">
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#fff1f0; color:#b91c1c;">🤝 Step 5</div>
          <div class="plx-step-title">Discovery call, scope, close</div>
          <div class="plx-step-desc">You have a conversation with a business owner who already said they need an agency. No cold pitching. Agree on scope, timeline, and price.</div>
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
          <div class="plx-step-desc">You build, deliver, and get paid. No Upwork commissions eating 20% of your income. No platform owning your client. Just you and the client.</div>
          <span class="plx-money-amount">+$5,000</span>
          <div class="plx-money-sub">avg first project from an Agency lead · directly to you</div>
          <div class="plx-step-detail" style="margin-top:16px">Platinux cost: <strong>$199/mo</strong>&nbsp;&nbsp;·&nbsp;&nbsp;Your ROI: <strong>Massive</strong></div>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  var stepObs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.25 });
  document.querySelectorAll('.plx-step').forEach(function(el) { stepObs.observe(el); });

  var timeline = document.getElementById('plx-timeline');
  var fill = document.getElementById('plx-track-fill');
  if (timeline && fill) {
    window.addEventListener('scroll', function() {
      var rect = timeline.getBoundingClientRect();
      var total = rect.height;
      var seen = Math.max(0, -rect.top + window.innerHeight * 0.6);
      var pct = Math.min(100, (seen / total) * 100);
      fill.style.height = pct + '%';
    }, { passive: true });
  }

  var notifs = [
    '"Need an agency to build a custom CRM — budget $12,000"',
    '"Looking for a dev shop to handle our SaaS MVP asap"',
    '"Funded startup looking for full-stack agency, ready to pay"',
    '"Urgent: need enterprise landing pages and backend overhaul"'
  ];
  var notifEls = document.querySelectorAll('.plx-notif-text');
  if (notifEls.length > 0) {
    var idx = 0;
    setInterval(function() {
      idx = (idx + 1) % notifs.length;
      notifEls[0].innerHTML = '<strong>Live post:</strong> ' + notifs[idx];
    }, 3500);
  }
</script>
"""

# Render the HTML/JS block securely using Streamlit components
st.components.v1.html(ROADMAP_HTML, height=1300, scrolling=False)


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
    
    plan_cost = 17999 if is_inr else 199

    if is_inr:
        avg_project = st.slider("Average project size (₹)", 50000, 2000000, 400000, step=50000)
    else:
        avg_project = st.slider("Average deal size ($)", 2000, 50000, 8000, step=1000)

    leads_per_month = st.slider("Platinux Leads worked per month", 20, 300, 100, step=10)
    conversion_rate = st.slider("Close rate (%)", 1, 20, 3, step=1)
    agency_margin = st.slider("Net Profit Margin (%)", 10, 80, 40, step=5)

with col_right:
    st.markdown("**Your Agency Results**")
    clients_per_month = leads_per_month * (conversion_rate / 100)
    monthly_revenue = clients_per_month * avg_project
    monthly_overhead = monthly_revenue * (1 - (agency_margin / 100))
    monthly_profit = monthly_revenue - monthly_overhead
    roi_x = round((monthly_profit / plan_cost) * 100) if plan_cost > 0 else 0

    def fmt(n):
        if is_inr:
            return f"₹{n/100000:.1f}L" if n >= 100000 else f"₹{int(round(n)):,}"
        return f"${n/1000:.1f}k" if n >= 1000 else f"${int(round(n)):,}"

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card highlight animate-up">
        <div class="m-label">Agency ROI</div>
        <div class="m-value">{roi_x:,}%</div>
        <div class="m-sub">return on {sym}{plan_cost:,}/mo</div>
      </div>
      <div class="metric-card animate-up delay-1">
        <div class="m-label">Net Profit / Mo</div>
        <div class="m-value">{fmt(monthly_profit)}</div>
        <div class="m-sub">After {100-agency_margin}% dev overhead</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── PRICING SECTION ───────────────────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Agency Plans</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">One deal covers the year.</div>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3, gap="medium")

if is_inr:
    pro_p, agency_p, scale_p, agency_yr = "₹1,999", "₹17,999", "Custom", "₹160,000/yr"
else:
    pro_p, agency_p, scale_p, agency_yr = "$79", "$199", "$499+", "$1,899/yr"

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
        ✓ API Access
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
