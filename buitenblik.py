import streamlit as st

st.set_page_config(page_title="MKB4Real Buitenblik", page_icon="⚖️", layout="wide")

st.title("MKB4Real: De Buitenblik Impact-Monitor")
st.markdown("### *Van Systeem-dwang naar Menselijke Logica*")

# --- SIDEBAR: DE DIAGNOSE ---
st.sidebar.header("1. De Nulmeting")
scenario = st.sidebar.selectbox("Kies het scenario:", 
    ["Workday Migratie", "Lokale Alignment (BE/DE)", "Bureaucratie Sanering"])

# De hoofdschuif: De Buitenblik factor
regie = st.sidebar.slider("Pas de 'Buitenblik' toe (Regie niveau):", 0, 100, 44)

st.sidebar.markdown("---")
st.sidebar.write("**MKB4Real Methode:**")
st.sidebar.caption("Organisation | People | Process")

# --- HOOFDSCHERM: DE IMPACT ---
col1, col2, col3 = st.columns(3)

with col1:
    waste = 100 - regie
    st.metric("Waste (Verspilling)", f"{waste}%", delta=f"-{regie}%", delta_color="inverse")
    st.progress(waste)

with col2:
    adoptie = int(regie * 0.9)
    st.metric("Adoptie-bereidheid", f"{adoptie}%", delta=f"+{regie}%")
    st.progress(adoptie)

with col3:
    snelheid = int(regie * 1.2) if regie * 1.2 <= 100 else 100
    st.metric("Snelheid naar Resultaat", f"{snelheid}%", delta=f"{regie}%")
    st.progress(snelheid)

# --- DE NIEUWE LOGICA-SECTIE ---
st.markdown("### 🔍 De Logica achter de Score")

with st.expander("Klik hier om te zien hoe de 'Buitenblik' de cijfers beïnvloedt", expanded=True):
    l_col, r_col = st.columns(2)
    
    with l_col:
        st.write("**Waarom is de Waste zo hoog?**")
        st.info(f"""
        Bij een score van **{regie}** zien we een directe correlatie:
        - **Approval-hell:** {int(waste * 0.7)}% van de vertraging komt door onnodige hiërarchie.
        - **Shadow IT:** Er wordt voor {int(waste * 0.4)}% buiten het systeem om gewerkt.
        - **Data-reparatie:** {int(waste * 0.3)}% van de tijd gaat op aan het herstellen van fouten.
        """)
        
    with r_col:
        st.write("**Hoe verhogen we de Flow?**")
        st.success(f"""
        Door de Regie te verhogen naar **80+**, realiseren we:
        - **CUI Minimalisatie:** Minder schermen, meer resultaat.
        - **Absorptievermogen:** Mensen begrijpen de logica weer.
        - **Zelfsturing:** Het systeem valideert, de mens beslist.
        """)

# --- DE CONCLUSIE ---
st.markdown("---")
if regie < 50:
    st.error(f"**Analyse:** Je digitaliseert momenteel een 'geasfalteerd koepad'. De tool werkt, maar de organisatie lekt.")
else:
    st.success(f"**Analyse:** De 'H' is terug in HR-Tech. De techniek faciliteert de logica.")

st.caption(f"Status: {scenario} | MKB4Real 'Buitenblik' Tool v2.0")