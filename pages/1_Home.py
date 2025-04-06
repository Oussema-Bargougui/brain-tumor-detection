# pages/1_Home.py
import streamlit as st
import random
import time
import base64

# Language detection
language = st.session_state.get("language", "English")

st.markdown(f"<h1 style='text-align: center;'>🧠 {'Brain Tumor Detection' if language == 'English' else 'Détection de Tumeur Cérébrale' if language == 'French' else 'كشف أورام الدماغ'}</h1>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center;'> {'Using Deep Learning (VGG16) for MRI Scan Classification' if language == 'English' else 'Utilisation de l\'apprentissage profond (VGG16) pour la classification des IRM' if language == 'French' else 'باستخدام التعلم العميق (VGG16) لتصنيف فحوصات التصوير بالرنين المغناطيسي'}</h4>", unsafe_allow_html=True)

# Centered Video
def get_base64_video(video_path):
    with open(video_path, 'rb') as video_file:
        video_bytes = video_file.read()
    encoded = base64.b64encode(video_bytes).decode()
    return encoded

video_base64 = get_base64_video("assets/video.mp4")

st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <video autoplay loop muted playsinline style="width: 80%; border-radius: 15px;">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown(f"### {'🤖 Project Overview' if language == 'English' else '🤖 Aperçu du Projet' if language == 'French' else '🤖 نظرة عامة على المشروع'}")

st.write("""
This web app uses a **pre-trained VGG16 deep learning model** to automatically detect brain tumors from **MRI scans**.
""" if language == "English" else
"""
Cette application utilise un **modèle VGG16 pré-entraîné** pour détecter automatiquement les tumeurs cérébrales à partir d'IRM.
""" if language == "French" else
"""
يستخدم هذا التطبيق **نموذج VGG16 المدرب مسبقًا** لاكتشاف أورام الدماغ تلقائيًا من خلال صور التصوير بالرنين المغناطيسي.
""")

st.markdown("---")
st.markdown("### 💡 Did You Know?" if language == "English" else "### 💡 Le Saviez-Vous ?" if language == "French" else "### 💡 هل كنت تعلم؟")

# Tips section
tips = [
    "🧠 MRI stands for Magnetic Resonance Imaging.",
    "🧬 Gliomas account for ~30% of all brain tumors.",
    "🏛️ VGG16 was developed by researchers at Oxford.",
    "🤖 AI can assist doctors, but doesn’t replace them!",
    "🔬 Early tumor detection increases survival rates by 70%.",
    "📈 Deep Learning models require millions of parameters.",
]

placeholder = st.empty()

while True:
    tip = random.choice(tips)
    placeholder.info(tip)
    time.sleep(1.5)
