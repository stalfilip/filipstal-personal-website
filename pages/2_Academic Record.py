import streamlit as st
import json
from utils import display_activities_and_diplomas, apply_markdown_styling, blank_space, thick_line

# Set page configuration for wide layout
st.set_page_config(layout="wide", page_icon=":book:")
st.write("#### Academic Record")
st.write("---")
# Load JSON file with logos
json_file = "assets/logos.json"
apply_markdown_styling()

with open(json_file) as f:
    logos_json = json.load(f)


def display_banner(image_url):
    st.markdown(
        f"""
        <style>
        .banner {{
            width: 100%;
            height: 40vh; /* Adjust this value as needed for your banner's height relative to viewport height */
            object-fit: cover;
            object-position: bottom; /* Ensures the bottom part of the image is always visible */
        }}
        </style>
        <img src="{image_url}" class="banner">
        """,
        unsafe_allow_html=True
    )
    


banner_url = "https://images.unsplash.com/photo-1653463174231-3911539cfdd9?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
display_banner(banner_url)

# Write experience section

blank_space(size=100)
# st.write("---")

st.write("During my academic career, I've been involved in various extra curricular activities and have received several diplomas.")
st.write("##")

display_activities_and_diplomas(logos_json)
st.write("##")

