from pathlib import Path
import streamlit as st
import json
from utils import display_education, display_experience, display_activities_and_diplomas, apply_markdown_styling, blank_space

# Set page configuration for wide layout
st.set_page_config(layout="wide", page_icon=":book:")
st.write("#### Experience")
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
    


banner_url = "https://images.unsplash.com/photo-1508189860359-777d945909ef?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
display_banner(banner_url)

# Write experience section

blank_space(size=100)
# st.write("---")

st.write("During my tenure at KTH, I've been involved in various projects and activities, ranging from freelancing as a software engineer to several internships at well-known companies.")
st.write("##")


# # Display education, experience, and activities/diplomas
# display_education(logos_json)       
# st.write("##")

display_experience(logos_json)
st.write("##")

display_activities_and_diplomas(logos_json)
