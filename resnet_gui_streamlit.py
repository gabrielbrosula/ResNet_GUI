import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub

# Image Upload
import requests
from PIL import Image
from io import BytesIO
import os

st.set_page_config(
    page_title = "ImageNet Classifiers",
    layout = "wide",
    menu_items={
        'About': "# This is a header. This is an *extremely cool app!"
    }
)

@st.cache
def set_default_img():
    """
    Sets default image as "African Grey 1.jpg"
    from the Test Images directory
    """
    default_img = Image.open("./Test Images/African Grey 1.jpg")
    return default_img

@st.cache
def get_tid_files():
    """
    Retrieves a list of all of the files in the Test Images Directory
    """
    tid_path = "./Test Images/"
    files = [f for f in os.listdir(tid_path) if os.path.isfile(os.path.join(tid_path, f))]

    return tid_path, files


img = set_default_img()

# Create sidebar for selecting an image
# Upload a file in the sidebar
with st.sidebar:

    # Selected image file
    img_file = None

    upload_opt = st.selectbox(
        "Upload image via: ",
        ["Local File Upload", "URL", "Test Images Directory"],
        key = "sb_upload_opt"
    )

    if upload_opt == "Local File Upload":
        # Upload a file with Local Upload
        img_file = st.file_uploader(
            "Upload Image", 
            type = ["png", "jpg", "jpeg"],
            key = "file_uploader_img"
        )

        if img_file is not None:
            img_file = Image.open(img_file)

    elif upload_opt == "URL":
        # Upload a file via URL
        img_file_url = st.text_input("Image URL")

        if not img_file_url == "":

            # Error handling for URLs
            try:
                response = requests.get(img_file_url)
            except requests.exceptions.HTTPError as e:
                st.error(f"HTTP Error: {e}")
            except requests.exceptions.ConnectionError as e:
                st.error(f"Connection Error: {e}")
            except requests.exceptions.RequestException as e:
                st.error(f"Unknown error: {e}")
            else:

                if (response.status_code >= 400 and response.status_code < 500):
                    st.error("Client error: {response.status_code}, {response.reason}")
                elif (response.status_code >= 500):
                    st.error("Server error: {response.status_code}, {response.reason}")
                else:
                    
                    # Handle successful HTTP Requests, but invalid image urls
                    try:
                        img_file = Image.open(BytesIO(response.content))
                    except Exception as e:
                        st.error(f"Error uploading image: {e}")
                    else:
                        st.success("Succesfully uploaded image!")


    elif upload_opt == "Test Images Directory":
        # Get a file in the Test Images Directory
        tid_path, files = get_tid_files()  

        img_file_name = st.selectbox(
            "Available images",
            files,
            key = "sb_tid",
            index = files.index("African Grey 1.jpg")
        )

        if img_file_name is not None:
            img_file = Image.open(f"{tid_path}{img_file_name}")

    if img_file is not None:
        img = img_file


st.subheader("ResNet_GUI")
st.write("An app to compare the performance of classifiers trained on the ImageNet dataset")
st.write("---")


with st.container():

    # Left column: Image
    l_col, r_col = st.columns(2)

    # Right column: Image classification plot

    with l_col:
        st.write("**Uploaded Image**")
        st.image(img)
    
    with r_col:
        st.write("**Analysis**")
    
    # Classification prediction

    # Prediction Confidence
