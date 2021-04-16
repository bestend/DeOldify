import streamlit as st

from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *
from utils import download

download("https://download.pytorch.org/models/resnet34-333f7ec4.pth", "resnet34-333f7ec4.pth",
         target_dir=os.path.expanduser('~/.cache/torch/hub/checkpoints/'))
download("https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth", "ColorizeArtistic_gen.pth",
         target_dir='models')


@st.cache(allow_output_mutation=True)
def load_model():
    print('load model')
    device.set(device=DeviceId.GPU0)
    warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

    model = get_image_colorizer(artistic=True)
    #model = get_image_colorizer(artistic=False)
    return model


@st.cache(allow_output_mutation=True)
def convert(model, content_image, render_factor=15):
    filtered_image = model.filter.filter(
        content_image, content_image, render_factor=render_factor
    )
    return filtered_image
