import streamlit as st

# Setup: Mobile First & Wide Layout for impact
st.set_page_config(page_title="MKB4Real Mini Scan", page_icon="🎯", layout="centered")

# Custom CSS voor professionele uitstraling
st.markdown("""
    <style>
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 12px; border: 1px solid #eee; }
    .main { padding-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("Mini Business Scan")
st.markdown("*De Buitenblik op Logica & Flow*")

# --- 1. DE DATA (De uitgebreide expert-uitleg hersteld) ---
scenario_data = {
    "De IT-Valstrik": {
        "onderstroom": "De techniek dicteert, de menselijke logica volgt. Je bent 'vinkjes' aan het zetten voor een systeem dat de praktijk niet begrijpt. Je asfalteert een koepad.",
        "risico": "Digitale bureaucratie. Medewerkers haken af, creëren hun eigen 'schaduw-lijstjes' en het rendement op je IT-investering verdampt waar je bij staat.",
        "reset": "Proces-sanering. We halen de techniek uit de lead en herstellen de menselijke regie. De tool gaat de mens weer faciliteren in plaats van gijzelen."
    },
    "Papieren Werkelijkheid": {
        "onderstroom": "Er is een prachtig strategisch plan, maar op de werkvloer weet niemand wat ze morgen anders moeten doen. De verbinding tussen hoofd en handen is weg.",
        "risico": "Cynisme bij je beste mensen en plannen die stof vangen in de directiela. De organisatie draait op routine, niet op visie.",
        "reset": "De 'Vloer-check'. We slopen de ivoren toren en vertalen de strategie naar drie concrete, begrijpelijke stappen op één A4. Actie boven rapportage."
    },
    "Onzichtbare Onvreden": {
        "onderstroom": "De 'stille krachten' haken emotioneel af. Er wordt in de wandelgangen meer gezegd dan in de vergadering. De lucht is dik van onuitgesproken zaken.",
        "risico": "Onverwacht verloop van je cruciale talent en een sfeer van 'het zal mijn tijd wel duren'. De innovatiekracht van je bedrijf ligt volledig stil.",
        "reset": "De Dialoog. Ik voer als buitenstaander de gesprekken die jij zelf niet meer kunt voeren. We klaren de lucht en herstellen het psychologische contract."
    },
    "Stroeve Samenwerking": {
        "onderstroom": "Eilandjes (silo's). Iedereen doet zijn best op zijn eigen vierkante meter, maar de flow tussen afdelingen is een modderstroom geworden.",
        "risico": "Enorm veel 'communicatie-waste', dubbel werk en overlap. Klanten voelen de interne frictie in de kwaliteit van je levering.",
        "reset": "Silo-doorbraak. We herstellen de ketenlogica en de verbinding tussen Organisatie, Mens en Proces. We stoppen met over elkaar praten en gaan mét elkaar bouwen."
    }
}

# --- 2. DE BEDIENING ---
keuze = st.selectbox("Welk scenario herken je?", list(scenario_data.keys()))
regie = st.slider("Regie-niveau (De Buitenblik Factor):", 0, 100, 44)

# --- 3. DE SPIEGEL (Nu weer met volle diepgang) ---
st.markdown("---")
details = scenario_data[keuze]

if regie < 50:
    st.error(f"### 🔍 De Spiegel op: {keuze}")
    st.write(f"**De Onderstroom:**\n*{details['onderstroom']}*")
    st.write(f"**⚠️ Het Risico:** {details['risico']}")
else:
    st.success(f"### 🎯 De MKB4Real Reset")
    st.write(f"**De Aanpak:**\n*{details['reset']}*")
    st.write("**✅ Resultaat:** Directe regie en rust in je bedrijf door een plan dat je mensen écht dient.")

st.markdown("---")

# --- 4. IMPACT DASHBOARD (Visueel & Krachtig) ---
st.markdown("### Impact op de Bedrijfsvoering")
c1, c2, c3 = st.columns(3)

with c1:
    waste = 100 - regie
    st.metric("🗑️ Waste", f"{waste}%")
    st.progress(waste)
    st.caption("Operationele ruis")

with c2:
    flow = int(regie * 0.9)
    st.metric("🌊 Flow", f"{flow}%")
    st.progress(flow)
    st.caption("Rendement")

with c3:
    rust = int(regie * 1.1) if regie * 1.1 <= 100 else 100
    st.metric("🧘 Rust", f"{rust}%")
    st.progress(rust)
    st.caption("Focus & Energie")

st.divider()

# --- 5. TRANSPARANTIE & BELOFTE ---
with st.expander("📊 Methodologie & Logica (Transparantie)"):
    st.write("De Mini Business Scan berekent de correlatie tussen proceszuiverheid en organisatie-absorptie:")
    st.latex(r"Waste (W) = 100 - R")
    st.latex(r"Flow (F) = R \times 0.9")
    st.latex(r"Rust (R_u) = \min(R \times 1.1, 100)")
    st.caption("Modellen gebaseerd op het snijvlak van Organisatie, Mens en Proces.")

st.info("### 🤝 De MKB4Real Belofte\nVind ik binnen 3 dagen geen fundamenteel verbeterpunt? Dan praten we niet over de factuur, maar over de koffie.")
st.caption("Scherpsessie: € 265,- | Business Scan: € 2.950,-")