import streamlit as st
from PIL import Image
from vision_engine import analyze_image

st.title("AI Surveillance Image Analyzer")

uploaded_file = st.file_uploader("Upload CCTV Image", type=["png","jpg","jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded CCTV Frame")

    if st.button("Analyze Scene"):

        with st.spinner("Analyzing..."):

            report = analyze_image(image)

        st.subheader("AI Security Report")

        st.write(report)