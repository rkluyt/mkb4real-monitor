import streamlit as st

# MKB4Real Brand Setup
st.set_page_config(page_title="MKB4Real Mini Business Scan", page_icon="🎯", layout="centered")

st.title("MKB4Real: Mini Business Scan")
st.markdown("*De Buitenblik: Vreemde ogen zien wat jij niet meer ziet*")
st.markdown("---")

# --- DATA ---
scenario_data = {
    "De IT-Valstrik": {
        "onderstroom": "De techniek dicteert, de menselijke logica volgt. Je asfalteert een koepad.",
        "risico": "Digitale bureaucratie. Medewerkers haken af of werken 'om het systeem heen'.",
        "reset": "Proces-sanering. We herstellen de regie: de techniek faciliteert de mens weer."
    },
    "Papieren Werkelijkheid": {
        "onderstroom": "Er is een prachtig plan, maar op de werkvloer landt het niet. Gebrek aan verbinding.",
        "risico": "Cynisme op de werkvloer en plannen die stof vangen in de directiela.",
        "reset": "De 'Vloer-check'. We vertalen strategie naar actie op één A4."
    },
    "Onzichtbare Onvreden": {
        "onderstroom": "Stille krachten haken af. Er wordt over elkaar gepraat in plaats van met elkaar.",
        "risico": "Onverwacht verloop van talent en een sfeer van 'het zal mijn tijd wel duren'.",
        "reset": "De Dialoog. Ik voer de gesprekken die jij zelf niet meer kunt voeren."
    },
    "Stroeve Samenwerking": {
        "onderstroom": "Eilandjes. Iedereen doet zijn best, maar de flow tussen afdelingen ontbreekt.",
        "risico": "Dubbel werk, overlap en een enorme hoeveelheid 'communicatie-waste'.",
        "reset": "Silo-doorbraak. We herstellen de verbinding tussen Organisatie, Mens en Proces."
    }
}

# --- INPUT ---
st.sidebar.header("Scan Instellingen")
scenario_keuze = st.sidebar.selectbox(
    "Welke situatie herken je?", 
    options=list(scenario_data.keys()),
    key="scenario_box"
)

regie = st.sidebar.slider("Regie-niveau (Buitenblik Factor):", 0, 100, 44)

# --- IMPACT DASHBOARD ---
st.markdown("### Resultaat Mini Business Scan")
col1, col2, col3 = st.columns(3)

with col1:
    waste = 100 - regie
    st.metric("Waste (Ruis)", f"{waste}%", delta=f"-{regie}%", delta_color="inverse")
    st.progress(waste)

with col2:
    flow = int(regie * 0.9)
    st.metric("Logica & Flow", f"{flow}%", delta=f"+{regie}%")
    st.progress(flow)

with col3:
    rust = int(regie * 1.1) if regie * 1.1 <= 100 else 100
    st.metric("Focus & Rust", f"{rust}%", delta=f"{int(regie/2)}%")
    st.progress(rust)

# --- DE SPIEGEL ---
st.markdown("---")
details = scenario_data[scenario_keuze]

with st.container():
    if regie < 50:
        st.error(f"**Analyse: {scenario_keuze}**")
        st.write(f"👉 **De Onderstroom:** *{details['onderstroom']}*")
        st.write(f"⚠️ **Het Risico:** {details['risico']}")
    else:
        st.success(f"**De Reset-Route**")
        st.write(f"🎯 **Aanpak:** *{details['reset']}*")
        st.write("✅ **Winst:** Directe regie en rust in je bedrijf door een plan dat je mensen dient.")

# --- DE MKB4REAL BELOFTE ---
st.markdown("---")
st.info("### 🤝 Mijn Belofte bij een Deep Dive")
st.write("""
Als ik na drie dagen geen fundamenteel verbeterpunt vind in de verbinding tussen je mensen en je organisatie, 
dan praten we niet over de factuur, maar over de koffie.
""")

# --- SIDEBAR VOLGENDE STAPPEN ---
st.sidebar.markdown("---")
st.sidebar.subheader("Verder kijken?")
st.sidebar.write("**1. De Scherpsessie (€ 265,-)**")
st.sidebar.caption("2 uur focus. Resultaat: Stop-Start-Check op één A4.")
st.sidebar.write("**2. De Business Scan (€ 2.950,-)**")
st.sidebar.caption("3-daagse deep dive. Inclusief bovenstaande belofte.")