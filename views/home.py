import streamlit as st

def show():
    st.markdown('<h1 class="main-header">❤️ Dashboard de Predicción de Enfermedades Cardíacas</h1>', unsafe_allow_html=True)
    st.markdown("### 🎯 Bienvenido al Sistema de Predicción Cardíaca")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🔮 Predicción</h3>
            <p>Predice el riesgo cardíaco de pacientes individuales</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Análisis</h3>
            <p>Procesa múltiples pacientes desde archivos CSV</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Métricas</h3>
            <p>Visualiza el rendimiento del modelo ML</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📋 Instrucciones de Uso")
    st.markdown("""
    1. **Carga tu modelo**: Asegúrate de que tu modelo entrenado esté en la carpeta `models/`  
    2. **Predicción Individual**: Ingresa datos de un paciente para obtener predicción instantánea  
    3. **Análisis por Lotes**: Sube un archivo CSV para analizar múltiples pacientes  
    4. **Métricas**: Revisa el rendimiento de tu modelo con métricas detalladas  
    """)
