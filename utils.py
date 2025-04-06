# utils.py
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Preload class names
CLASS_NAMES = ['Glioma Tumor', 'Meningioma Tumor', 'No Tumor', 'Pituitary Tumor']

@st.cache_resource
def load_vgg16_model():
    model = load_model('vgg16_brain_mri_model.h5')
    return model

def preprocess_image(uploaded_file):
    img = Image.open(uploaded_file).convert('RGB')
    img = img.resize((224, 224))  # VGG16 expects 224x224
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Make batch of 1
    img_array /= 255.0  # Normalize to [0,1]
    return img_array

def predict(model, img_array):
    preds = model.predict(img_array, verbose=0)
    predicted_class = CLASS_NAMES[np.argmax(preds)]
    confidence = np.max(preds) * 100
    return predicted_class, confidence
