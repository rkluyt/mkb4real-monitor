import streamlit as st

# Setup: Mobile First
st.set_page_config(page_title="MKB4Real Mini Scan", page_icon="🎯", layout="centered")

# Custom CSS: De perfecte mix van Flyer-stijl en Dashboard-dynamiek
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; margin-bottom: 5px; }
    /* Scenario Tiles */
    .scenario-btn > div > button { height: 80px; background-color: #f0f4f2; border: 2px solid #1e3d37; color: #1e3d37; }
    /* Dashboard Look */
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #dee2e6; }
    .scenario-text { background-color: #f0f4f2; padding: 15px; border-left: 5px solid #1e3d37; border-radius: 5px; margin-bottom: 15px; color: #333; }
    .solution-box { background-color: #f0f4f2; padding: 12px; border-radius: 8px; border: 1px solid #1e3d37; margin-top: 8px; font-size: 14px; }
    h1, h2, h3 { color: #1e3d37 !important; margin-bottom: 5px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- TAAL & DATA ---
lang = st.radio("Language / Taal", ["NL", "EN"], horizontal=True)

data = {
    "NL": {
        "step1": "1. Kies een scenario:",
        "step2": "2. Is dit herkenbaar?",
        "scenarios": {"IT": "De IT-Valstrik", "PAPER": "Papieren Werkelijkheid", "FRICTION": "Onzichtbare Onvreden", "SILO": "Stroeve Samenwerking"},
        "details": {
            "IT": {"under": "Techniek dicteert, de mens volgt. Je asfalteert een koepad.", "risk": "Digitale bureaucratie. Medewerkers haken af. Rendement verdampt."},
            "PAPER": {"under": "Prachtig plan, maar de vloer weet niet wat ze morgen moeten doen.", "risk": "Cynisme op de vloer. De organisatie draait op routine, niet op visie."},
            "FRICTION": {"under": "Stille krachten haken af. Er wordt over elkaar gepraat ipv met elkaar.", "risk": "Talent verlaat de organisatie. Innovatiekracht ligt stil."},
            "SILO": {"under": "Eilandjes. De flow tussen afdelingen is een modderstroom geworden.", "risk": "Massale communicatie-waste en dubbel werk. Klanten voelen frictie."}
        },
        "btn": ["Heel herkenbaar", "Een beetje", "Niet"],
        "metrics": ["Waste", "Flow", "Rust"],
        "sol_title": "MKB4Real Oplossingen",
        "sol_1": "**De Scherpsessie (€ 265,-)**\n2 uur focus. Resultaat: Stop-Start-Check op één A4 binnen 24u.",
        "sol_2": "**De 3-daagse Deep Dive (€ 2.950,-)**\n3 dagen regie. Resultaat: Concreet actieplan op één A4.",
        "cta": "📧 Neem direct contact op",
        "promise": "De MKB4Real Belofte: Geen verbeterpunt gevonden? Dan geen factuur!"
    },
    "EN": {
        "step1": "1. Select scenario:",
        "step2": "2. Recognizable?",
        "scenarios": {"IT": "The IT Trap", "PAPER": "Paper Reality", "FRICTION": "Invisible Friction", "SILO": "Siloed Operations"},
        "details": {
            "IT": {"under": "Technology dictates, humans follow. You're paving a cow path.", "risk": "Digital bureaucracy. Employees disengage. ROI evaporates."},
            "PAPER": {"under": "Great strategy, but the floor has no clue how to execute.", "risk": "Cynicism among staff. Routine replaces vision."},
            "FRICTION": {"under": "Key talent is disengaging. More said in hallways than meetings.", "risk": "Loss of talent. Innovation is at a standstill."},
            "SILO": {"under": "Islands. Flow between departments is a mudslide.", "risk": "Massive communication waste. Customers feel the friction."}
        },
        "btn": ["Highly", "Somewhat", "Not at all"],
        "metrics": ["Waste", "Flow", "Peace"],
        "sol_title": "MKB4Real Solutions",
        "sol_1": "**Sharp Session (€ 265,-)**\n2h focus. Result: Stop-Start-Check on one A4.",
        "sol_2": "**3-day Deep Dive (€ 2.950,-)**\n3 days control. Result: Action plan on one A4.",
        "cta": "📧 Get in touch",
        "promise": "The MKB4Real Promise: No improvement? No invoice!"
    }
}

c = data[lang]

# --- STATE MANAGEMENT ---
if 'sc' not in st.session_state: st.session_state.sc = None
if 'regie' not in st.session_state: st.session_state.regie = None

# --- UI ---
st.title("Mini Business Scan")

# 1. SCENARIO TEGELS
st.write(f"**{c['step1']}**")
col1, col2 = st.columns(2)
with col1:
    if st.button(c["scenarios"]["IT"]): st.session_state.sc = "IT"; st.session_state.regie = None
    if st.button(c["scenarios"]["FRICTION"]): st.session_state.sc = "FRICTION"; st.session_state.regie = None
with col2:
    if st.button(c["scenarios"]["PAPER"]): st.session_state.sc = "PAPER"; st.session_state.regie = None
    if st.button(c["scenarios"]["SILO"]): st.session_state.sc = "SILO"; st.session_state.regie = None

# 2. TOON ONDERSTROOM
if st.session_state.sc:
    sc_key = st.session_state.sc
    st.markdown(f"""<div class="scenario-text"><strong>{c['scenarios'][sc_key]}:</strong><br>{c['details'][sc_key]['under']}</div>""", unsafe_allow_html=True)

    # 3. IMPACT BUTTONS
    st.write(f"**{c['step2']}**")
    b1, b2, b3 = st.columns(3)
    if b1.button(c["btn"][0]): st.session_state.regie = 25
    if b2.button(c["btn"][1]): st.session_state.regie = 55
    if b3.button(c["btn"][2]): st.session_state.regie = 85

# 4. DASHBOARD & DIAGNOSE (De 'Oogst')
if st.session_state.regie is not None:
    r = st.session_state.regie
    w, f, p = 100-r, int(r*0.9), min(int(r*1.1), 100)
    
    st.markdown("---")
    # De Visuele Balkjes
    m1, m2, m3 = st.columns(3)
    with m1: 
        st.metric(c['metrics'][0], f"{w}%")
        st.progress(w)
    with m2: 
        st.metric(c['metrics'][1], f"{f}%")
        st.progress(f)
    with m3: 
        st.metric(c['metrics'][2], f"{p}%")
        st.progress(p)

    # De Inhoudelijke Diagnose
    if r < 60:
        st.warning(f"**Risico:** {c['details'][st.session_state.sc]['risk']}")
    
    # De Oplossingen (Direct uit Flyer)
    st.write(f"### {c['sol_title']}")
    st.markdown(f"""<div class="solution-box">{c['sol_1']}</div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="solution-box">{c['sol_2']}</div>""", unsafe_allow_html=True)

    # CTA & BELOFTE
    st.divider()
    contact_url = "mailto:contact@mkb4real.nl?subject=Aanvraag%20naar%20aanleiding%20van%20Mini%20Scan"
    st.markdown(f'<a href="{contact_url}" style="text-decoration:none;"><button style="width:100%; height:55px; background-color:#1e3d37; color:white; border:none; border-radius:8px; font-size:18px; cursor:pointer;">{c["cta"]}</button></a>', unsafe_allow_html=True)
    st.caption(f"**{c['promise']}**")