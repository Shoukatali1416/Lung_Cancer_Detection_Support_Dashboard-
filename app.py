import streamlit as st
from modules import image_utils, explainability

st.set_page_config(page_title="Lung Cancer Support Dashboard", layout="wide")
st.title("Lung Cancer Detection Support Dashboard")

# Sidebar for uploading images
st.sidebar.header("Upload CT Scans")
uploaded_files = st.sidebar.file_uploader("Choose CT scan images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

if uploaded_files:
    st.header("Uploaded Images")
    for file in uploaded_files:
        st.image(file, caption=file.name, use_column_width=True)
        
        # Preprocessing example
        processed_img = image_utils.preprocess_image(file)
        st.image(processed_img, caption=f"Processed: {file.name}", use_column_width=True)
        
        # Placeholder for explainability heatmap
        heatmap_img = explainability.generate_heatmap(processed_img)
        st.image(heatmap_img, caption=f"Heatmap: {file.name}", use_column_width=True)
else:
    st.info("Please upload CT scan images to get started.")
