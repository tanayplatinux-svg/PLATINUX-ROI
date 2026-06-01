import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Platinux Agency — ROI Calculator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── LIGHT THEME: Crisp Corporate (Agency) ─────────────────────────────────────
# Personality: sharp, data-driven, confident. Like a McKinsey deck gone SaaS.
# Palette: pure white, cool slate, indigo accents, hard blacks. Zero warmth.
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #ffffff !important;
  }
  .main { background: #ffffff; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

  /* ── Hero: pure white, bold indigo accent ── */
  .hero {
    background: #ffffff;
    border-bottom: 1px solid #e2e8f0;
    padding: 80px 72px 64px;
  }
  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #eef2ff;
    border: 1px solid #c7d2fe;
    border-radius: 4px;
    padding: 5px 12px;
    font-size: 12px;
    font-weight: 600;
    color: #4338ca;
    margin-bottom: 28px;
    letter-spacing: .04em;
    text-transform: uppercase;
  }
  .hero h1 {
    font-size: 52px;
    font-weight: 800;
    line-height: 1.1;
    color: #0f172a;
    margin: 0 0 20px;
    letter-spacing: -2px;
    max-width: 700px;
  }
  .hero h1 em { font-style: normal; color: #4f46e5; }
  .hero p {
    font-size: 17px;
    color: #64748b;
    max-width: 560px;
    margin: 0;
    line-height: 1.65;
  }

  /* ── Section ── */
  .section { padding: 60px 72px; background: #ffffff; }
  .section.alt { background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; }
  .sec-eyebrow {
    font-size: 11px; font-weight: 700;
    letter-spacing: .14em; text-transform: uppercase;
    color: #4f46e5; margin-bottom: 8px;
  }
  .sec-title {
    font-size: 30px; font-weight: 800;
    color: #0f172a; letter-spacing: -1px; margin-bottom: 6px;
  }
  .sec-sub { font-size: 15px; color: #64748b; margin-bottom: 36px; }

  /* ── Metric cards ── */
  .m-row { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 14px; }
  .mc {
    flex: 1; min-width: 130px;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 18px 20px;
    transition: border-color .15s;
  }
  .mc:hover { border-color: #a5b4fc; }
  .mc .lbl { font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: #94a3b8; margin-bottom: 6px; }
  .mc .val { font-size: 24px; font-weight: 700; color: #0f172a; }
  .mc .sub { font-size: 11px; color: #cbd5e1; margin-top: 3px; }
  .mc.star {
    background: #eef2ff;
    border: 1.5px solid #a5b4fc;
  }
  .mc.star .lbl { color: #6366f1; }
  .mc.star .val { color: #3730a3; font-size: 28px; }
  .mc.star .sub { color: #818cf8; }

  /* ── Insight card ── */
  .note {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3px solid #4f46e5;
    border-radius: 0 6px 6px 0;
    padding: 13px 18px;
    font-size: 13px; color: #475569; line-height: 1.65;
    margin-bottom: 10px;
  }
  .note b { color: #0f172a; font-weight: 700; }

  /* ── Compare table ── */
  .ctable {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 20px;
  }
  .chead {
    display: grid; grid-template-columns: 2fr 1fr 1fr;
    background: #0f172a;
    padding: 13px 22px;
    font-size: 12px; font-weight: 700;
    letter-spacing: .06em; text-transform: uppercase; color: #94a3b8;
  }
  .chead span:last-child { color: #818cf8; }
  .crow {
    display: grid; grid-template-columns: 2fr 1fr 1fr;
    padding: 13px 22px;
    border-bottom: 1px solid #f1f5f9;
    font-size: 13px; align-items: center;
  }
  .crow:last-child { border-bottom: none; }
  .crow .lbl { color: #64748b; }
  .crow .bad { color: #ef4444; font-weight: 500; }
  .crow .good { color: #4f46e5; font-weight: 600; }

  /* ── Pricing ── */
  .pcard {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 24px 26px;
    height: 100%; min-height: 300px;
  }
  .pcard.best {
    background: #0f172a;
    border: 1.5px solid #0f172a;
  }
  .pcard .ptag { font-size: 11px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: #94a3b8; margin-bottom: 12px; }
  .pcard.best .ptag { color: #818cf8; }
  .pcard .pprice { font-size: 36px; font-weight: 800; color: #0f172a; margin-bottom: 2px; letter-spacing: -1px; }
  .pcard.best .pprice { color: #ffffff; }
  .pcard .psub { font-size: 12px; color: #94a3b8; margin-bottom: 20px; }
  .pcard .pfeat { font-size: 13px; color: #64748b; line-height: 2.1; }
  .pcard.best .pfeat { color: #94a3b8; }

  /* ── CTA ── */
  .cta {
    background: #0f172a;
    padding: 80px 72px;
    text-align: center;
  }
  .cta h2 { font-size: 40px; font-weight: 800; color: #fff; letter-spacing: -1.5px; margin-bottom: 16px; }
  .cta p { font-size: 17px; color: #475569; }
  .cta em { font-style: normal; color: #818cf8; }

  .divider { height: 1px; background: #e2e8f0; }

  /* Hide Streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
  [data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">📈 Agency Plan — platinux.net/agency</div>
  <h1>Stop scaling your sales team.<br>Scale your <em>lead flow.</em></h1>
  <p>Platinux tracks founders and enterprises actively requesting custom development, SaaS builds, and design overhauls. Reach high-ticket clients before your competitors even know they exist.</p>
</div>
""", unsafe_allow_html=True)


# ── ROI CALCULATOR ────────────────────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Agency Economics</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Calculate your true net profit</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-sub">Model your agency overhead and see what a single subscription actually yields.</div>', unsafe_allow_html=True)

col_l, col_r = st.columns([1, 1], gap="large")

with col_l:
    st.markdown("**Your agency profile**")
    currency = st.selectbox("Currency", ["USD ($)", "INR (₹)"], key="currency")
    is_inr = currency == "INR (₹)"
    sym = "₹" if is_inr else "$"
    plan_cost = 17999 if is_inr else 199

    if is_inr:
        avg_project  = st.slider("Average deal size (₹)", 50000, 2000000, 400000, 50000)
        sdr_cost     = st.slider("Current outbound / ad spend per month (₹)", 40000, 800000, 150000, 20000)
    else:
        avg_project  = st.slider("Average deal size ($)", 2000, 50000, 8000, 1000)
        sdr_cost     = st.slider("Current outbound / ad spend per month ($)", 500, 10000, 2000, 500)

    leads_pm      = st.slider("Platinux leads worked per month", 20, 300, 100, 10)
    conv          = st.slider("Close rate (%)", 1, 20, 3, 1)
    agency_margin = st.slider("Net profit margin (%)", 10, 80, 40, 5)

with col_r:
    st.markdown("**Your numbers**")

    clients_pm       = leads_pm * (conv / 100)
    monthly_rev      = clients_pm * avg_project
    monthly_overhead = monthly_rev * (1 - agency_margin / 100)
    monthly_profit   = monthly_rev * (agency_margin / 100)
    net_profit       = monthly_profit - plan_cost
    annual_profit    = net_profit * 12
    roi_x            = round(monthly_profit / plan_cost) if plan_cost else 0
    payback_clients  = round(plan_cost / max(avg_project * agency_margin / 100, 1), 2)

    def fmt(n):
        if is_inr:
            return f"₹{n/100000:.1f}L" if n >= 100000 else f"₹{int(round(n)):,}"
        return f"${n/1000:.1f}k" if n >= 1000 else f"${int(round(n)):,}"

    st.markdown(f"""
    <div class="m-row">
      <div class="mc star">
        <div class="lbl">Profit ROI</div>
        <div class="val">{roi_x}x</div>
        <div class="sub">net profit vs plan cost</div>
      </div>
      <div class="mc">
        <div class="lbl">Gross revenue / mo</div>
        <div class="val">{fmt(monthly_rev)}</div>
        <div class="sub">{clients_pm:.1f} deals closed</div>
      </div>
    </div>
    <div class="m-row">
      <div class="mc">
        <div class="lbl">Net profit / mo</div>
        <div class="val">{fmt(monthly_profit)}</div>
        <div class="sub">After {100 - agency_margin}% overhead</div>
      </div>
      <div class="mc">
        <div class="lbl">SDR / ad spend saved</div>
        <div class="val">{fmt(sdr_cost)}</div>
        <div class="sub">vs current outbound cost</div>
      </div>
      <div class="mc">
        <div class="lbl">Annual net profit</div>
        <div class="val">{fmt(annual_profit)}</div>
        <div class="sub">after Platinux fees</div>
      </div>
    </div>
    <div class="note">
      <b>Minimal risk.</b> You only need to close
      <b>{payback_clients if payback_clients > 1 else "< 1"} deal{"s" if payback_clients > 1 else ""}</b>
      to cover your entire Agency subscription from net profit alone.
      Every deal after that is pure margin expansion.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── CHARTS ────────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section alt">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">12-Month Projection</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Scaling profit, not headcount</div>', unsafe_allow_html=True)

cc1, cc2 = st.columns([3, 2], gap="large")

with cc1:
    months = list(range(1, 13))
    sdr_line      = [(monthly_profit * (1 + .02*i)) - sdr_cost for i in range(12)]
    platinux_line = [(monthly_profit * (1 + .05*i)) - plan_cost for i in range(12)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=[round(max(v, 0)) for v in sdr_line],
        name="Via Ads / Outbound SDR", mode="lines+markers",
        line=dict(color="#fca5a5", width=2, dash="dot"),
        marker=dict(size=5)
    ))
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in platinux_line],
        name="Via Platinux Agency", mode="lines+markers",
        line=dict(color="#4f46e5", width=2.5),
        marker=dict(size=6),
        fill="tozeroy", fillcolor="rgba(79,70,229,0.06)"
    ))
    fig.update_layout(
        paper_bgcolor="#f8fafc", plot_bgcolor="#f8fafc",
        font=dict(family="Inter", size=12, color="#64748b"),
        legend=dict(orientation="h", y=1.08, x=0),
        margin=dict(l=0, r=0, t=30, b=0), height=300,
        xaxis=dict(showgrid=False, tickvals=months, ticktext=[f"M{m}" for m in months]),
        yaxis=dict(showgrid=True, gridcolor="#e2e8f0", tickformat=",")
    )
    st.plotly_chart(fig, use_container_width=True)

with cc2:
    fig2 = go.Figure(go.Pie(
        labels=["Agency Net Profit", f"Dev/Overhead ({100-agency_margin}%)", "Platinux Cost"],
        values=[max(monthly_profit - plan_cost, 0), round(monthly_overhead), plan_cost],
        hole=0.62,
        marker=dict(colors=["#4f46e5", "#e2e8f0", "#0f172a"],
                    line=dict(color="#f8fafc", width=3)),
        textinfo="label+percent", textfont=dict(size=11),
        hovertemplate="%{label}: %{value:,}<extra></extra>"
    ))
    fig2.update_layout(
        paper_bgcolor="#f8fafc", showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0), height=300,
        annotations=[dict(
            text=f"{fmt(max(monthly_profit - plan_cost, 0))}<br><span style='font-size:11px;color:#94a3b8'>true profit</span>",
            x=0.5, y=0.5, font_size=15, showarrow=False
        )]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── COMPARE TABLE ─────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Acquisition comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Platinux vs paid acquisition</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="ctable">
  <div class="chead"><span></span><span>B2B Ads / Outbound SDR</span><span>Platinux Agency</span></div>
  <div class="crow"><span class="lbl">Lead intent</span><span class="bad">Cold — interruptive</span><span class="good">Hot — actively asking</span></div>
  <div class="crow"><span class="lbl">Cost to scale leads</span><span class="bad">Higher spend = more leads</span><span class="good">Flat rate, unlimited leads</span></div>
  <div class="crow"><span class="lbl">Lead exclusivity</span><span class="bad">Bidding vs competitors</span><span class="good">You reach out first</span></div>
  <div class="crow"><span class="lbl">Annual acquisition cost</span><span class="bad">{fmt(sdr_cost * 12)}</span><span class="good">{fmt(plan_cost * 12)} flat</span></div>
  <div class="crow"><span class="lbl">Scales without headcount?</span><span class="bad">No — needs more SDRs</span><span class="good">Yes — 1 tool, whole team</span></div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── PRICING ───────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section alt">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Agency Plans</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">One deal covers the year.</div>', unsafe_allow_html=True)

if is_inr:
    pro_p, agency_p, scale_p = "₹1,999", "₹17,999", "Custom"
    agency_yr = "₹1,60,000/yr"
else:
    pro_p, agency_p, scale_p = "$79", "$199", "$499+"
    agency_yr = "$1,899/yr"

pc1, pc2, pc3 = st.columns(3, gap="medium")
with pc1:
    st.markdown(f"""
    <div class="pcard">
      <div class="ptag">Pro — Solo devs</div>
      <div class="pprice">{pro_p}</div>
      <div class="psub">/ mo</div>
      <div class="pfeat">
        ✓ Unlimited leads<br>
        ✓ Real-time alerts<br>
        ✓ 1 user seat<br>
        — No team routing<br>
        — No CRM integrations
      </div>
    </div>
    """, unsafe_allow_html=True)

with pc2:
    st.markdown(f"""
    <div class="pcard best">
      <div class="ptag">Agency — Built for teams</div>
      <div class="pprice">{agency_p}</div>
      <div class="psub">/ mo · or {agency_yr}</div>
      <div class="pfeat">
        ✓ Everything in Pro<br>
        ✓ 5 team seats<br>
        ✓ Slack / Discord routing<br>
        ✓ HubSpot / Salesforce sync<br>
        ✓ API access
      </div>
    </div>
    """, unsafe_allow_html=True)

with pc3:
    st.markdown(f"""
    <div class="pcard">
      <div class="ptag">Enterprise Scale</div>
      <div class="pprice">{scale_p}</div>
      <div class="psub">/ mo</div>
      <div class="pfeat">
        ✓ Unlimited team seats<br>
        ✓ Custom data pipelines<br>
        ✓ Dedicated account rep<br>
        ✓ White-label reports
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="cta">
  <h2>Feed your sales team.<br><em>Not your ad budget.</em></h2>
  <p>At {sym}{plan_cost:,}/mo — a fraction of one SDR salary.<br>
  Fill your agency pipeline with leads that are already asking.</p>
</div>
""", unsafe_allow_html=True)
