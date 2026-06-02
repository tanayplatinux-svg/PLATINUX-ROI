import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Platinux — Freelancer ROI Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── LIGHT THEME: Warm Minimal (Freelancer) ────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #faf9f6 !important;
  }
  .main { background: #faf9f6; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

  /* Global Animations */
  @keyframes fadeUp {
    0% { opacity: 0; transform: translateY(40px); }
    100% { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }
  .animate-up { animation: fadeUp 0.6s ease-out forwards; }
  .animate-in { animation: fadeIn 0.8s ease-out forwards; }
  .delay-1 { animation-delay: 0.1s; }
  .delay-2 { animation-delay: 0.2s; }

  /* Hero: light warm, not dark */
  .hero {
    background: #faf9f6;
    border-bottom: 1px solid #e8e4dc;
    padding: 72px 64px 56px;
    text-align: center;
  }
  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 100px;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 500;
    color: #16a34a;
    margin-bottom: 28px;
    letter-spacing: .01em;
  }
  .hero h1 {
    font-size: 48px;
    font-weight: 700;
    line-height: 1.18;
    color: #111;
    margin: 0 0 18px;
    letter-spacing: -1.5px;
  }
  .hero h1 span { color: #16a34a; }
  .hero p {
    font-size: 17px;
    color: #6b6b6b;
    max-width: 520px;
    margin: 0 auto;
    line-height: 1.65;
  }

  /* Section */
  .section { padding: 56px 64px; background: #faf9f6; }
  .section.alt { background: #f5f3ef; }
  .sec-eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #16a34a;
    margin-bottom: 8px;
  }
  .sec-title {
    font-size: 32px;
    font-weight: 700;
    color: #111;
    letter-spacing: -.5px;
    margin-bottom: 6px;
  }
  .sec-title em {
    font-style: normal;
    background: #b8fce8;
    border-radius: 6px;
    padding: 0 8px;
  }
  .sec-sub {
    font-size: 15px;
    color: #777;
    margin-bottom: 36px;
  }

  /* ── Roadmap Section Styling Integration ── */
  .plx-road-inner {
    max-width: 1100px;
    margin: 0 auto;
  }
  .plx-timeline {
    position: relative;
    margin-top: 40px;
  }
  .plx-timeline-track {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 0;
    bottom: 0;
    width: 2px;
    background: #e8e4dc;
    overflow: hidden;
  }
  .plx-timeline-progress {
    width: 100%;
    background: linear-gradient(to bottom, #16a34a, #16a34a88);
    height: 0%;
    transition: height .1s linear;
  }
  .plx-step {
    display: grid;
    grid-template-columns: 1fr 80px 1fr;
    align-items: center;
    margin-bottom: 64px;
    position: relative;
    opacity: 0;
    transition: opacity .6s ease, transform .6s ease;
  }
  .plx-step:nth-child(odd) { transform: translateX(-30px); }
  .plx-step:nth-child(even) { transform: translateX(30px); }
  .plx-step.visible {
    opacity: 1;
    transform: translateX(0) !important;
  }
  .plx-step-node {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    z-index: 2;
  }
  .plx-node-circle {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    border: 2px solid #e8e4dc;
    background: #faf9f6;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    position: relative;
    transition: border-color .4s, box-shadow .4s, background .4s;
  }
  .plx-step.visible .plx-node-circle {
    border-color: #16a34a;
    background: #fff;
    box-shadow: 0 0 0 6px rgba(22,163,74,.12), 0 0 0 12px rgba(22,163,74,.05);
  }
  .plx-node-num {
    position: absolute;
    top: -8px;
    right: -8px;
    width: 20px;
    height: 20px;
    background: #111;
    color: #fff;
    border-radius: 50%;
    font-size: 10px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #faf9f6;
  }
  .plx-step-card {
    background: #fff;
    border: 1.5px solid #e8e4dc;
    border-radius: 16px;
    padding: 24px 28px;
    position: relative;
    transition: border-color .3s, box-shadow .3s, transform .3s;
  }
  .plx-step-card:hover {
    border-color: #16a34a;
    box-shadow: 0 8px 32px rgba(22,163,74,.12);
    transform: translateY(-2px);
  }
  .plx-step-card::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 20px;
    height: 2px;
    background: #e8e4dc;
    transform: translateY(-50%);
    transition: background .4s;
  }
  .plx-step.visible .plx-step-card::after { background: #16a34a; }
  .plx-step:nth-child(odd) .plx-step-card { grid-column: 1; }
  .plx-step:nth-child(odd) .plx-step-node { grid-column: 2; }
  .plx-step:nth-child(odd) .plx-step-empty { grid-column: 3; }
  .plx-step:nth-child(odd) .plx-step-card::after { right: -22px; }
  .plx-step:nth-child(even) .plx-step-empty { grid-column: 1; }
  .plx-step:nth-child(even) .plx-step-node { grid-column: 2; }
  .plx-step:nth-child(even) .plx-step-card { grid-column: 3; }
  .plx-step:nth-child(even) .plx-step-card::after { left: -22px; }
  
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
    margin-bottom: 10px;
  }
  .plx-step-title { font-size: 18px; font-weight: 700; color: #111; margin-bottom: 8px; letter-spacing: -.3px; }
  .plx-step-desc { font-size: 14px; color: #666; line-height: 1.6; }
  .plx-step-detail { display: flex; align-items: center; gap: 8px; margin-top: 14px; font-size: 13px; color: #888; }
  .plx-step-detail strong { color: #111; font-weight: 600; }
  .plx-notif { display: flex; align-items: flex-start; gap: 10px; background: #f5f3ef; border: 1.5px solid #e8e4dc; border-radius: 10px; padding: 10px 12px; margin-top: 14px; }
  .plx-notif-dot { width: 8px; height: 8px; border-radius: 50%; background: #16a34a; margin-top: 4px; flex-shrink: 0; }
  .plx-notif-text { font-size: 12px; color: #555; line-height: 1.4; }
  .plx-notif-text strong { color: #000; }

  /* VIP Premium Money Card */
  .plx-money-card { background: #111; border: 1.5px solid #16a34a; position: relative; overflow: hidden; }
  .plx-money-card::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(ellipse at top left, rgba(22,163,74,.2) 0%, transparent 60%);
  }
  .plx-money-card .plx-step-title { color: #fff; }
  .plx-money-card .plx-step-desc { color: #aaa; }
  .plx-money-card .plx-step-detail { color: #777; }
  .plx-money-card .plx-step-detail strong { color: #16a34a; }
  .plx-money-amount { font-size: 36px; font-weight: 700; color: #16a34a; letter-spacing: -1px; margin-top: 12px; display: block; }
  .plx-money-sub { font-size: 12px; color: #555; margin-top: 2px; }

  .plx-road-cta { text-align: center; margin-top: 80px; opacity: 0; transform: translateY(30px); transition: opacity .6s .2s, transform .6s .2s; }
  .plx-road-cta.visible { opacity: 1; transform: translateY(0); }
  .plx-road-cta-title { font-size: 32px; font-weight: 700; color: #111; letter-spacing: -1px; margin-bottom: 8px; }
  .plx-road-cta-sub { font-size: 16px; color: #888; margin-bottom: 28px; }
  .plx-road-cta-btn {
    display: inline-flex; align-items: center; gap: 8px; background: #111; color: #fff; font-size: 15px; font-weight: 600;
    padding: 14px 28px; border-radius: 100px; text-decoration: none; border: none; cursor: pointer; transition: background .2s, transform .2s;
    font-family: 'DM Sans', sans-serif;
  }
  .plx-road-cta-btn:hover { background: #16a34a; color: #fff; transform: translateY(-2px); }

  /* Metric cards */
  .m-row { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 16px; }
  .mc {
    flex: 1; min-width: 130px; background: #fff; border: 1px solid #e8e4dc; border-radius: 10px; padding: 18px 20px;
    transition: box-shadow .15s;
  }
  .mc:hover { box-shadow: 0 2px 12px rgba(0,0,0,.06); }
  .mc .lbl { font-size: 11px; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; color: #aaa; margin-bottom: 6px; }
  .mc .val { font-size: 26px; font-weight: 700; color: #111; }
  .mc .sub { font-size: 12px; color: #bbb; margin-top: 3px; }
  .mc.star { background: #f0fdf4; border: 1.5px solid #86efac; }
  .mc.star .lbl { color: #16a34a; }
  .mc.star .val { color: #15803d; font-size: 30px; }
  .mc.star .sub { color: #4ade80; }

  /* Insight card */
  .note {
    background: #fff; border: 1px solid #e8e4dc; border-left: 3px solid #16a34a; border-radius: 0 8px 8px 0;
    padding: 14px 18px; font-size: 13px; color: #555; line-height: 1.65; margin-bottom: 10px;
  }
  .note b { color: #111; font-weight: 600; }

  /* Compare table */
  .ctable { background: #fff; border: 1px solid #e8e4dc; border-radius: 12px; overflow: hidden; margin-bottom: 20px; }
  .chead {
    display: grid; grid-template-columns: 2fr 1fr 1fr; background: #f5f3ef; padding: 12px 22px;
    font-size: 12px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; color: #555;
  }
  .crow { display: grid; grid-template-columns: 2fr 1fr 1fr; padding: 13px 22px; border-bottom: 1px solid #f5f3ef; font-size: 13px; align-items: center; }
  .crow:last-child { border-bottom: none; }
  .crow .lbl { color: #666; }
  .crow .bad { color: #dc2626; font-weight: 500; }
  .crow .good { color: #16a34a; font-weight: 500; }

  /* Pricing */
  .pcard { background: #fff; border: 1px solid #e8e4dc; border-radius: 12px; padding: 24px; height: 100%; min-height: 300px; }
  .pcard.best { background: #f0fdf4; border: 1.5px solid #86efac; }
  .pcard .ptag { font-size: 11px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #aaa; margin-bottom: 10px; }
  .pcard.best .ptag { color: #16a34a; }
  .pcard .pprice { font-size: 34px; font-weight: 700; color: #111; margin-bottom: 2px; }
  .pcard.best .pprice { color: #15803d; }
  .pcard .psub { font-size: 12px; color: #aaa; margin-bottom: 18px; }
  .pcard .pfeat { font-size: 13px; color: #555; line-height: 2.1; }
  .pcard.best .pfeat { color: #333; }

  /* CTA */
  .cta { background: #111; padding: 72px 64px; text-align: center; }
  .cta h2 { font-size: 38px; font-weight: 700; color: #fff; letter-spacing: -.5px; margin-bottom: 14px; }
  .cta p { font-size: 17px; color: #666; margin-bottom: 0; }
  .cta em { font-style: normal; color: #4ade80; }

  .divider { height: 1px; background: #e8e4dc; margin: 40px 0px; }

  /* Mobile Responsive Timeline Track Rules */
  @media (max-width: 768px) {
    .plx-timeline-track { left: 28px; transform: none; }
    .plx-step { grid-template-columns: 56px 1fr !important; grid-template-rows: auto; margin-bottom: 45px; }
    .plx-step:nth-child(odd) .plx-step-node,
    .plx-step:nth-child(even) .plx-step-node { grid-column: 1; grid-row: 1; justify-content: flex-start; }
    .plx-step:nth-child(odd) .plx-step-card,
    .plx-step:nth-child(even) .plx-step-card { grid-column: 2; grid-row: 1; }
    .plx-step:nth-child(odd) .plx-step-empty,
    .plx-step:nth-child(even) .plx-step-empty { display: none; }
    .plx-step:nth-child(odd) .plx-step-card::after,
    .plx-step:nth-child(even) .plx-step-card::after { left: -22px; right: auto; }
  }

  /* Hide Streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
  [data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ── HERO SECTION ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero animate-in">
  <div class="hero-badge animate-up delay-1">⚡ platinux.net/freelance - ROI Calculator</div>
  <h1 class="animate-up delay-1">Stop scaling your sales team.<br>Scale your <span>lead flow.</span></h1>
  <p class="animate-up delay-2">Platinux tracks founders and enterprises actively requesting custom development, SaaS builds, and design overhauls. Reach high-ticket clients before they post on Upwork.</p>
</div>
""", unsafe_allow_html=True)


# ── HIGH PERFORMANCE INJECTED ROADMAP COMPONENT ──────────────────────────────
st.markdown("""
<section class="section alt" style="padding-top:80px; padding-bottom:100px;">
  <div class="plx-road-inner">
    
    <!-- Header -->
    <div style="max-width: 560px; margin-bottom: 60px;">
      <div class="sec-eyebrow">🗺 Your path to clients</div>
      <h2 class="sec-title">From <em>zero</em> to paid. In 6 steps.</h2>
      <p class="sec-sub" style="margin-bottom:0;">
        Here's exactly how Platinux turns a business owner's post into money in your account — and why responding first is everything.
      </p>
    </div>

    <!-- Timeline Track Container -->
    <div class="plx-timeline" id="plx-timeline">
      <div class="plx-timeline-track">
        <div class="plx-timeline-progress" id="plx-track-fill"></div>
      </div>

      <!-- STEP 1 -->
      <div class="plx-step" data-step="1">
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#f0fff8; color:#00875a;">🔍 Step 1</div>
          <div class="plx-step-title">Business owner posts online</div>
          <div class="plx-step-desc">
            Somewhere on Reddit, Facebook, LinkedIn or Threads, a real business owner types "looking for a web developer." It goes live publicly.
          </div>
          <div class="plx-notif">
            <div class="plx-notif-dot"></div>
            <div class="plx-notif-text">
              <strong>r/entrepreneur:</strong> "Need someone to build a site for my salon — budget $800, want it done this month."
            </div>
          </div>
        </div>
        <div class="plx-step-node">
          <div class="plx-node-circle">📝<div class="plx-node-num">1</div></div>
        </div>
        <div class="plx-step-empty"></div>
      </div>

      <!-- STEP 2 -->
      <div class="plx-step" data-step="2">
        <div class="plx-step-empty"></div>
        <div class="plx-step-node">
          <div class="plx-node-circle">⚡<div class="plx-node-num">2</div></div>
        </div>
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#fff8e6; color:#b45309;">⚡ Step 2</div>
          <div class="plx-step-title">Platinux detects it instantly</div>
          <div class="plx-step-desc">
            Our engine scans 7+ platforms 24/7. The second the post goes live, we capture it, verify it's a real business owner (not spam), and score its intent.
          </div>
          <div class="plx-step-detail">
            <strong>Avg detection time:</strong> under 60 seconds
          </div>
        </div>
      </div>

      <!-- STEP 3 -->
      <div class="plx-step" data-step="3">
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#f0f9ff; color:#0369a1;">🔔 Step 3</div>
          <div class="plx-step-title">You get a real-time alert</div>
          <div class="plx-step-desc">
            Platinux sends you a direct link to the post the moment it's verified. You see the platform, the post, the budget signal — everything you need to respond.
          </div>
          <div class="plx-notif">
            <div class="plx-notif-dot"></div>
            <div class="plx-notif-text">
              <strong>🔔 New Project Alert</strong> — Salon owner · Reddit · Budget ~$800 · Posted 2 min ago
            </div>
          </div>
        </div>
        <div class="plx-step-node">
          <div class="plx-node-circle">🔔<div class="plx-node-num">3</div></div>
        </div>
        <div class="plx-step-empty"></div>
      </div>

      <!-- STEP 4 -->
      <div class="plx-step" data-step="4">
        <div class="plx-step-empty"></div>
        <div class="plx-step-node">
          <div class="plx-node-circle">💬<div class="plx-node-num">4</div></div>
        </div>
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#fdf0ff; color:#7e22ce;">💬 Step 4</div>
          <div class="plx-step-title">You reply first</div>
          <div class="plx-step-desc">
            You go directly to the post and respond — as a comment, a DM, or a reply. The business owner gets your message before they've even seen 10 other pitches.
          </div>
          <div class="plx-step-detail">
            Freelancers who respond within 1 hour close at <strong>3× the rate</strong> of those who respond later.
          </div>
        </div>
      </div>

      <!-- STEP 5 -->
      <div class="plx-step" data-step="5">
        <div class="plx-step-card">
          <div class="plx-step-tag" style="background:#fff1f0; color:#b91c1c;">🤝 Step 5</div>
          <div class="plx-step-title">Discovery call, scope, close</div>
          <div class="plx-step-desc">
            You have a conversation with a business owner who already said they need a developer. No cold pitching — they raised their hand first. Agree on scope, timeline, and price.
          </div>
          <div class="plx-step-detail">
            No platform middleman. No bidding wars.<br><strong>You own the client relationship directly.</strong>
          </div>
        </div>
        <div class="plx-step-node">
          <div class="plx-node-circle">🤝<div class="plx-node-num">5</div></div>
        </div>
        <div class="plx-step-empty"></div>
      </div>

      <!-- STEP 6 -->
      <div class="plx-step" data-step="6">
        <div class="plx-step-empty"></div>
        <div class="plx-step-node">
          <div class="plx-node-circle" style="font-size:26px;">💰<div class="plx-node-num" style="background:#16a34a; color:#fff">6</div></div>
        </div>
        <div class="plx-step-card plx-money-card">
          <div class="plx-step-tag" style="background:rgba(22,163,74,.2); color:#4ade80;">💰 Step 6</div>
          <div class="plx-step-title">Project delivered. Money in.</div>
          <div class="plx-step-desc">
            You build, deliver, and get paid. No Upwork commissions eating 20% of your income. No platform owning your client. Just you, the client, and the full project value.
          </div>
          <span class="plx-money-amount">+$2,400</span>
          <div class="plx-money-sub">avg first project from a Platinux lead · directly to you</div>
        </div>
      </div>

    </div>

    <!-- Interactive Roadmap CTA Button Entry -->
    <div class="plx-road-cta" id="plx-road-cta">
      <div class="plx-road-cta-title">Ready to start Step 1?</div>
      <div class="plx-road-cta-sub">Your next client posted today. Get the alert before anyone else does.</div>
      <button class="plx-road-cta-btn">Start Finding Clients →</button>
    </div>

  </div>
</section>

<script>
(function() {
  var stepObs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) { e.target.classList.add('visible'); }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll('.plx-step').forEach(function(el) {
    stepObs.observe(el);
  });

  var ctaObs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) e.target.classList.add('visible');
    });
  }, { threshold: 0.15 });

  var cta = document.getElementById('plx-road-cta');
  if (cta) ctaObs.observe(cta);

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
    '"Need a web developer for my restaurant — budget $1,200"',
    '"Looking for someone to build my portfolio site asap"',
    '"Small biz owner, need ecommerce site, ready to pay"',
    '"Urgent: need landing page for product launch next week"'
  ];
  var notifEls = document.querySelectorAll('.plx-notif-text');
  if (notifEls.length > 0) {
    var idx = 0;
    setInterval(function() {
      idx = (idx + 1) % notifs.length;
      notifEls[0].innerHTML = '<strong>Live post:</strong> ' + notifs[idx];
    }, 3500);
  }
})();
</script>
""", unsafe_allow_html=True)


# ── ROI CALCULATOR SECTION ────────────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Freelance Economics</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Calculate your true net profit</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-sub">Model your business overhead and see what a single subscription yields.</div>', unsafe_allow_html=True)

calc_col_left, calc_col_right = st.columns([1, 1], gap="large")

with calc_col_left:
    st.markdown("**Your Profile**")

    currency = st.selectbox("Your currency", ["USD ($)", "INR (₹)"], key="currency")
    is_inr = currency == "INR (₹)"
    sym = "₹" if is_inr else "$"
    
    plan_cost = 1999 if is_inr else 79

    if is_inr:
        avg_project = st.slider("Average project size (₹)", 10000, 500000, 80000, step=5000)
        leads_per_month = st.slider("Platinux Leads worked per month", 10, 150, 40, step=5)
        conversion_rate = st.slider("Close rate (%)", 1, 20, 5, step=1)
        freelancer_margin = st.slider("Take-home Profit Margin (%)", 30, 100, 85, step=5)
        marketing_cost = st.slider("Current platforms/Ad spend per month (₹)", 0, 50000, 5000, step=1000)
    else:
        avg_project = st.slider("Average deal size ($)", 500, 15000, 2500, step=250)
        leads_per_month = st.slider("Platinux Leads worked per month", 10, 150, 40, step=5)
        conversion_rate = st.slider("Close rate (%)", 1, 20, 5, step=1)
        freelancer_margin = st.slider("Take-home Profit Margin (%)", 30, 100, 85, step=5)
        marketing_cost = st.slider("Current platforms/Ad spend per month ($)", 0, 1000, 150, step=25)

with calc_col_right:
    st.markdown("**Your Results**")

    clients_per_month = leads_per_month * (conversion_rate / 100)
    monthly_revenue = clients_per_month * avg_project
    monthly_overhead = monthly_revenue * (1 - (freelancer_margin / 100))
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

    st.markdown(f"""
    <div class="m-row">
      <div class="mc star">
        <div class="lbl">Freelancer ROI</div>
        <div class="val">{roi_x:,}%</div>
        <div class="sub">return on {sym}{plan_cost:,}/mo</div>
      </div>
      <div class="mc">
        <div class="lbl">Gross Revenue / Mo</div>
        <div class="val">{fmt(monthly_revenue)}</div>
        <div class="sub">{clients_per_month:.1f} deals closed</div>
      </div>
    </div>
    <div class="m-row">
      <div class="mc">
        <div class="lbl">Net Take-Home / Mo</div>
        <div class="val">{fmt(monthly_profit)}</div>
        <div class="sub">At {freelancer_margin}% pocket margin</div>
      </div>
      <div class="mc">
        <div class="lbl">Annual Revenue</div>
        <div class="val">{fmt(annual_profit)}</div>
        <div class="sub">Net of Platinux fees</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    payback_clients = round(plan_cost / (avg_project * (freelancer_margin / 100)), 2)
    st.markdown(f"""
    <div class="note">
      <b>Minimal Risk.</b> You only need to close <b>{payback_clients if payback_clients > 1 else "< 1"} projects</b> to completely cover your monthly subscription from your direct cash earnings margin.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── CHART VISUALIZATIONS SECTION ──────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="sec-eyebrow">12-Month Projection</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Scaling Profit, Not Overhead</div>', unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns([3, 2], gap="large")

with chart_col1:
    months = list(range(1, 13))
    organic_monthly = [(monthly_profit * (1 + 0.01*i)) - marketing_cost for i in range(12)]
    platinux_monthly = [(monthly_profit * (1 + 0.04*i)) - plan_cost for i in range(12)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=[round(max(v,0)) for v in organic_monthly],
        mode='lines+markers',
        name='Traditional Freelance Platforms',
        line=dict(color='#dc2626', width=2, dash='dot'),
        marker=dict(size=5),
    ))
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in platinux_monthly],
        mode='lines+markers',
        name='Via Platinux Tracker',
        line=dict(color='#16a34a', width=3),
        marker=dict(size=6),
        fill='tozeroy',
        fillcolor='rgba(22,163,74,0.04)'
    ))
    fig.update_layout(
        paper_bgcolor='#faf9f6', plot_bgcolor='#faf9f6',
        font=dict(family='Inter', size=12, color='#555'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='left', x=0),
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis=dict(title='Month', showgrid=False, tickvals=months, ticktext=[f'M{m}' for m in months]),
        yaxis=dict(title=f'Net Income ({sym})', showgrid=True, gridcolor='#e8e4dc', tickformat=','),
        height=320
    )
    st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    labels = ['Take-Home Profit', f'Expenses ({(100-freelancer_margin)}%)', 'Platinux Subscription']
    values = [monthly_profit - plan_cost, monthly_overhead, plan_cost]
    colors = ['#16a34a', '#e8e4dc', '#111111']

    fig2 = go.Figure(go.Pie(
        labels=labels,
        values=[max(v, 0) for v in values],
        hole=0.6,
        marker=dict(colors=colors, line=dict(color='#faf9f6', width=2)),
        textinfo='label+percent',
        textfont=dict(size=11),
        hovertemplate='%{label}: %{value:,}<extra></extra>'
    ))
    fig2.update_layout(
        paper_bgcolor='#faf9f6', showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0), height=320,
        annotations=[dict(
            text=f"{fmt(monthly_profit - plan_cost)}<br><span style='font-size:11px'>true cash</span>",
            x=0.5, y=0.5, font_size=14, showarrow=False
        )]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── COMPARISON TABLES ─────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="sec-eyebrow">Acquisition Comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Platinux vs Upwork & Cold Outreach</div>', unsafe_allow_html=True)

marketing_yearly = marketing_cost * 12
plat_yearly = plan_cost * 12

st.markdown(f"""
<div class="ctable">
  <div class="chead">
    <span></span>
    <span>Upwork / Freelancer Connects</span>
    <span>Platinux Tracker</span>
  </div>
  <div class="crow">
    <span class="lbl">Platform Commission</span>
    <span class="bad">10% - 20% per client check</span>
    <span class="good">0% (You keep 100%)</span>
  </div>
  <div class="crow">
    <span class="lbl">Lead Quality & Intent</span>
    <span class="bad">Saturated bidding races</span>
    <span class="good">Direct high-intent responses</span>
  </div>
  <div class="crow">
    <span class="lbl">Client Connection</span>
    <span class="bad">Locked into platform messenger</span>
    <span class="good">You own the direct email/DM</span>
  </div>
  <div class="crow">
    <span class="lbl">Annual Sourcing Cost</span>
    <span class="bad">{fmt(marketing_yearly)}</span>
    <span class="good">{fmt(plat_yearly)} Flat</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── PRICING MATRIX PLANS ──────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="sec-eyebrow">Subscription Pricing</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">One deal covers the entire year.</div>', unsafe_allow_html=True)

p1, p2 = st.columns(2, gap="medium")

if is_inr:
    pro_p, agency_p = "₹1,999", "₹17,999"
    pro_sub = "Best value for freelancers"
else:
    pro_p, agency_p = "$79", "$199"
    pro_sub = "Best value for freelancers"

with p1:
    st.markdown(f"""
    <div class="pcard best">
      <div class="ptag">Pro Plan — Solo Tracker</div>
      <div class="pprice">{pro_p}</div>
      <div class="psub">/ month · {pro_sub}</div>
      <div class="pfeat">
        ✓ Unlimited incoming tracked leads<br>
        ✓ Instant real-time alerts<br>
        ✓ Discord & Custom Platform Links<br>
        ✓ 1 Dedicated Seat<br>
        ✓ 0% Platform Commission fees
      </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown(f"""
    <div class="pcard">
      <div class="ptag">Agency Core Framework</div>
      <div class="pprice">{agency_p}</div>
      <div class="psub">/ month · Built for expanding teams</div>
      <div class="pfeat">
        ✓ Everything inside the Pro Plan<br>
        ✓ 5 Connected Dashboard Seats<br>
        ✓ Active HubSpot / Salesforce Pipelines<br>
        ✓ Live Slack Team Routing Hooks<br>
        ✓ Full API Endpoint access
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── BOTTOM MARKETING FOOTER CTA ───────────────────────────────────────────────
st.markdown(f"""
<div class="cta">
  <h2>Feed your portfolio.</h2>
  <p>At {sym}{plan_cost:,}/mo, Platinux provides predictable lead sourcing without platform middleman loops.<br>
     Secure your freelance revenue baseline today.</p>
  <div style="font-size:13px; color:#555; margin-top:32px; font-family:'Inter', sans-serif;">
    platinux.net/freelance · Cancel subscription anytime
  </div>
</div>
""", unsafe_allow_html=True)
