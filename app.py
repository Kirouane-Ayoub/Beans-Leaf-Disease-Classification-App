import streamlit as st 
import os 
from lib.utils import * 

st.set_page_config(page_title='Beans Leaf Disease Classifier', layout="wide")
st.header(":hand: Welcome To Beans Leaf Disease Classifier APP: ")
st.info("""
This is a Streamlit web application that utilizes a fine-tuned Vision Transformer (ViT) model 
to classify images of bean leaves into three categories: Angular Leaf Spot, Bean Rust, and Healthy. 
The model has been trained on the Beans leaf dataset, which contains images of diseased and healthy
bean leaves.""")
image_file = st.file_uploader("Upload your Image :")

if image_file : 
    if st.button("start") : 
        with st.spinner("this process may take some time .."): 
            current_directory = os.getcwd()
            img_name = image_file.name 
            img_path = f"{current_directory}/{img_name}"
            results = run(img_path)
            st.image(img_path)
            st.text(results[0] , results[1])
