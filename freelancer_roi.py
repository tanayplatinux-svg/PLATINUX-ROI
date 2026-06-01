import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Platinux — Freelancer ROI Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── LIGHT THEME: Warm Minimal (Freelancer) ────────────────────────────────────
# Personality: personal, approachable, warm. Like a well-designed Notion doc.
# Palette: warm whites, charcoal text, green accents, soft amber highlights.
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #faf9f6 !important;
  }
  .main { background: #faf9f6; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

  /* ── Hero: light warm, not dark ── */
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
  .hero h1 em { font-style: normal; color: #16a34a; }
  .hero p {
    font-size: 17px;
    color: #6b6b6b;
    max-width: 520px;
    margin: 0 auto;
    line-height: 1.65;
  }

  /* ── Section ── */
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
  .sec-sub {
    font-size: 15px;
    color: #777;
    margin-bottom: 36px;
  }

  /* ── Metric cards ── */
  .m-row { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 16px; }
  .mc {
    flex: 1; min-width: 130px;
    background: #fff;
    border: 1px solid #e8e4dc;
    border-radius: 10px;
    padding: 18px 20px;
    transition: box-shadow .15s;
  }
  .mc:hover { box-shadow: 0 2px 12px rgba(0,0,0,.06); }
  .mc .lbl { font-size: 11px; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; color: #aaa; margin-bottom: 6px; }
  .mc .val { font-size: 26px; font-weight: 700; color: #111; }
  .mc .sub { font-size: 12px; color: #bbb; margin-top: 3px; }
  .mc.star {
    background: #f0fdf4;
    border: 1.5px solid #86efac;
  }
  .mc.star .lbl { color: #16a34a; }
  .mc.star .val { color: #15803d; font-size: 30px; }
  .mc.star .sub { color: #4ade80; }

  /* ── Insight card ── */
  .note {
    background: #fff;
    border: 1px solid #e8e4dc;
    border-left: 3px solid #16a34a;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    font-size: 13px;
    color: #555;
    line-height: 1.65;
    margin-bottom: 10px;
  }
  .note b { color: #111; font-weight: 600; }

  /* ── Compare table ── */
  .ctable {
    background: #fff;
    border: 1px solid #e8e4dc;
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 20px;
  }
  .chead {
    display: grid; grid-template-columns: 2fr 1fr 1fr;
    background: #f5f3ef;
    padding: 12px 22px;
    font-size: 12px; font-weight: 700;
    letter-spacing: .04em; text-transform: uppercase; color: #555;
  }
  .crow {
    display: grid; grid-template-columns: 2fr 1fr 1fr;
    padding: 13px 22px;
    border-bottom: 1px solid #f5f3ef;
    font-size: 13px; align-items: center;
  }
  .crow:last-child { border-bottom: none; }
  .crow .lbl { color: #666; }
  .crow .bad { color: #dc2626; font-weight: 500; }
  .crow .good { color: #16a34a; font-weight: 500; }

  /* ── Pricing ── */
  .pcard {
    background: #fff;
    border: 1px solid #e8e4dc;
    border-radius: 12px;
    padding: 24px;
    height: 100%;
    min-height: 300px;
  }
  .pcard.best {
    background: #f0fdf4;
    border: 1.5px solid #86efac;
  }
  .pcard .ptag { font-size: 11px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #aaa; margin-bottom: 10px; }
  .pcard.best .ptag { color: #16a34a; }
  .pcard .pprice { font-size: 34px; font-weight: 700; color: #111; margin-bottom: 2px; }
  .pcard.best .pprice { color: #15803d; }
  .pcard .psub { font-size: 12px; color: #aaa; margin-bottom: 18px; }
  .pcard .pfeat { font-size: 13px; color: #555; line-height: 2.1; }
  .pcard.best .pfeat { color: #333; }

  /* ── CTA ── */
  .cta {
    background: #111;
    padding: 72px 64px;
    text-align: center;
  }
  .cta h2 { font-size: 38px; font-weight: 700; color: #fff; letter-spacing: -.5px; margin-bottom: 14px; }
  .cta p { font-size: 17px; color: #666; margin-bottom: 0; }
  .cta em { font-style: normal; color: #4ade80; }

  .divider { height: 1px; background: #e8e4dc; }

  /* Hide Streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
  [data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">⚡ Freelancer ROI — platinux.net/social</div>
  <h1>Find clients before<br>anyone else <em>even sees the post.</em></h1>
  <p>Platinux tracks business owners the moment they post asking for a web developer — so you're first in their inbox, not 50th in a proposal queue.</p>
</div>
""", unsafe_allow_html=True)


# ── ROI CALCULATOR ────────────────────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">ROI Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">What\'s Platinux worth to you?</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-sub">Adjust the sliders to match your profile. Numbers update live.</div>', unsafe_allow_html=True)

col_l, col_r = st.columns([1, 1], gap="large")

with col_l:
    st.markdown("**Your profile**")
    currency = st.selectbox("Currency", ["USD ($)", "INR (₹)"], key="currency")
    is_inr = currency == "INR (₹)"
    sym = "₹" if is_inr else "$"
    plan_cost = 1999 if is_inr else 79
    starter_cost = 799 if is_inr else 29

    if is_inr:
        rate        = st.slider("Your hourly rate (₹/hr)", 500, 8000, 1500, 100)
        avg_project = st.slider("Avg project size (₹)", 10000, 500000, 40000, 5000)
    else:
        rate        = st.slider("Your hourly rate ($/hr)", 10, 300, 75, 5)
        avg_project = st.slider("Avg project size ($)", 500, 20000, 2500, 250)

    leads_pm    = st.slider("Leads per month from Platinux", 10, 150, 35, 5)
    conv        = st.slider("Lead → client conversion (%)", 1, 30, 8, 1)
    upwork_pct  = st.slider("Upwork / Fiverr fee you currently pay (%)", 0, 30, 20, 1)
    hunt_hrs    = st.slider("Hours/week spent hunting for clients now", 1, 30, 8, 1)

with col_r:
    st.markdown("**Your numbers**")

    clients_pm      = leads_pm * (conv / 100)
    monthly_rev     = clients_pm * avg_project
    fees_saved      = monthly_rev * (upwork_pct / 100)
    time_saved      = hunt_hrs * 4 * rate
    net_gain        = monthly_rev + fees_saved + time_saved - plan_cost
    roi_x           = round(monthly_rev / plan_cost) if plan_cost else 0
    annual_gain     = net_gain * 12
    payback_days    = round((plan_cost / max(monthly_rev, 1)) * 30)

    def fmt(n):
        if is_inr:
            return f"₹{n/100000:.1f}L" if n >= 100000 else f"₹{int(round(n)):,}"
        return f"${n/1000:.1f}k" if n >= 1000 else f"${int(round(n)):,}"

    st.markdown(f"""
    <div class="m-row">
      <div class="mc star">
        <div class="lbl">Your ROI</div>
        <div class="val">{roi_x}x</div>
        <div class="sub">return on {sym}{plan_cost:,}/mo</div>
      </div>
      <div class="mc">
        <div class="lbl">Monthly revenue</div>
        <div class="val">{fmt(monthly_rev)}</div>
        <div class="sub">{clients_pm:.1f} clients × {fmt(avg_project)}</div>
      </div>
    </div>
    <div class="m-row">
      <div class="mc">
        <div class="lbl">Platform fees saved</div>
        <div class="val">{fmt(fees_saved)}</div>
        <div class="sub">vs {upwork_pct}% Upwork cut</div>
      </div>
      <div class="mc">
        <div class="lbl">Time value saved</div>
        <div class="val">{fmt(time_saved)}</div>
        <div class="sub">{hunt_hrs} hrs/wk reclaimed</div>
      </div>
      <div class="mc">
        <div class="lbl">Annual net gain</div>
        <div class="val">{fmt(annual_gain)}</div>
        <div class="sub">after Platinux cost</div>
      </div>
    </div>
    <div class="note">
      <b>Pays for itself in {payback_days} days.</b> One project from a Platinux lead covers
      {round((plan_cost / avg_project) * 100)}% of your entire monthly subscription.
      After that — every lead is pure upside.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── CHARTS ────────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section alt">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">12-Month Projection</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Your earnings over a year</div>', unsafe_allow_html=True)

cc1, cc2 = st.columns([3, 2], gap="large")

with cc1:
    months = list(range(1, 13))
    upwork_line  = [monthly_rev * (1 - upwork_pct/100) * (1 + .02*i) for i in range(12)]
    platinux_line = [(monthly_rev + time_saved/12) * (1 + .04*i) - plan_cost for i in range(12)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in upwork_line],
        name="Via Upwork/Fiverr", mode="lines+markers",
        line=dict(color="#fca5a5", width=2, dash="dot"),
        marker=dict(size=5)
    ))
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in platinux_line],
        name="Via Platinux", mode="lines+markers",
        line=dict(color="#16a34a", width=2.5),
        marker=dict(size=6),
        fill="tozeroy", fillcolor="rgba(22,163,74,0.07)"
    ))
    fig.update_layout(
        paper_bgcolor="#f5f3ef", plot_bgcolor="#f5f3ef",
        font=dict(family="Inter", size=12, color="#555"),
        legend=dict(orientation="h", y=1.08, x=0),
        margin=dict(l=0, r=0, t=30, b=0), height=300,
        xaxis=dict(showgrid=False, tickvals=months, ticktext=[f"M{m}" for m in months]),
        yaxis=dict(showgrid=True, gridcolor="#e8e4dc", tickformat=",")
    )
    st.plotly_chart(fig, use_container_width=True)

with cc2:
    fig2 = go.Figure(go.Pie(
        labels=["You keep", f"Upwork fees ({upwork_pct}%)", f"Platinux ({sym}{plan_cost:,})"],
        values=[max(round(monthly_rev * (1 - upwork_pct/100) - plan_cost), 0),
                round(monthly_rev * upwork_pct / 100),
                plan_cost],
        hole=0.62,
        marker=dict(colors=["#16a34a", "#fca5a5", "#d1d5db"],
                    line=dict(color="#f5f3ef", width=3)),
        textinfo="label+percent", textfont=dict(size=11),
        hovertemplate="%{label}: %{value:,}<extra></extra>"
    ))
    fig2.update_layout(
        paper_bgcolor="#f5f3ef", showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0), height=300,
        annotations=[dict(
            text=f"{fmt(round(monthly_rev*(1-upwork_pct/100)-plan_cost))}<br><span style='font-size:11px;color:#888'>you keep</span>",
            x=0.5, y=0.5, font_size=15, showarrow=False
        )]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── COMPARE TABLE ─────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Platform comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Platinux vs the old way</div>', unsafe_allow_html=True)

upwork_fee_per = round(avg_project * upwork_pct / 100)
plat_per       = round(plan_cost / max(clients_pm, 0.1))

st.markdown(f"""
<div class="ctable">
  <div class="chead"><span></span><span>Upwork / Fiverr</span><span>Platinux</span></div>
  <div class="crow"><span class="lbl">Cost per project</span><span class="bad">{fmt(upwork_fee_per)} ({upwork_pct}% fee)</span><span class="good">~{fmt(plat_per)} (flat)</span></div>
  <div class="crow"><span class="lbl">Time to find a client</span><span class="bad">8–15 hrs of proposals</span><span class="good">1–2 hrs of outreach</span></div>
  <div class="crow"><span class="lbl">Competition per lead</span><span class="bad">50–200 proposals</span><span class="good">You contact them first</span></div>
  <div class="crow"><span class="lbl">Monthly platform cost</span><span class="bad">{fmt(fees_saved)} in fees</span><span class="good">{sym}{plan_cost:,} flat</span></div>
  <div class="crow"><span class="lbl">Own the client?</span><span class="bad">No — platform owns it</span><span class="good">Yes — direct contact</span></div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── PRICING ───────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section alt">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Pricing</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Start for free. Pay when it works.</div>', unsafe_allow_html=True)

if is_inr:
    starter_p, pro_p = "₹799", "₹1,999"
    payg1, payg2, payg3 = "₹399", "₹999", "₹1,999"
    starter_yr, pro_yr = "₹6,999/yr", "₹17,999/yr"
else:
    starter_p, pro_p = "$29", "$79"
    payg1, payg2, payg3 = "$19", "$49", "$99"
    starter_yr, pro_yr = "$249/yr", "$699/yr"

pc1, pc2, pc3 = st.columns(3, gap="medium")
with pc1:
    st.markdown(f"""
    <div class="pcard">
      <div class="ptag">PAYG — No commitment</div>
      <div class="pprice">{payg1}</div>
      <div class="psub">starter pack · credits never expire</div>
      <div class="pfeat">
        ✓ Packs: {payg1} / {payg2} / {payg3}<br>
        ✓ Credits never expire<br>
        ✓ All lead sources<br>
        ✓ No monthly lock-in<br>
        — No real-time alerts
      </div>
    </div>
    """, unsafe_allow_html=True)

with pc2:
    st.markdown(f"""
    <div class="pcard">
      <div class="ptag">Starter</div>
      <div class="pprice">{starter_p}</div>
      <div class="psub">/ mo · or {starter_yr}</div>
      <div class="pfeat">
        ✓ 25 leads/day<br>
        ✓ 5 keywords tracked<br>
        ✓ Email alerts<br>
        ✓ Reddit + LinkedIn<br>
        — No real-time alerts
      </div>
    </div>
    """, unsafe_allow_html=True)

with pc3:
    st.markdown(f"""
    <div class="pcard best">
      <div class="ptag">Pro — Most popular</div>
      <div class="pprice">{pro_p}</div>
      <div class="psub">/ mo · or {pro_yr}</div>
      <div class="pfeat">
        ✓ Unlimited leads<br>
        ✓ Unlimited keywords<br>
        ✓ Real-time alerts<br>
        ✓ Reddit + LinkedIn + X<br>
        ✓ Lead scoring
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="cta">
  <h2>Your next client is posting <em>right now.</em></h2>
  <p>At {sym}{plan_cost:,}/mo, Platinux pays for itself after one project.<br>
  Based on your numbers — that's in {payback_days} days.</p>
</div>
""", unsafe_allow_html=True)
