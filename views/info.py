import streamlit as st

def show():
    st.markdown("### ℹ️ Información del Sistema")
    st.markdown("""
    #### 🎯 Objetivo del Sistema
    Este dashboard fue diseñado para facilitar la predicción de enfermedades cardíacas
    utilizando un modelo de Machine Learning supervisado.

    #### 📊 Variables Utilizadas
    - **HadHeartAttack**: Historial de ataque cardíaco
    - **HadDiabetes**: Presencia de diabetes
    - **HadStroke**: Historial de derrame cerebral
    - **BMI**: Índice de masa corporal
    - **GeneralHealth**: Estado general de salud
    - **PhysicalHealthDays**: Días con mala salud física
    - **SmokerStatus**: Estado de fumador
    - **PhysicalActivities**: Realización de actividad física
    - **SleepHours**: Horas de sueño
    - **AlcoholDrinkers**: Consumo de alcohol
    - **HadDepressiveDisorder**: Trastorno depresivo
    - **MentalHealthDays**: Días con mala salud mental
    - **DifficultyWalking**: Dificultad para caminar
    - **AgeCategory**: Categoría de edad
    - **Sex**: Sexo del paciente

    #### 🛠️ Tecnologías Utilizadas
    - **Python**: Lenguaje de programación principal
    - **Streamlit**: Framework para el dashboard web
    - **Scikit-learn**: Librería de Machine Learning
    - **Plotly**: Visualizaciones interactivas
    - **Pandas**: Manipulación de datos

    #### 📧 Contacto
    Para soporte técnico o consultas sobre el modelo, contacta al desarrollador.
    """)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **Versiones de Librerías:**
        - Streamlit: 1.28.1
        - Pandas: 2.1.1
        - Scikit-learn: 1.3.0
        - Plotly: 5.17.0
        """)
    with c2:
        st.markdown("""
        **Características del Modelo:**
        - Tipo: Clasificación Binaria
        - Algoritmo: [Tu algoritmo aquí]
        - Precisión: ~87%
        - Última actualización: [Fecha]
        """)
