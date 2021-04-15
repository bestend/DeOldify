import streamlit as st

from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *


@st.cache(allow_output_mutation=True)
def load_model():
    print('load model')
    device.set(device=DeviceId.GPU0)
    warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
    model = get_image_colorizer(artistic=True)
    return model


@st.cache(allow_output_mutation=True)
def convert(model, content_image, render_factor=35):
    filtered_image = model.filter.filter(
        content_image, content_image, render_factor=render_factor
    )
    return filtered_image