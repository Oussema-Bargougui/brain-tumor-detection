# app.py
import streamlit as st
from pathlib import Path
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

# Set page configuration
st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="wide",
)

# Initialize language at startup
if "language" not in st.session_state:
    st.session_state["language"] = "English"

# Sidebar
with st.sidebar:
    st.image("assets/logo.png", width=150)
    st.title("Brain Tumor Detection 🧠")
    st.markdown("---")

    # Language Selector
    language = st.selectbox(
        "🌐 Select Language",
        ("English", "French", "Arabic")
    )
    st.session_state["language"] = language

    st.markdown("**🧠 AI-powered MRI Brain Tumor Detection System**")
    st.markdown("**>> \"Saving lives through deep learning.\"**")
    st.markdown("---")
    st.caption("Made with ❤️ by Oussema Bargougui")

# Background
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: url("assets/background.jpg");
            background-size: cover;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Main Content
col1, col2 = st.columns([4, 1])

with col1:
    if st.session_state["language"] == "French":
        st.title("🔗 Naviguez depuis la barre latérale")
        st.write("Bienvenue ! Utilisez la barre latérale pour naviguer dans l'application.")
    elif st.session_state["language"] == "Arabic":
        st.title("🔗 تنقل من الشريط الجانبي")
        st.write("مرحبًا! استخدم الشريط الجانبي للتنقل عبر التطبيق.")
    else:
        st.title("🔗 Navigate from the Sidebar")
        st.write("Welcome! Please use the sidebar to navigate through the app.")

with col2:
    image = Image.open("assets/background.jpg")
    st.image(image, width=200)

st.markdown("---")
st.markdown("<h3 style='text-align: center;'>🚀 Get Involved</h3>", unsafe_allow_html=True)

with st.container():
    # Dynamic full paragraph based on language
    message = (
        "**Help us advance brain tumor detection!**  \n"
        "If you're a medical professional, data scientist, or just passionate about AI in healthcare, we would love to hear from you."
        if st.session_state["language"] == "English" else
        "**Aidez-nous à faire progresser la détection des tumeurs cérébrales !**  \n"
        "Si vous êtes un professionnel de la santé, un data scientist ou simplement passionné par l'IA en santé, nous serions ravis d'avoir de vos nouvelles."
        if st.session_state["language"] == "French" else
        "**ساعدنا في تطوير الكشف عن أورام الدماغ!**  \n"
        "إذا كنت متخصصًا طبيًا أو عالم بيانات أو شغوفًا بالذكاء الاصطناعي في الرعاية الصحية، يسعدنا التواصل معك."
    )

    st.info(message, icon="💬")


    if st.button("📩 Contact Us" if st.session_state["language"] == "English" else
                 "📩 Contactez-nous" if st.session_state["language"] == "French" else
                 "📩 تواصل معنا"):
        st.success("You can contact us at: **Ooussema.Bargougui@esprit.tn**")
