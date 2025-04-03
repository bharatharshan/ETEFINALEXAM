from PIL import Image
import io
import streamlit as st
import os

# Directory to store images
IMAGE_DIR = "uploaded_images"

def process_images(uploaded_file):
    # Process the uploaded image
    image = Image.open(uploaded_file)
    # Example processing: convert to grayscale
    processed_image = image.convert("L")
    return processed_image

def save_image(uploaded_file, day):
    # Save the uploaded image to the directory
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    image_path = os.path.join(IMAGE_DIR, f"{day}_{uploaded_file.name}")
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return image_path

def display_image_gallery(day):
    # Display images for the selected day
    st.subheader(f"Image Gallery for Day {day}")
    for filename in os.listdir(IMAGE_DIR):
        if filename.startswith(f"{day}_"):
            image_path = os.path.join(IMAGE_DIR, filename)
            st.image(image_path, caption=filename)

def custom_image_processing(image_path, operation):
    # Apply custom image processing based on the selected operation
    image = Image.open(image_path)
    if operation == "Grayscale":
        return image.convert("L")
    elif operation == "Resize":
        return image.resize((100, 100))  # Example resizing
    return image
