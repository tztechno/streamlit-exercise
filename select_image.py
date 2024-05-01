
import streamlit as st
from PIL import Image

st.title('Selecct Image')

uploaded_file = st.file_uploader("Selecct Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded", use_column_width=True)

