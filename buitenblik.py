import streamlit as st

# Setup: Mobile First & Branding
st.set_page_config(page_title="MKB4Real Mini Scan", page_icon="🎯", layout="centered")

# Custom CSS voor de "Buitenblik" stijl en gekleurde knoppen
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    
    /* Taalkeuze styling */
    .stRadio > label { font-weight: bold; color: #1e3d37 !important; font-size: 16px; }
    
    /* Scenario knoppen (2x2 grid) */
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold; 
        height: 4.5em; 
        margin-bottom: 5px; 
        font-size: 14px !important; 
        line-height: 1.2;
        background-color: #f8f9fa;
        border: 1px solid #1e3d37;
    }

    /* STOPLICHT KLEUREN VOOR HERKENNING */
    div[data-testid="column"]:nth-of-type(1) button {
        background-color: #d9534f !important; 
        color: white !important;
        border: none !important;
    }
    div[data-testid="column"]:nth-of-type(2) button {
        background-color: #f0ad4e !important; 
        color: white !important;
        border: none !important;
    }
    div[data-testid="column"]:nth-of-type(3) button {
        background-color: #5cb85c !important; 
        color: white !important;
        border: none !important;
    }

    /* Stijl voor de Help Card inclusief Formules */
    .help-card {
        background-color: #f0f4f2;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #1e3d37;
        margin-top: 10px;
        color: #1e3d37;
    }
    .help-header { font-weight: bold; font-size: 16px; margin-bottom: 10px; border-bottom: 1px solid #1e3d37; padding-bottom: 5px; }
    .help-item { margin-bottom: 12px; font-size: 14px; line-height: 1.4; }
    .formula { font-family: monospace; font-weight: bold; background-color: #ffffff; padding: 2px 4px; border-radius: 4px; }
    
    .scenario-text { background-color: #f8f9fa; padding: 15px; border-left: 5px solid #1e3d37; border-radius: 5px; margin-bottom: 15px; }
    h1 { font-size: 26px !important; color: #1e3d37; }
    
    @media (max-width: 480px) {
        .stButton>button { font-size: 12px !important; height: 5em; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- TAAL & DATA ---
lang = st.radio("Kies je taal / Select language:", ["NL", "EN"], horizontal=True)

data = {
    "NL": {
        "step1": "1. Welk scenario herken je?",
        "step2": "2. Hoe herkenbaar is dit?",
        "scenarios": {"IT": "De IT-Valstrik", "PAPER": "Papieren Werkelijkheid", "FRICTION": "Onzichtbare Onvreden", "SILO": "Stroeve Samenwerking"},
        "details": {
            "IT": {"lbl": "De IT-Valstrik", "under": "Techniek dicteert, de mens volgt. Je bent 'vinkjes' aan het zetten voor een systeem dat de praktijk niet begrijpt."},
            "PAPER": {"lbl": "Papieren Werkelijkheid", "under": "Prachtig plan, maar op de vloer landt het niet. De verbinding tussen hoofd en handen is weg."},
            "FRICTION": {"lbl": "Onzichtbare Onvreden", "under": "Stille krachten haken af. Er wordt over elkaar gepraat ipv met elkaar. De lucht is dik."},
            "SILO": {"lbl": "Stroeve Samenwerking", "under": "Eilandjes. Iedereen doet zijn best, maar de flow tussen afdelingen is een modderstroom."}
        },
        "btn": ["Heel herkenbaar", "Beetje", "Niet"],
        "help_title": "🔍 Hoe we de impact berekenen",
        "help_html": """
<div class="help-card">
    <div class="help-header">De Buitenblik Logica</div>
    <div class="help-item"><b>🗑️ Waste (Ruis)</b><br>Energie die weglekt door onduidelijke regie en systeemdwang.<br><span class="formula">W = 100 - Regie</span></div>
    <div class="help-item"><b>🌊 Flow (Rendement)</b><br>De soepelheid waarmee actie door de keten beweegt.<br><span class="formula">F = Regie x 0.9</span></div>
    <div class="help-item"><b>🧘 Rust (Focus)</b><br>De mentale ruimte voor innovatie en energie.<br><span class="formula">Rust = Regie x 1.1</span></div>
</div>
""",
        "sol_1": "**De Scherpsessie (€ 265,-)**: 2 uur focus op één situatie.",
        "sol_2": "**De 3-daagse Deep Dive (€ 2.950,-)**: 3 dagen regie op de vloer.",
        "cta": "📧 Neem direct contact op",
        "promise": "MKB4Real Belofte: Geen fundamenteel verbeterpunt gevonden in drie dagen? Geen factuur!"
    },
    "EN": {
        "step1": "1. Which scenario do you recognize?",
        "step2": "2. How recognizable is this?",
        "scenarios": {"IT": "The IT Trap", "PAPER": "Paper Reality", "FRICTION": "Invisible Friction", "SILO": "Siloed Operations"},
        "details": {
            "IT": {"lbl": "The IT Trap", "under": "Technology dictates, humans follow. You're paving a cow path for a system."},
            "PAPER": {"lbl": "Paper Reality", "under": "Great strategy, but it doesn't land on the work floor. Connection lost."},
            "FRICTION": {"lbl": "Invisible Friction", "under": "Key talent is disengaging. More is said in hallways than meetings."},
            "SILO": {"lbl": "Siloed Operations", "under": "Islands. Everyone does their best, but the flow is clogged by handovers."}
        },
        "btn": ["Highly", "Somewhat", "Not at all"],
        "help_title": "🔍 How we calculate impact",
        "help_html": """
<div class="help-card">
    <div class="help-header">The 'Outside-In' Logic</div>
    <div class="help-item"><b>🗑️ Waste (Noise)</b><br>Energy lost due to lack of control and system constraints.<br><span class="formula">W = 100 - Control</span></div>
    <div class="help-item"><b>🌊 Flow (Yield)</b><br>Smoothness of action moving through the value chain.<br><span class="formula">F = Control x 0.9</span></div>
    <div class="help-item"><b>🧘 Peace (Focus)</b><br>Mental space for innovation and energy.<br><span class="formula">Peace = Control x 1.1</span></div>
</div>
""",
        "sol_1": "**Sharp Session (€ 265,-)**: 2 hours of deep focus.",
        "sol_2": "**3-day Deep Dive (€ 2.950,-)**: 3 days of control on-site.",
        "cta": "📧 Get in touch",
        "promise": "MKB4Real Promise: No fundamental improvement found in three days? No invoice!"
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
col_t_l, col_t_r = st.columns(2)
col_b_l, col_b_r = st.columns(2)
with col_t_l: 
    if st.button(c["scenarios"]["IT"]): st.session_state.sc = "IT"; st.session_state.regie = None
with col_t_r: 
    if st.button(c["scenarios"]["PAPER"]): st.session_state.sc = "PAPER"; st.session_state.regie = None
with col_b_l: 
    if st.button(c["scenarios"]["FRICTION"]): st.session_state.sc = "FRICTION"; st.session_state.regie = None
with col_b_r: 
    if st.button(c["scenarios"]["SILO"]): st.session_state.sc = "SILO"; st.session_state.regie = None

# 2. TOON ONDERSTROOM
if st.session_state.sc:
    s = c["details"][st.session_state.sc]
    st.markdown(f"""<div class="scenario-text"><strong>{s['lbl']}:</strong> {s['under']}</div>""", unsafe_allow_html=True)

    # 3. IMPACT BUTTONS
    st.write(f"**{c['step2']}**")
    b1, b2, b3 = st.columns(3)
    if b1.button(c["btn"][0]): st.session_state.regie = 25
    if b2.button(c["btn"][1]): st.session_state.regie = 55
    if b3.button(c["btn"][2]): st.session_state.regie = 85

# 4. DASHBOARD
if st.session_state.regie is not None:
    r = st.session_state.regie
    st.markdown("---")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Waste", f"{100-r}%"); st.progress(100-r)
    with m2: st.metric("Flow", f"{int(r*0.9)}%"); st.progress(int(r*0.9))
    with m3: st.metric("Rust", f"{min(int(r*1.1), 100)}%"); st.progress(min(int(r*1.1), 100))

    # De Help Card MET Formules
    with st.expander(c["help_title"]):
        st.markdown(c["help_html"], unsafe_allow_html=True)

    st.info(f"### {c['sol_1']}\n\n{c['sol_2']}")
    
    contact_url = "mailto:contact@mkb4real.nl?subject=Aanvraag%20Mini%20Scan"
    st.markdown(f'<a href="{contact_url}" style="text-decoration:none;"><button style="background-color:#1e3d37; color:white; border:none; border-radius:8px; font-size:18px; cursor:pointer;">{c["cta"]}</button></a>', unsafe_allow_html=True)
    st.caption(f"**{c['promise']}**")