# pages/3_About.py
import streamlit as st

language = st.session_state.get("language", "English")

st.markdown(f"<h2>{'ℹ️ About This Project' if language == 'English' else 'ℹ️ À propos de ce projet' if language == 'French' else 'ℹ️ حول هذا المشروع'}</h2>", unsafe_allow_html=True)

st.write("""
This project was developed as part of a deep learning initiative for detecting brain tumors from MRI scans.
""" if language == "English" else
"""
Ce projet a été développé dans le cadre d'une initiative d'apprentissage profond pour détecter les tumeurs cérébrales à partir d'IRM.
""" if language == "French" else
"""
تم تطوير هذا المشروع كجزء من مبادرة التعلم العميق لاكتشاف أورام الدماغ من فحوصات التصوير بالرنين المغناطيسي.
""")

st.markdown("### 🔍 Technologies Used" if language == "English" else "### 🔍 Technologies utilisées" if language == "French" else "### 🔍 التقنيات المستخدمة")

st.write("- TensorFlow / Keras\n- Pre-trained **VGG16** model\n- Streamlit for the web interface")

st.markdown("### 👨‍💻 Author" if language == "English" else "### 🔍 Auteur" if language == "French" else "### 🔍 المؤلف" )
st.write("- **Oussema Bargougui**\n- [LinkedIn](https://www.linkedin.com/in/oussema-bargougui-63049825b/) | [GitHub](https://github.com/Oussema-Bargougui)")

st.markdown("### 🧠 Dataset")
st.write("- Brain Tumor MRI Dataset (Kaggle)")

st.markdown("### 💡 Goal")
st.write("Make AI-assisted diagnosis more accessible and interpretable to the public and medical professionals." if language == "English" else
         "Rendre le diagnostic assisté par l'IA plus accessible au public et aux professionnels de la santé." if language == "French" else
         "جعل التشخيص بمساعدة الذكاء الاصطناعي أكثر سهولة لعامة الناس وللمتخصصين في الرعاية الصحية.")
