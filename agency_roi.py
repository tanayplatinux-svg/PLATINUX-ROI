<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Platinux Agency — From Lead to ROI</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap">
  <style>
    body {
      margin: 0;
      padding: 0;
      background: #f7f7f5;
    }
    
    /* Smooth transition layout container for Streamlit Integration */
    .embedded-app-container {
      background: #f8f7f4;
      padding: 40px 0 80px;
    }

    .embedded-app-frame {
      width: 100%;
      height: 900px; /* Adjust height based on calculator dimensions */
      border: none;
      display: block;
    }
  </style>
</head>
<body>

<style>
  /* ── Roadmap Section ─────────────────────────────────────── */
  .plx-road-section {
    background: #f7f7f5;
    padding: 100px 0 120px;
    overflow: hidden;
    font-family: 'DM Sans', sans-serif;
    position: relative;
  }

  .plx-road-section::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: #e4e4e4;
  }

  .plx-road-inner {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 24px;
  }

  .plx-road-header {
    max-width: 560px;
    margin-bottom: 80px;
  }

  .plx-road-title {
    font-size: clamp(30px, 4.5vw, 50px);
    font-weight: 700;
    color: #0a0a0a;
    letter-spacing: -1.5px;
    line-height: 1.1;
    margin: 0 0 16px;
  }

  .plx-road-title em {
    font-style: normal;
    background: #b8fce8;
    border-radius: 6px;
    padding: 0 8px;
  }

  .plx-road-sub {
    font-size: 17px;
    color: #666;
    line-height: 1.65;
    margin: 0;
  }

  /* ── Timeline track ── */
  .plx-timeline {
    position: relative;
  }

  /* Vertical line */
  .plx-timeline-track {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 0;
    bottom: 0;
    width: 2px;
    background: #e4e4e4;
    overflow: hidden;
  }

  .plx-timeline-progress {
    width: 100%;
    background: linear-gradient(to bottom, #00c48c, #00c48c88);
    height: 0%;
    transition: height .1s linear;
  }

  /* ── Step ── */
  .plx-step {
    display: grid;
    grid-template-columns: 1fr 80px 1fr;
    align-items: center;
    margin-bottom: 64px;
    position: relative;
    opacity: 0;
    transition: opacity .6s ease, transform .6s ease;
  }

  .plx-step:nth-child(odd) {
    transform: translateX(-30px);
  }

  .plx-step:nth-child(even) {
    transform: translateX(30px);
  }

  .plx-step.visible {
    opacity: 1;
    transform: translateX(0) !important;
  }

  /* Center node */
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
    border: 2px solid #e4e4e4;
    background: #f7f7f5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    position: relative;
    transition: border-color .4s, box-shadow .4s, background .4s;
  }

  .plx-step.visible .plx-node-circle {
    border-color: #00c48c;
    background: #fff;
    box-shadow: 0 0 0 6px rgba(0,196,140,.12), 0 0 0 12px rgba(0,196,140,.05);
  }

  .plx-node-num {
    position: absolute;
    top: -8px;
    right: -8px;
    width: 20px;
    height: 20px;
    background: #000;
    color: #fff;
    border-radius: 50%;
    font-size: 10px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #f7f7f5;
  }

  /* Step card */
  .plx-step-card {
    background: #fff;
    border: 1.5px solid #e4e4e4;
    border-radius: 16px;
    padding: 24px 28px;
    position: relative;
    transition: border-color .3s, box-shadow .3s, transform .3s;
  }

  .plx-step-card:hover {
    border-color: #00c48c;
    box-shadow: 0 8px 32px rgba(0,196,140,.12);
    transform: translateY(-2px);
  }

  /* Card arrow connector */
  .plx-step-card::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 20px;
    height: 2px;
    background: #e4e4e4;
    transform: translateY(-50%);
    transition: background .4s;
  }

  .plx-step.visible .plx-step-card::after {
    background: #00c48c;
  }

  /* Odd steps: card on left */
  .plx-step:nth-child(odd) .plx-step-card { grid-column: 1; }
  .plx-step:nth-child(odd) .plx-step-node { grid-column: 2; }
  .plx-step:nth-child(odd) .plx-step-empty { grid-column: 3; }
  .plx-step:nth-child(odd) .plx-step-card::after {
    right: -22px;
  }

  /* Even steps: card on right */
  .plx-step:nth-child(even) .plx-step-empty { grid-column: 1; }
  .plx-step:nth-child(even) .plx-step-node { grid-column: 2; }
  .plx-step:nth-child(even) .plx-step-card { grid-column: 3; }
  .plx-step:nth-child(even) .plx-step-card::after {
    left: -22px;
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
    margin-bottom: 10px;
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
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 14px;
    font-size: 13px;
    color: #888;
  }

  .plx-step-detail strong {
    color: #0a0a0a;
    font-weight: 600;
  }

  /* Mock notification */
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
    animation: plx-live 1s ease-in-out infinite;
  }

  .plx-notif-text {
    font-size: 12px;
    color: #555;
    line-height: 1.4;
  }

  .plx-notif-text strong { color: #000; }

  /* Money card final step */
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

  .plx-money-sub {
    font-size: 12px;
    color: #555;
    margin-top: 2px;
  }

  /* ── Final CTA block ── */
  .plx-road-cta {
    text-align: center;
    margin-top: 80px;
    opacity: 0;
    transform: translateY(30px);
    transition: opacity .6s .2s, transform .6s .2s;
  }

  .plx-road-cta.visible {
    opacity: 1;
    transform: translateY(0);
  }

  .plx-road-cta-title {
    font-size: 32px;
    font-weight: 700;
    color: #0a0a0a;
    letter-spacing: -1px;
    margin-bottom: 8px;
  }

  .plx-road-cta-sub {
    font-size: 16px;
    color: #888;
    margin-bottom: 28px;
  }

  .plx-road-cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #000;
    color: #fff;
    font-size: 15px;
    font-weight: 600;
    padding: 14px 28px;
    border-radius: 100px;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: background .2s, transform .2s;
    font-family: 'DM Sans', sans-serif;
  }

  .plx-road-cta-btn:hover {
    background: #00c48c;
    color: #000;
    transform: translateY(-2px);
  }

  /* Mobile */
  @media (max-width: 768px) {
    .plx-timeline-track { left: 28px; }
    .plx-step {
      grid-template-columns: 56px 1fr !important;
      grid-template-rows: auto;
    }
    .plx-step:nth-child(odd) .plx-step-node,
    .plx-step:nth-child(even) .plx-step-node { grid-column: 1; grid-row: 1; }
    .plx-step:nth-child(odd) .plx-step-card,
    .plx-step:nth-child(even) .plx-step-card { grid-column: 2; grid-row: 1; }
    .plx-step:nth-child(odd) .plx-step-empty,
    .plx-step:nth-child(even) .plx-step-empty { display: none; }
    .plx-step:nth-child(odd) .plx-step-card::after,
    .plx-step:nth-child(even) .plx-step-card::after { left: -22px; right: auto; }
  }
