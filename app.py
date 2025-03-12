import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import os

# Load environment variables
load_dotenv()

# Import from our modules
from src.helper import get_gemini_response
from src.prompt import prompt

# Set up the Streamlit interface
st.set_page_config(page_title="Health Advisor Friend")
st.header("Health Advisor Friend")

# Upload image functionality
uploaded_file = st.file_uploader("Upload an image....", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)

# Analysis button
submit = st.button("Tell me about the dish I am having now: ")

if submit:
    if image is not None:
        with st.spinner("Analyzing the image..."):
            # Get response using the imported function and prompt
            response = get_gemini_response(prompt, image)
            st.header("The response is:")
            st.write(response)
    else:
        st.error("Please upload an image first")