
import streamlit as st

st.title("Evaluación Clínica de SIBO (Sobrecrecimiento Bacteriano)")

st.markdown("""
Esta herramienta está diseñada para apoyar al profesional de salud en la evaluación clínica de pacientes con sospecha de SIBO.  
**Nota:** No reemplaza el juicio clínico ni exámenes confirmatorios como el test de aliento.
""")

with st.form("form_sibo"):
    st.subheader("Síntomas gastrointestinales")
    distension = st.checkbox("Distensión abdominal")
    flatulencia = st.checkbox("Flatulencia excesiva")
    diarrea = st.checkbox("Diarrea recurrente")
    estreñimiento = st.checkbox("Estreñimiento crónico")
    dolor = st.checkbox("Dolor abdominal postprandial")

    st.subheader("Antecedentes y factores de riesgo")
    antibioticos = st.checkbox("Uso frecuente de antibióticos")
    intestino_irritable = st.checkbox("Diagnóstico previo de SII (Síndrome de Intestino Irritable)")
    cirugia_intestinal = st.checkbox("Antecedentes de cirugía intestinal o gástrica")
    diabetes = st.checkbox("Diabetes mellitus")
    hipotiroidismo = st.checkbox("Hipotiroidismo")

    submitted = st.form_submit_button("Evaluar riesgo de SIBO")

if submitted:
    puntaje = sum([
        distension, flatulencia, diarrea, estreñimiento, dolor,
        antibioticos, intestino_irritable, cirugia_intestinal, diabetes, hipotiroidismo
    ])
    
    st.subheader("Resultado:")
    if puntaje >= 6:
        st.error("Alto riesgo de SIBO. Se recomienda evaluación diagnóstica formal.")
    elif puntaje >= 3:
        st.warning("Riesgo moderado. Considere seguimiento clínico o pruebas.")
    else:
        st.success("Bajo riesgo clínico de SIBO según los criterios ingresados.")
✅ Paso 3: Baja y haz clic en “Commit changes” (Confirmar cambios)
