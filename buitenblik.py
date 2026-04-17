import streamlit as st

# Setup: Mobile First
st.set_page_config(page_title="MKB4Real Mini Scan", page_icon="🎯", layout="centered")

# Custom CSS voor compacte mobiele weergave
st.markdown("""
    <style>
    .main { padding-top: 0rem; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("Mini Business Scan")
st.markdown("*De Buitenblik op Logica & Flow*")

# --- INPUT: ALLES IN ÉÉN BLOK ---
with st.container():
    scenario_data = {
        "De IT-Valstrik": "Techniek dicteert, menselijke logica volgt.",
        "Papieren Werkelijkheid": "Prachtig plan, maar landt niet op de vloer.",
        "Onzichtbare Onvreden": "Stille krachten haken af, lucht moet geklaard.",
        "Stroeve Samenwerking": "Silo's en eilandjes; over ipv met elkaar praten."
    }
    
    keuze = st.selectbox("Selecteer Knelpunt:", list(scenario_data.keys()))
    regie = st.slider("Regie-niveau (Buitenblik):", 0, 100, 44)

st.divider()

# --- OUTPUT: HET DASHBOARD ---
c1, c2, c3 = st.columns(3)
with c1:
    waste = 100 - regie
    st.metric("Waste", f"{waste}%", delta_color="inverse")
with c2:
    flow = int(regie * 0.9)
    st.metric("Flow", f"{flow}%")
with c3:
    rust = int(regie * 1.1) if regie * 1.1 <= 100 else 100
    st.metric("Rust", f"{rust}%")

# --- DE DYNAMISCHE SPIEGEL ---
if regie < 50:
    st.error(f"**De Onderstroom:** {scenario_data[keuze]}")
else:
    st.success(f"**De Reset:** Focus op verbinding en het herstellen van de regie.")

st.divider()

# --- TRANSPARANTIE: DE FORMULES (Het "Echte" Werk) ---
with st.expander("📊 Methodologie & Logica (Transparantie)"):
    st.write("De Mini Business Scan is geen willekeurige tool, maar gebaseerd op de correlatie tussen proceszuiverheid en organisatie-absorptie.")
    
    st.markdown("#### De Correlatie-Modellen:")
    st.latex(r"Waste (W) = 100 - R")
    st.caption("Elke procent gebrek aan regie (R) resulteert in directe operationele ruis.")
    
    st.latex(r"Flow (L) = R \times 0.9")
    st.caption("Rendement volgt de logica, gecorrigeerd voor de menselijke factor.")
    
    st.latex(r"Rust (F) = \min(R \times 1.1, 100)")
    st.caption("Regie werkt als hefboom (leverage) voor organisatierust.")

# --- DE BELOFTE & CTA ---
st.info("**De MKB4Real Belofte:** Geen verbetering in 3 dagen? Geen factuur.")
st.caption("Scherpsessie: €265 | Business Scan: €2.950")