import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_sample_data

def show():
    st.markdown("### 📊 Análisis por Lotes")
    st.markdown("Sube un archivo CSV con datos de múltiples pacientes para análisis masivo.")

    uploaded_file = st.file_uploader("📁 Selecciona archivo CSV", type=['csv'])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ Archivo cargado exitosamente: {len(df)} registros")
            st.markdown("#### 👀 Vista previa de los datos:")
            st.dataframe(df.head())

            st.markdown("#### 📈 Análisis Estadístico")
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("Total Pacientes", len(df))
            if 'Sex' in df.columns:
                c2.metric("Hombres", len(df[df['Sex']=='Male']))
                c3.metric("Mujeres", len(df[df['Sex']=='Female']))
            else:
                c2.metric("BMI Promedio", f"{df['BMI'].mean():.1f}" if 'BMI' in df else "N/A")
                c3.metric("Edad Promedio", "Calculando...")
            c4.metric("Variables", len(df.columns))

            st.markdown("#### 📊 Visualizaciones")
            if 'AgeCategory' in df.columns:
                st.plotly_chart(px.histogram(df, x='AgeCategory', title='Distribución por Categoría de Edad'), use_container_width=True)
            if 'BMI' in df.columns:
                st.plotly_chart(px.box(df, y='BMI', title='Distribución del BMI'), use_container_width=True)

        except Exception as e:
            st.error(f"❌ Error al procesar el archivo: {e}")
    else:
        st.markdown("#### 💡 Datos de Ejemplo")
        st.markdown("Si no tienes un archivo, puedes usar estos datos de ejemplo:")
        df = load_sample_data()
        st.dataframe(df)
        if st.button("📊 Usar Datos de Ejemplo"):
            st.session_state['sample_data'] = df
            st.success("✅ Datos de ejemplo cargados")
