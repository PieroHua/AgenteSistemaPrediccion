import joblib
import pandas as pd
import streamlit as st

@st.cache_data
def load_model(model_path):
    """Cargar el modelo de Machine Learning"""
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None

@st.cache_data
def load_sample_data():
    """Cargar datos de ejemplo para testing"""
    sample_data = {
        'HadHeartAttack': [0, 1, 0, 1, 0],
        'HadDiabetes': [0, 1, 0, 0, 1],
        'HadStroke': [0, 0, 1, 0, 0],
        'BMI': [27.17, 32.5, 24.8, 29.3, 26.1],
        'GeneralHealth': [4, 2, 5, 3, 4],
        'PhysicalHealthDays': [0, 10, 2, 5, 0],
        'SmokerStatus': [0, 2, 1, 0, 1],
        'PhysicalActivities': [1, 0, 1, 1, 0],
        'SleepHours': [8, 6, 7, 8, 9],
        'AlcoholDrinkers': [1, 0, 1, 0, 1],
        'HadDepressiveDisorder': [1, 0, 0, 1, 0],
        'MentalHealthDays': [0, 15, 3, 8, 0],
        'DifficultyWalking': [0, 1, 0, 0, 1],
        'AgeCategory': [12, 8, 10, 6, 11],
        'Sex': [1, 0, 1, 0, 1]
    }
    return pd.DataFrame(sample_data)
