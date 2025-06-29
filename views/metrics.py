import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def show():
    st.markdown("### 📈 Métricas de Rendimiento del Modelo")

    metrics = {
        'Accuracy': 0.87,
        'Precision': 0.84,
        'Recall': 0.89,
        'F1-Score': 0.86
    }

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("🎯 Accuracy", f"{metrics['Accuracy']:.2%}", "2.3%")
    c2.metric("🔍 Precision", f"{metrics['Precision']:.2%}", "1.8%")
    c3.metric("📊 Recall", f"{metrics['Recall']:.2%}", "3.1%")
    c4.metric("⚖️ F1-Score", f"{metrics['F1-Score']:.2%}", "2.7%")

    fig_metrics = go.Figure(data=[
        go.Bar(x=list(metrics.keys()), y=list(metrics.values()),
               marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ])
    fig_metrics.update_layout(title="Métricas de Rendimiento del Modelo",
                              yaxis_title="Puntuación", xaxis_title="Métrica")
    st.plotly_chart(fig_metrics, use_container_width=True)

    st.markdown("#### 🔄 Matriz de Confusión")
    confusion_data = np.array([[850,95],[75,680]])
    fig_confusion = px.imshow(
        confusion_data,
        text_auto=True,
        title="Matriz de Confusión",
        labels=dict(x="Predicción", y="Real"),
        x=['Sin Riesgo','Con Riesgo'],
        y=['Sin Riesgo','Con Riesgo']
    )
    st.plotly_chart(fig_confusion, use_container_width=True)
