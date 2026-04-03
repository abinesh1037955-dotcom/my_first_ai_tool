import streamlit as st
import google.generativeai as genai

# Setup the Page
st.set_page_config(page_title="AI Task Assistant", layout="centered")
st.title("🤖 My Professional AI Tool")
st.write("I can help you with coding, writing, or data tasks.")

# API Key Sidebar
st.sidebar.header("Setup")
api_key = st.sidebar.text_input("AIzaSyAzyYlslHpAqI1-INvwe7xtKpctItqLshg", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        
        user_input = st.text_area("Describe the task you want me to do:", height=150)
        
        if st.button("Generate Result"):
            if user_input:
                with st.spinner("Processing..."):
                    response = model.generate_content(user_input)
                    st.success("Task Completed!")
                    st.markdown("### Result:")
                    st.write(response.text)
            else:
                st.warning("Please enter a task first.")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("👈 Please enter your Gemini API Key in the sidebar to start.")
  
