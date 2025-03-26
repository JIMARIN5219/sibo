
import streamlit as st

st.title("Evaluación Clínica de SIBO (Sobrecrecimiento Bacteriano)")

st.markdown("""
Esta herramienta apoya la evaluación clínica inicial de pacientes con sospecha de SIBO.  
**Nota:** No reemplaza el juicio clínico ni pruebas diagnósticas como el test de aliento.
""")

with st.form("form_sibo"):
    st.subheader("Síntomas gastrointestinales altos")
    nausea = st.checkbox("Náuseas frecuentes")
    reflujo = st.checkbox("Reflujo gastroesofágico")
    plenitud = st.checkbox("Sensación de plenitud posprandial")

    st.subheader("Síntomas gastrointestinales bajos")
    flatulencia = st.checkbox("Flatulencia excesiva")
    diarrea = st.checkbox("Diarrea recurrente")
    estreñimiento = st.checkbox("Estreñimiento crónico")
    distension = st.checkbox("Distensión abdominal")
    dolor = st.checkbox("Dolor abdominal posprandial")

    st.subheader("Síntomas generales/sistémicos")
    fatiga = st.checkbox("Fatiga persistente")
    niebla_mental = st.checkbox("Niebla mental o dificultad para concentrarse")
    perdida_peso = st.checkbox("Pérdida de peso no intencionada")

    st.subheader("Antecedentes y factores de riesgo")
    antibioticos = st.checkbox("Uso frecuente de antibióticos")
    intestino_irritable = st.checkbox("Diagnóstico previo de SII")
    cirugia = st.checkbox("Cirugía intestinal o gástrica")
    diabetes = st.checkbox("Diabetes mellitus")
    hipotiroidismo = st.checkbox("Hipotiroidismo")

    submitted = st.form_submit_button("Evaluar riesgo de SIBO")

if submitted:
    puntaje = sum([
        nausea, reflujo, plenitud,
        flatulencia, diarrea, estreñimiento, distension, dolor,
        fatiga, niebla_mental, perdida_peso,
        antibioticos, intestino_irritable, cirugia, diabetes, hipotiroidismo
    ])

    st.subheader("Resultado clínico:")
    if puntaje >= 10:
        st.error("⚠️ Riesgo clínico ALTO de SIBO.")
        st.markdown("""
        El paciente presenta múltiples síntomas compatibles con sobrecrecimiento bacteriano, 
        incluyendo digestivos bajos y síntomas sistémicos.  
        **Recomendación:** Realizar test de aliento (glucosa o lactulosa) y considerar iniciar tratamiento empírico si no disponible.
        """)
    elif puntaje >= 6:
        st.warning("⚠️ Riesgo clínico MODERADO de SIBO.")
        st.markdown("""
        Se identifican síntomas digestivos relevantes y factores de riesgo.  
        **Recomendación:** Considerar evaluación diagnóstica adicional o monitoreo clínico con posible prueba confirmatoria.
        """)
    else:
        st.success("✅ Riesgo clínico BAJO de SIBO.")
        st.markdown("""
        El número de síntomas y factores asociados es bajo.  
        **Recomendación:** Explorar otras causas gastrointestinales. Reevaluar si persisten o progresan los síntomas.
        """)
