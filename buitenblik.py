import streamlit as st

st.set_page_config(page_title="MKB4Real Impact Monitor", page_icon="⚖️")

st.title("MKB4Real: De Buitenblik Impact-Monitor")
st.markdown("---")

# Zijbalk voor de 'Pijn-analyse'
st.sidebar.header("Scenario Analyse")
knelpunt = st.sidebar.radio(
    "Wat is de grootste blokkade?",
    ("Wachten op goedkeuring (Waste)", 
     "Systeem is leidend (IT-Valstrik)", 
     "Medewerkers haken af (Adoptie-moeheid)",
     "Data is onbetrouwbaar (Chaos)")
)

# De Slider: De Buitenblik factor
st.subheader("Regie: Van Systeem-dwang naar Menselijke Logica")
regie = st.slider("Hoeveel 'Buitenblik' passen we toe?", 0, 100, 20)

# De Impact Metrics (De Rekensom)
col1, col2, col3 = st.columns(3)

with col1:
    # Berekening voor verspilling (Tijd/Geld)
    waste = 100 - regie
    st.metric("Waste (Inefficiëntie)", f"{waste}%", f"-{regie}%", delta_color="inverse")
    st.caption("Onnodige vinkjes & wachttijd")

with col2:
    # Berekening voor de 'H' factor
    happiness = int(regie * 0.9)
    st.metric("Adoptie-bereidheid", f"{happiness}%", f"+{regie}%")
    st.caption("Focus op de menselijke maat")

with col3:
    # Time-to-Value
    speed = int(regie * 1.2)
    if speed > 100: speed = 100
    st.metric("Snelheid naar Resultaat", f"{speed}%", f"{regie}%")
    st.caption("Flow in de operatie")

st.markdown("---")

# De 'Killer' Conclusie
if regie < 40:
    st.error(f"### 🚩 Risico: {knelpunt}")
    st.write(f"In dit scenario wordt de organisatie gegijzeld door de techniek. De manager is een 'vinkjesmachine' geworden. Gevolg: De 'H' verdwijnt en de implementatiekosten lopen met 30% op door verborgen 'Waste'.")
elif 40 <= regie < 80:
    st.warning("### 🔄 De Kanteling: Logica keert terug")
    st.write("De Buitenblik saneert de processen. We stoppen met het 'asfalteren van het koepad'. De wachttijden nemen af en de data wordt voor het eerst weer betrouwbaar.")
else:
    st.success("### 🎯 Het MKB4Real Resultaat: Maximale Flow")
    st.write("De techniek faciliteert de mens. Geen overlap, geen dubbel werk. De organisatie absorbeert de verandering moeiteloos omdat de proceslogica weer leidend is.")

st.info(f"**Robert's Advies:** Voor {knelpunt} is geen nieuwe module nodig, maar een proces-reset.")