import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Platinux Agency - ROI Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── GLOBAL STYLE OVERRIDES ───────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif; 
  }
  .main { background: #f8f7f4; }
  
  .block-container { 
    padding-left: 5% !important; 
    padding-right: 5% !important; 
    max-width: 90% !important; 
  }

  /* Global Animations */
  @keyframes fadeIn { 0% { opacity: 0; } 100% { opacity: 1; } }
  @keyframes pulseHighlight {
    0% { box-shadow: 0 0 0 0 rgba(0, 196, 140, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(0, 196, 140, 0); }
    100% { box-shadow: 0 0 0 0 rgba(0, 196, 140, 0); }
  }

  .animate-in { animation: fadeIn 0.8s ease-out forwards; }

  /* Hero Section */
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

  /* Structure Headings */
  .section { padding: 60px 0px; }
  .section-label { font-size: 12px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: #888; margin-bottom: 12px; }
  .section-title { font-size: 38px; font-weight: 700; color: #0f0f0f; margin-bottom: 12px; letter-spacing: -.5px; }
  .section-title em { font-style: normal; background: #b8fce8; border-radius: 6px; padding: 0 8px; }
  .section-sub { font-size: 16px; color: #666; margin-bottom: 40px; max-width: 650px; line-height: 1.6; }

  /* Metrics Display Grid */
  .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px; }
  .metric-card {
    flex: 1; min-width: 140px; background: #fff; border: 1px solid #e8e6e0; border-radius: 12px; padding: 20px;
    transition: transform 0.2s ease;
  }
  .metric-card:hover { transform: translateY(-3px); }
  .metric-card .m-label { font-size: 12px; color: #888; margin-bottom: 6px; }
  .metric-card .m-value { font-size: 28px; font-weight: 700; color: #0f0f0f; }
  .metric-card .m-sub { font-size: 12px; color: #aaa; margin-top: 4px; }
  .metric-card.highlight { background: #0f0f0f; border-color: #0f0f0f; animation: pulseHighlight 2s infinite; }
  .metric-card.highlight .m-label { color: #888; }
  .metric-card.highlight .m-value { color: #00c48c; }
  .metric-card.highlight .m-sub { color: #666; }

  /* Comparison Data Layout styling */
  .compare-table { background: #fff; border: 1px solid #e8e6e0; border-radius: 16px; overflow: hidden; }
  .compare-header { display: grid; grid-template-columns: 2fr 1fr 1fr; background: #0f0f0f; color: #fff; padding: 14px 24px; font-size: 13px; font-weight: 600; }
  .compare-row { display: grid; grid-template-columns: 2fr 1fr 1fr; padding: 14px 24px; border-bottom: 1px solid #f0eeea; font-size: 14px; align-items: center; }
  .compare-row:last-child { border-bottom: none; }
  .compare-row .label { color: #555; }
  .compare-row .bad { color: #e24b4a; font-weight: 500; }
  .compare-row .good { color: #16a34a; font-weight: 500; }

  .insight-card { background: #fff; border: 1px solid #e8e6e0; border-left: 3px solid #00c48c; border-radius: 0 12px 12px 0; padding: 16px 20px; margin-bottom: 12px; font-size: 14px; color: #444; line-height: 1.6; }
  .insight-card b { color: #0f0f0f; font-weight: 600; }

  .cta-section { background: #0f0f0f; color: #fff; padding: 80px 60px; text-align: center; border-radius: 24px; margin-bottom: 40px; }
  .cta-section h2 { font-size: 40px; font-weight: 700; margin-bottom: 16px; letter-spacing: -.5px; }
  .cta-section p { font-size: 18px; color: #888; margin-bottom: 40px; }
  .divider { height: 1px; background: #e8e6e0; margin: 40px 0px; }

  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── HERO SECTION ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero animate-in">
  <div class="hero-badge">⚡ platinux.net/agency - ROI Calculator</div>
  <h1>Stop scaling your sales team.<br>Scale your <span>lead flow.</span></h1>
  <p>Platinux tracks founders and enterprises actively requesting custom development, SaaS builds, and design overhauls. Reach high-ticket clients before they post on Upwork.</p>
</div>
""", unsafe_allow_html=True)


# ── HIGH PERFORMANCE INJECTED ROADMAP COMPONENT ──────────────────────────────
st.markdown("""
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
    margin-
