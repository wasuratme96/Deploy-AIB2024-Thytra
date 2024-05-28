# Import convention
import streamlit as st
import pandas as pd
import glob
import PIL
from PIL import Image
from utils.pipeline import thyroid_image_classification

st.header('Thytra (Thyroid Ultrasound Image Classification for Disease Diagnosis)')
classifier = thyroid_image_classification(model_name="agent593/Thyroid-Ultrasound-Image-Classification-ViTModel")
st.sidebar.write('### Enter image to classify')
option = st.sidebar.radio('', ['Use a validation image', 'Use your own image'])
valid_images = glob.glob('data/test/*')
valid_images.sort()

if option == 'Use a validation image':
    st.sidebar.write('### Select a validation image')
    fname = st.sidebar.selectbox('', valid_images)
    if fname:
        image = Image.open(fname)
        st.sidebar.image(image)
        st.session_state['result'] = image

else:
    st.sidebar.write('### Select an image to upload')
    fname = st.sidebar.file_uploader('',
                                     type=['png', 'jpg', 'jpeg'],
                                     accept_multiple_files=False)
    if fname:
        image = Image.open(fname)
        st.sidebar.image(image)
        st.session_state['result'] = image
if st.session_state['result']:
    st.image(st.session_state['result'])
    st.text(classifier(st.session_state['result']))