</style>

<section class="plx-road-section" id="plx-roadmap">
  <div class="plx-road-inner">

    <div class="plx-road-header">
      <div class="plx-eyebrow" style="margin-bottom:20px">
        <span>🗺</span> Your path to clients
      </div>
      <h2 class="plx-road-title">
        From <em>zero</em> to paid.<br>In 6 steps.
      </h2>
      <p class="plx-road-sub">
        Here's exactly how Platinux turns a business owner's post into money in your account — and why responding first is everything.
      </p>
    </div>

    <div class="plx-timeline" id="plx-timeline">
      <div class="plx-timeline-track">
        <div class="plx-timeline-progress" id="plx-track-fill"></div>
      </div>

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
              <strong>🔔 New Project Alert</strong> — Salon owner · Reddit · Budget ~$800 · Posted 2 min ago →
              <strong style="color:#00c48c">View post</strong>
            </div>
          </div>
        </div>
        <div class="plx-step-node">
          <div class="plx-node-circle">🔔<div class="plx-node-num">3</div></div>
        </div>
        <div class="plx-step-empty"></div>
      </div>

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

      <div class="plx-step" data-step="6">
        <div class="plx-step-empty"></div>
        <div class="plx-step-node">
          <div class="plx-node-circle" style="font-size:26px;">💰<div class="plx-node-num" style="background:#00c48c; color:#000">6</div></div>
        </div>
        <div class="plx-step-card plx-money-card">
          <div class="plx-step-tag" style="background:rgba(0,196,140,.15); color:#00c48c;">💰 Step 6</div>
          <div class="plx-step-title">Project delivered. Money in.</div>
          <div class="plx-step-desc">
            You build, deliver, and get paid. No Upwork commissions eating 20% of your income. No platform owning your client. Just you, the client, and the full project value.
          </div>
          <span class="plx-money-amount">+$2,400</span>
          <div class="plx-money-sub">avg first project from a Platinux lead · directly to you</div>
          <div class="plx-step-detail" style="margin-top:16px">
            Platinux cost: <strong>$79/mo</strong>&nbsp;&nbsp;·&nbsp;&nbsp;Your ROI: <strong>30×</strong>
          </div>
        </div>
      </div>

    </div><div class="plx-road-cta" id="plx-road-cta">
      <div class="plx-road-cta-title">Ready to start Step 1?</div>
      <div class="plx-road-cta-sub">Your next client posted today. Get the alert before anyone else does.</div>
      <a href="/signin" class="plx-road-cta-btn">
        Start Finding Clients →
      </a>
    </div>

  </div>
</section>

<script>
(function() {
  // Step animations
  var stepObs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
      }
    });
  }, { threshold: 0.25 });

  document.querySelectorAll('.plx-step').forEach(function(el) {
    stepObs.observe(el);
  });

  // CTA animation
  var ctaObs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) e.target.classList.add('visible');
    });
  }, { threshold: 0.3 });

  var cta = document.getElementById('plx-road-cta');
  if (cta) ctaObs.observe(cta);

  // Progress line fill on scroll
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

  // Cycling notification text
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
<div class="embedded-app-container">
  <iframe 
    src="https://your-agency-calculator.streamlit.app/?embed=true" 
    class="embedded-app-frame"
    allow="clipboard-write"
    loading="lazy">
  </iframe>
</div>
</body>
</html>
