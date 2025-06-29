import streamlit as st
from views.home import show as show_home
from views.prediction import show as show_pred
from views.batch_analysis import show as show_batch
from views.metrics import show as show_metrics
from views.info import show as show_info


st.set_page_config(
    page_title="Dashboard de Predicción Cardíaca",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyectar CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🧭 Navegación")
page = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["🏠 Inicio", "🔮 Predicción Individual", "📊 Análisis por Lotes", "📈 Métricas del Modelo", "ℹ️ Información"]
)

if page == "🏠 Inicio":
    show_home()
elif page == "🔮 Predicción Individual":
    show_pred()
elif page == "📊 Análisis por Lotes":
    show_batch()
elif page == "📈 Métricas del Modelo":
    show_metrics()
else:
    show_info()
