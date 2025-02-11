import streamlit as st
import os
import png_generator as pg
import svgs2ttf
import shutil
from PIL import Image
import streamlit.components.v1 as components

# SVG_to_TTF_convertor import start_process_ttf
def paths():
    for folder in ["input", "preprocessed", "cropped", "png", "pbm", "svg"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)

def save_uploaded_file(uploaded_file, save_folder):
    """Function to save the uploaded file to a specified folder."""
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    file_path = os.path.join(save_folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

# Save the uploaded file
def process_file(uploaded_file):
    if uploaded_file is not None:
        save_folder = os.path.join(os.getcwd(), "input/")
        saved_file_path = save_uploaded_file(uploaded_file, save_folder)
        pg.process_start(in_path=save_folder)
        st.success(f"File saved at: {saved_file_path}")

def display_svg_images_in_folder(folder_path, columns=3):
    """Function to display all SVG images in a specified folder."""
    if os.path.exists(folder_path):
        st.header("SVG Images in Folder")
        svg_files = [f for f in os.listdir(folder_path) if f.endswith('.svg')]
        selected_images = []
        
        select_all = st.checkbox("Select All", key="select_all")
        cols = st.columns(columns)
        col_idx = 0

        for svg_file in svg_files:
            with cols[col_idx]:
                svg_path = os.path.join(folder_path, svg_file)
                checked = st.checkbox(svg_file, key=svg_file, value=select_all)
                if checked:
                    selected_images.append(svg_file)
                with open(svg_path, "r") as f:
                    svg_content = f.read()
                components.html(svg_content, height=250, width=400)
            col_idx = (col_idx + 1) % columns
        
        if selected_images:
            if st.button("Delete Selected Files"):
                for svg_file in selected_images:
                    os.remove(os.path.join(folder_path, svg_file))
                st.success(f"Deleted {len(selected_images)} file(s)")
                st.rerun()

def main():
    # Allow the user to upload files
    st.title("Font Generator")

    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "JPG"])
    # Display basic file details
    if uploaded_file is not None:
        st.write("Filename:", uploaded_file.name)
        st.write("File type:", uploaded_file.type)
        st.write("File size:", uploaded_file.size, "bytes")
        
        if uploaded_file.type in ["image/png", "image/jpeg"]:
            st.image(uploaded_file)
        else:
            st.error("Error! Please upload a .jpg or .png image")
    else:
        st.error("Error! Please upload an image")
    
    # Button to trigger the file processing
    if st.button("Generate SVGs"):
        process_file(uploaded_file)
        paths()
    # Display all images in the folder
    display_svg_images_in_folder(os.path.join(os.getcwd(), "svg/"))
    
    if st.button("Generate TTF"):
        svgs2ttf.start_process_ttf("test.json")
        st.success("TTF file generated successfully")
        
        file_name = "tamilfonts.ttf"
        with open(file_name, 'rb') as file:
            font_data = file.read()
        
        st.title("Download TTF file")
        st.download_button(label="Download TTF file", data=font_data, file_name=file_name, mime="font/ttf")

if __name__ == "__main__":
    main()
