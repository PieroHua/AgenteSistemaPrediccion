import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from utils.data_loader import load_model
from utils.preprocessing import preprocess_input_data

def show():
    st.markdown("### 🔮 Predicción Individual de Riesgo Cardíaco")

    # Intentar cargar el modelo
    model = load_model("models/heart_disease_model.pkl")
    if model is None:
        st.warning("⚠️ No se pudo cargar el modelo. Usando modo demostración.")

    st.markdown("#### 📝 Ingrese los datos del paciente:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🏥 Historial Médico**")
        had_heart_attack = st.selectbox("¿Ha tenido ataque cardíaco?", ["No", "Sí"])
        had_diabetes = st.selectbox("¿Tiene diabetes?", ["No", "Sí"])
        had_stroke = st.selectbox("¿Ha tenido derrame cerebral?", ["No", "Sí"])
        had_depressive_disorder = st.selectbox("¿Tiene trastorno depresivo?", ["No", "Sí"])
        difficulty_walking = st.selectbox("¿Tiene dificultad para caminar?", ["No", "Sí"])
        st.markdown("**⚖️ Datos Físicos**")
        bmi = st.number_input("BMI (Índice de Masa Corporal)", min_value=10.0, max_value=60.0, value=27.17, step=0.1)
        age_category = st.selectbox("Categoría de Edad", ['18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80+'])
        sex = st.selectbox("Sexo", ["Masculino", "Femenino"])
    with col2:
        st.markdown("**🏃‍♂️ Estilo de Vida**")
        general_health = st.selectbox("Salud General", ["Excelente","Muy Buena","Buena","Regular","Mala"])
        physical_health_days = st.number_input("Días con mala salud física (último mes)", min_value=0, max_value=30, value=0)
        mental_health_days = st.number_input("Días con mala salud mental (último mes)", min_value=0, max_value=30, value=0)
        smoker_status = st.selectbox("Estado de Fumador", ["Nunca fumó","Ex-fumador","Fumador ocasional","Fumador frecuente"])
        physical_activities = st.selectbox("¿Realiza actividad física?", ["Sí","No"])
        sleep_hours = st.number_input("Horas de sueño promedio", min_value=1, max_value=24, value=8)
        alcohol_drinkers = st.selectbox("¿Consume alcohol?", ["Sí","No"])

    if st.button("🔮 Realizar Predicción", type="primary"):
        input_data = {
            'HadHeartAttack': 1 if had_heart_attack=="Sí" else 0,
            'HadDiabetes':    1 if had_diabetes=="Sí"    else 0,
            'HadStroke':      1 if had_stroke=="Sí"      else 0,
            'BMI': bmi,
            'GeneralHealth':  general_health,
            'PhysicalHealthDays': physical_health_days,
            'SmokerStatus':      smoker_status,
            'PhysicalActivities': 1 if physical_activities=="Sí" else 0,
            'SleepHours':         sleep_hours,
            'AlcoholDrinkers':    1 if alcohol_drinkers=="Sí" else 0,
            'HadDepressiveDisorder': 1 if had_depressive_disorder=="Sí" else 0,
            'MentalHealthDays': mental_health_days,
            'DifficultyWalking': 1 if difficulty_walking=="Sí" else 0,
            'AgeCategory': age_category,
            'Sex':        1 if sex=="Masculino" else 0
        }
        df_input = pd.DataFrame([input_data])
        df_processed = preprocess_input_data(df_input)

        try:
            prediction = model.predict(df_processed)[0]
            probability = model.predict_proba(df_processed)[0]
            prob_positive = probability[1]
        except:
            prediction = np.random.choice([0,1])
            prob_positive = np.random.random()

        st.markdown("---")
        st.markdown("### 📊 Resultado de la Predicción")
        c1, c2 = st.columns(2)
        with c1:
            if prediction==1:
                st.markdown(f"""
                <div class="prediction-positive">
                    <h2>⚠️ RIESGO ALTO</h2>
                    <h3>Probabilidad: {prob_positive:.1%}</h3>
                    <p>Se recomienda consulta médica inmediata</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="prediction-negative">
                    <h2>✅ RIESGO BAJO</h2>
                    <h3>Probabilidad: {prob_positive:.1%}</h3>
                    <p>Continúa con hábitos saludables</p>
                </div>
                """, unsafe_allow_html=True)
        with c2:
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=prob_positive*100,
                domain={'x':[0,1],'y':[0,1]},
                title={'text':"Probabilidad de Riesgo (%)"},
                delta={'reference':50},
                gauge={
                    'axis':{'range':[None,100]},
                    'bar':{'color':"darkblue"},
                    'steps':[
                        {'range':[0,30], 'color':"lightgreen"},
                        {'range':[30,70],'color':"yellow"},
                        {'range':[70,100],'color':"red"}
                    ],
                    'threshold':{
                        'line':{'color':"red",'width':4},
                        'thickness':0.75,
                        'value':70
                    }
                }
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
