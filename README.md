# 🧠 Brain Tumor Detection using Deep Learning

---

## 📚 Project Overview

This project presents an **AI-powered Brain Tumor Detection System** built using **Deep Learning (VGG16)** and **Streamlit**.  
It allows users to upload **MRI scans** and instantly predict the presence and type of brain tumor through an intuitive web interface.

---

## 🚀 Key Features

- 🧠 **MRI Image Upload** and Instant Tumor Prediction
- 📈 **Confidence Gauge** to show model certainty
- 🌐 **Multilingual Support**: English, French, Arabic
- 🎥 **Background Video + Smooth Animations**
- 🖼️ **Elegant and Responsive UI**
- 🛡️ **Pre-trained VGG16 Model** for high-accuracy classification
- 🌟 **Built fully in Python with TensorFlow and Streamlit**

---

## 🏗️ Project Structure

├── assets/ │ ├── background.jpg │ ├── logo.png │ └── video.mp4 ├── pages/ │ ├── 1_Home.py │ ├── 2_Predict.py │ └── 3_About.py ├── app.py ├── utils.py ├── requirements.txt ├── vgg16_brain_mri_model.h5 # (not uploaded here due to GitHub file size limits) └── brain_tumor_detection.ipynb # Jupyter Notebook

---

## 🧠 Model

We use **Transfer Learning** with a pre-trained **VGG16** model fine-tuned for MRI brain tumor images.

| Tumor Types Detected | ✅ |
|:---------------------|:--|
| Glioma Tumor          | ✅ |
| Meningioma Tumor      | ✅ |
| Pituitary Tumor       | ✅ |
| No Tumor              | ✅ |

> **Note**:  
> The model (`vgg16_brain_mri_model.h5`) is not uploaded to GitHub because it's larger than 25MB.  

---

