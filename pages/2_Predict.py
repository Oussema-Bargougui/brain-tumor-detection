# pages/2_Predict.py
import streamlit as st
from utils import load_vgg16_model, preprocess_image, predict
from PIL import Image
import plotly.graph_objects as go

language = st.session_state.get("language", "English")
model = load_vgg16_model()

st.markdown(f"<h2 style='text-align: center;'>🧠 {'Upload an MRI Image' if language == 'English' else 'Téléchargez une image IRM' if language == 'French' else 'تحميل صورة التصوير بالرنين المغناطيسي'}</h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose an image" if language == "English" else
    "Choisissez une image" if language == "French" else
    "اختر صورة", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    img_array = preprocess_image(uploaded_file)
    predicted_class, confidence = predict(model, img_array)

    st.markdown("---")
    st.markdown(f"<h3 style='text-align: center;'>✅ {'Prediction' if language == 'English' else 'Prédiction' if language == 'French' else 'التنبؤ'}: <span style='color: #4CAF50;'>{predicted_class}</span></h3>", unsafe_allow_html=True)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Confidence Level (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, 50], 'color': "lightcoral"},
                {'range': [50, 75], 'color': "gold"},
                {'range': [75, 100], 'color': "lightgreen"}
            ],
        }
    ))
    st.plotly_chart(fig, use_container_width=True)
