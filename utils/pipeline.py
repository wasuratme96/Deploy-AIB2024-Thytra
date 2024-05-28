from transformers import pipeline
import streamlit as st

@st.cache_data
def thyroid_image_classification(model_name):
    classifier = pipeline("image-classification", model=model_name)
    return classifier