import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Platinux — ROI Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

  .main { background: #f8f7f4; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

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
    max-width: 560px;
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
  }
  .metric-card .m-label { font-size: 12px; color: #888; margin-bottom: 6px; }
  .metric-card .m-value { font-size: 28px; font-weight: 700; color: #0f0f0f; }
  .metric-card .m-sub { font-size: 12px; color: #aaa; margin-top: 4px; }
  .metric-card.highlight { background: #0f0f0f; border-color: #0f0f0f; }
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

  /* Slider labels */
  .slider-label {
    font-size: 13px;
    color: #555;
    font-weight: 500;
    margin-bottom: 4px;
  }

  /* Hide streamlit branding */
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }

  /* Divider */
  .divider { height: 1px; background: #e8e6e0; margin: 0 60px; }
</style>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">⚡ platinux.net/social — ROI Calculator</div>
  <h1>Stop hunting for clients.<br>Let clients <span>find you first.</span></h1>
  <p>Platinux tracks business owners in real time when they post looking for web developers, designers, and tech freelancers — so you reach them before anyone else does.</p>
</div>
""", unsafe_allow_html=True)


# ── ROI CALCULATOR SECTION ────────────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">ROI Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">What\'s Platinux actually worth to you?</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Drag the sliders to match your freelance profile and see your real numbers.</div>', unsafe_allow_html=True)

# ── Inputs ────────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown("**Your profile**")

    currency = st.selectbox(
        "Your currency",
        ["USD ($)", "INR (₹)"],
        key="currency"
    )
    is_inr = currency == "INR (₹)"
    sym = "₹" if is_inr else "$"
    plan_cost = 1999 if is_inr else 79
    starter_cost = 799 if is_inr else 29
    upwork_label = "Upwork / Fiverr fee (%)"

    if is_inr:
        rate = st.slider("Your hourly rate (₹/hr)", 500, 5000, 1500, step=100)
        avg_project = st.slider("Average project size (₹)", 10000, 500000, 40000, step=5000)
    else:
        rate = st.slider("Your hourly rate ($/hr)", 10, 300, 75, step=5)
        avg_project = st.slider("Average project size ($)", 500, 20000, 2500, step=250)

    leads_per_month = st.slider("Leads you'd receive per month", 10, 150, 35, step=5)
    conversion_rate = st.slider("Lead → client conversion (%)", 1, 30, 8, step=1)
    upwork_pct = st.slider(upwork_label, 0, 30, 20, step=1)
    hours_hunting = st.slider("Hours/week currently spent finding clients", 1, 30, 8, step=1)

with col_right:
    st.markdown("**Your results**")

    # Core calculations
    clients_per_month = leads_per_month * (conversion_rate / 100)
    monthly_revenue = clients_per_month * avg_project
    upwork_fees_saved = monthly_revenue * (upwork_pct / 100)
    time_value_saved = hours_hunting * 4 * rate  # 4 weeks/month
    platinux_cost = plan_cost
    net_gain = monthly_revenue + upwork_fees_saved + time_value_saved - platinux_cost
    roi_x = round(monthly_revenue / platinux_cost) if platinux_cost > 0 else 0
    annual_gain = net_gain * 12

    def fmt(n):
        if is_inr:
            if n >= 100000:
                return f"₹{n/100000:.1f}L"
            return f"₹{int(round(n)):,}"
        else:
            if n >= 1000:
                return f"${n/1000:.1f}k"
            return f"${int(round(n)):,}"

    # Metric cards
    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card highlight">
        <div class="m-label">Platinux ROI</div>
        <div class="m-value">{roi_x}x</div>
        <div class="m-sub">return on {sym}{plan_cost:,}/mo</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Monthly revenue</div>
        <div class="m-value">{fmt(monthly_revenue)}</div>
        <div class="m-sub">{clients_per_month:.1f} clients × {fmt(avg_project)}</div>
      </div>
    </div>
    <div class="metric-row">
      <div class="metric-card">
        <div class="m-label">Platform fees saved</div>
        <div class="m-value">{fmt(upwork_fees_saved)}</div>
        <div class="m-sub">vs Upwork {upwork_pct}% per project</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Time value saved</div>
        <div class="m-value">{fmt(time_value_saved)}</div>
        <div class="m-sub">{hours_hunting} hrs/wk at {fmt(rate)}/hr</div>
      </div>
      <div class="metric-card">
        <div class="m-label">Annual net gain</div>
        <div class="m-value">{fmt(annual_gain)}</div>
        <div class="m-sub">after Platinux cost</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Payback period
    payback_days = round((platinux_cost / max(monthly_revenue, 1)) * 30)
    payback_str = f"{payback_days} days" if payback_days < 30 else "< 1 client"
    st.markdown(f"""
    <div class="insight-card">
      <b>Platinux pays for itself in {payback_str}.</b> One project from a Platinux lead covers {round((platinux_cost/avg_project)*100)}% of your entire monthly subscription.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close section


# ── CHART SECTION ─────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">12-Month Projection</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Your earnings over a year</div>', unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns([3, 2], gap="large")

with chart_col1:
    months = list(range(1, 13))
    # Upwork: revenue minus 20% fee, grows slowly
    upwork_monthly = [monthly_revenue * (1 - upwork_pct/100) * (1 + 0.02*i) for i in range(12)]
    # Platinux: full revenue, grows faster (word of mouth, more confident outreach)
    platinux_monthly = [(monthly_revenue + time_value_saved/12) * (1 + 0.04*i) - platinux_cost for i in range(12)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in upwork_monthly],
        mode='lines+markers',
        name='Via Upwork/Fiverr',
        line=dict(color='#e24b4a', width=2, dash='dot'),
        marker=dict(size=5),
    ))
    fig.add_trace(go.Scatter(
        x=months, y=[round(v) for v in platinux_monthly],
        mode='lines+markers',
        name='Via Platinux',
        line=dict(color='#4ade80', width=3),
        marker=dict(size=6),
        fill='tozeroy',
        fillcolor='rgba(74,222,128,0.06)'
    ))
    fig.update_layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        font=dict(family='Inter', size=12, color='#555'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='left', x=0),
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis=dict(
            title='Month',
            showgrid=False,
            tickvals=months,
            ticktext=[f'M{m}' for m in months]
        ),
        yaxis=dict(
            title=f'Monthly net ({sym})',
            showgrid=True,
            gridcolor='#f0eeea',
            tickformat=','
        ),
        height=320
    )
    st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    # Donut chart — revenue breakdown
    labels = ['You keep', f'Platform fees ({upwork_pct}%)', f'Platinux ({sym}{plan_cost:,}/mo)']
    values = [
        round(monthly_revenue * (1 - upwork_pct/100) - platinux_cost),
        round(monthly_revenue * upwork_pct/100),
        platinux_cost
    ]
    colors = ['#4ade80', '#e24b4a', '#0f0f0f']

    fig2 = go.Figure(go.Pie(
        labels=labels,
        values=[max(v, 0) for v in values],
        hole=0.6,
        marker=dict(colors=colors, line=dict(color='#fff', width=2)),
        textinfo='label+percent',
        textfont=dict(size=11),
        hovertemplate='%{label}: %{value:,}<extra></extra>'
    ))
    fig2.update_layout(
        paper_bgcolor='#ffffff',
        showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0),
        height=320,
        annotations=[dict(
            text=f"{fmt(monthly_revenue * (1-upwork_pct/100) - platinux_cost)}<br><span style='font-size:11px'>you keep</span>",
            x=0.5, y=0.5, font_size=14, showarrow=False
        )]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── COMPARISON TABLE ──────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Platform comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Platinux vs the alternative</div>', unsafe_allow_html=True)

upwork_fee_per_project = round(avg_project * upwork_pct / 100)
platinux_per_project = round(platinux_cost / max(clients_per_month, 0.1))

st.markdown(f"""
<div class="compare-table">
  <div class="compare-header">
    <span></span>
    <span>Via Upwork / Fiverr</span>
    <span>Via Platinux</span>
  </div>
  <div class="compare-row">
    <span class="label">Cost per project</span>
    <span class="bad">{fmt(upwork_fee_per_project)} ({upwork_pct}% fee)</span>
    <span class="good">~{fmt(platinux_per_project)} (flat rate)</span>
  </div>
  <div class="compare-row">
    <span class="label">Time to find a client</span>
    <span class="bad">8–15 hrs of proposals</span>
    <span class="good">1–2 hrs of outreach</span>
  </div>
  <div class="compare-row">
    <span class="label">Competition per lead</span>
    <span class="bad">50–200 proposals</span>
    <span class="good">You contact them first</span>
  </div>
  <div class="compare-row">
    <span class="label">Monthly platform cost</span>
    <span class="bad">{fmt(upwork_fees_saved)} in fees</span>
    <span class="good">{sym}{plan_cost:,} flat</span>
  </div>
  <div class="compare-row">
    <span class="label">Annual net at your numbers</span>
    <span class="bad">{fmt(monthly_revenue * (1-upwork_pct/100) * 12)}</span>
    <span class="good">{fmt(platinux_monthly[-1] * 12 / 12 * 12)}</span>
  </div>
  <div class="compare-row">
    <span class="label">You own the client relationship?</span>
    <span class="bad">No — platform owns it</span>
    <span class="good">Yes — direct contact</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── PRICING SECTION ───────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-label">Pricing</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Simple, no-nonsense pricing</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Start free. Pay when it makes sense for you.</div>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3, gap="medium")

if is_inr:
    starter_p, pro_p = "₹799", "₹1,999"
    payg_packs = "₹399 / ₹999 / ₹1,999"
    starter_yr, pro_yr = "₹6,999/yr", "₹17,999/yr"
else:
    starter_p, pro_p = "$29", "$79"
    payg_packs = "$19 / $49 / $99"
    starter_yr, pro_yr = "$249/yr", "$699/yr"

with p1:
    st.markdown(f"""
    <div class="metric-card" style="height:100%;min-height:320px">
      <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">PAYG</div>
      <div style="font-size:32px;font-weight:700;color:#0f0f0f;margin-bottom:4px">{payg_packs.split('/')[0].strip()}</div>
      <div style="font-size:13px;color:#aaa;margin-bottom:20px">credit packs · never expire</div>
      <div style="font-size:13px;color:#555;line-height:2">
        ✓ All packs: {payg_packs}<br>
        ✓ Credits never expire<br>
        ✓ All lead sources<br>
        ✓ No monthly commitment<br>
        — No real-time alerts
      </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown(f"""
    <div class="metric-card" style="height:100%;min-height:320px">
      <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">Starter</div>
      <div style="font-size:32px;font-weight:700;color:#0f0f0f;margin-bottom:4px">{starter_p}</div>
      <div style="font-size:13px;color:#aaa;margin-bottom:20px">/ mo · or {starter_yr}</div>
      <div style="font-size:13px;color:#555;line-height:2">
        ✓ 25 leads/day<br>
        ✓ 5 keywords<br>
        ✓ Email alerts<br>
        ✓ Reddit + LinkedIn<br>
        — No real-time alerts
      </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown(f"""
    <div class="metric-card highlight" style="height:100%;min-height:320px">
      <div style="font-size:11px;color:#4ade80;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">Pro — Most popular</div>
      <div style="font-size:32px;font-weight:700;color:#fff;margin-bottom:4px">{pro_p}</div>
      <div style="font-size:13px;color:#666;margin-bottom:20px">/ mo · or {pro_yr}</div>
      <div style="font-size:13px;color:#ccc;line-height:2">
        ✓ Unlimited leads<br>
        ✓ Unlimited keywords<br>
        ✓ Real-time alerts<br>
        ✓ Reddit + LinkedIn + X<br>
        ✓ Lead scoring
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ── CTA SECTION ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="cta-section">
  <h2>Your next client is posting<br>right now.</h2>
  <p>At {sym}{plan_cost:,}/mo, Platinux pays for itself after one project.<br>
     Based on your numbers, that's in under {payback_days} days.</p>
  <div style="font-size:14px;color:#666;margin-top:32px">
    platinux.net · Start with a free 7-day trial
  </div>
</div>
""", unsafe_allow_html=True)
