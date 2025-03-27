import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["genai_api_key"])

st.set_page_config(page_title="Translator Botz", page_icon="🌍", layout="centered")


st.sidebar.title("🌐 Select Language")
language = st.sidebar.selectbox(
    "Choose a language to translate into:",
    ['English', 'Spanish', 'Mandarin Chinese', 'French', 'Arabic', 'Portuguese', 'Russian', 'German', 'Hindi', 'Japanese']
)

# Main Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 Translator Botz</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'>Your AI-powered language translator</h5>", unsafe_allow_html=True)
st.divider()

# Input and translation button in a layout
col1, col2 = st.columns([3, 1])

with col1:
    prompt = st.text_area("✍️ Enter the text you want to translate:", height=150)

with col2:
    st.write("")
    st.write("")
    gptbutton = st.button("🚀 Translate", use_container_width=True)

st.divider()

# Translation process
if gptbutton:
    with st.spinner("🔄 Translating... Please wait."):
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        response = model.generate_content(f"Translate the following text into {language}:\n{prompt}")
        st.snow()
        st.success("✅ Translation Complete!")

        st.markdown("### 🔹 Translated Text:")
        st.markdown(f"""
            <div style='background-color:#2e2d2d;
                        padding:15px;
                        border-radius:10px;
                         font-size:18px;
                        border: 1px solid #ccc;
                        color: white;'>
                {response.text}
            </div>
            """, unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>🌎 Powered by AI | Developed with ❤️ using Streamlit</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Contact me",unsafe_allow_html=True) 
st.markdown("""
            <div style="display: flex; gap: 15px;justify-content: center; align-items: center;">
            <a href="https://www.linkedin.com/in/neil-parkhe/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" , width="20 px" >
            </a>
            <a href="https://github.com/Neil-05" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" , width="20 px" >
            </a>
            </div>
            """,
            unsafe_allow_html=True
               
)



