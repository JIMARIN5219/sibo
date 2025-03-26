import streamlit as st

st.set_page_config(page_title="Árbol de Decisión - SIBO", layout="centered")
st.title("Árbol de decisión para SIBO (Small Intestinal Bacterial Overgrowth)")

st.markdown("""
Este asistente interactivo está diseñado para ayudar en la **evaluación clínica funcional de SIBO**, integrando síntomas clave y el resultado del **test de aliento**.
""")

# Entrada de síntomas
st.header("1. Evaluación de síntomas")
sintomas = {
    "Distensión abdominal": st.checkbox("Distensión abdominal"),
    "Gases frecuentes": st.checkbox("Gases frecuentes"),
    "Dolor postprandial": st.checkbox("Dolor postprandial"),
    "Diarrea o estreñimiento": st.checkbox("Diarrea o estreñimiento"),
    "Sensación de comida no digerida": st.checkbox("Sensación de comida no digerida")
}

# Evaluación inicial basada en síntomas
sintomas_presentes = sum(sintomas.values())

# Entrada de resultado del test de aliento
st.header("2. Resultado del test de aliento")
test_aliento = st.radio("¿Cuál fue el resultado del test de aliento (glucosa o lactulosa)?", ["No realizado", "Negativo", "Positivo"])

# Análisis del árbol de decisión
st.header("3. Evaluación del riesgo de SIBO")
if sintomas_presentes >= 3 and test_aliento == "Positivo":
    st.success("Alta probabilidad de SIBO. Considerar tratamiento antimicrobiano funcional + dieta específica + evaluación de causas subyacentes.")
elif sintomas_presentes >= 3 and test_aliento == "No realizado":
    st.warning("Síntomas compatibles con SIBO. Se recomienda realizar el test de aliento para confirmar.")
elif sintomas_presentes >= 3 and test_aliento == "Negativo":
    st.info("Síntomas presentes pero test negativo. Considerar falso negativo, o explorar disbiosis distal / otras causas digestivas.")
elif sintomas_presentes < 3 and test_aliento == "Positivo":
    st.warning("Pocos síntomas pero test positivo. Evaluar si hay sobretratamiento o SIBO asintomático.")
else:
    st.info("Baja probabilidad de SIBO clínico en este momento. Monitorear o considerar otros diagnósticos funcionales.")

st.markdown("---")
st.caption("Esta herramienta no reemplaza el juicio clínico. Desarrollada con fines educativos y exploratorios.")
