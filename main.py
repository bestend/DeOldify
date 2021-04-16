import streamlit as st
from PIL import Image

import colorizer

model = colorizer.load_model()

st.title('Deoldify')

uploaded_file = st.file_uploader("Choose a brain MRI ...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='원본 이미지', use_column_width=True)
    st.write("")
    # result = st.write("변환중 ...")
    filtered_image = colorizer.convert(model, image)

    st.image(filtered_image, caption='변환 이미지', use_column_width=True)
