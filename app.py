# Import convention
import streamlit as st
import pandas as pd
import torch
import glob
import PIL
from PIL import Image

st.header('Thytra (Thyroid Ultrasound Image Classification for Disease Diagnosis)')

st.sidebar.write('### Enter image to classify')
option = st.sidebar.radio('', ['Use a validation image', 'Use your own image'])
valid_images = glob.glob('images/test/*')
valid_images.sort()

if option == 'Use a validation image':
    st.sidebar.write('### Select a validation image')
    fname = st.sidebar.selectbox('', valid_images)

else:
    st.sidebar.write('### Select an image to upload')
    fname = st.sidebar.file_uploader('',
                                     type=['png', 'jpg', 'jpeg'],
                                     accept_multiple_files=False)
    
    if fname is None:
        fname = valid_images[0]
img = PIL.Image.open(fname)