from pathlib import Path
import streamlit as st
from PIL import Image
import json
import io

from utils import logos_json, display_education, get_logo, load_css, display_logos, display_skills, apply_markdown_styling, thick_line, blank_space

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Filipstal.pdf"
profile_pic_path = current_dir / "assets" / "profilbild.png"
json_file = current_dir / "assets" / "logos.json"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Filip Stål"
PAGE_ICON = ":earth_americas:"
NAME = "Filip Stål"

DESCRIPTION = """
Physics student with a passion for software and finance.

During my tenure at KTH, I've been involved in various projects and activities, ranging from freelancing as a software engineer to several internships at well-known companies.
"""

EMAIL = "filip.johan.stal@gmail.com"

@st.cache_resource
def load_profile_pic():
    with open(profile_pic_path, "rb") as image_file:
        return image_file.read()

def display_hero_section(profile_pic_bytes, description, email):
    col1, space, col2 = st.columns([1, 0.2, 1.2])
    with col1:
        # 30 px blank space
        st.markdown("<div style='height:5px;'></div>", unsafe_allow_html=True)
        st.image(profile_pic_bytes, use_column_width=True)
    with space:
        st.empty()
    with col2:
        st.title("Filip Stål")
        st.write(description)
        st.write(f"📫 {email}")

def main():
    
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")

    # Load CSS only once
    load_css(css_file)
    apply_markdown_styling()
    
    # Use cached function to load profile picture
    profile_pic_bytes = load_profile_pic()

    # --- Display Sections ---
    display_hero_section(profile_pic_bytes, DESCRIPTION, EMAIL)
    
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        display_logos(logos_json)
        
    display_education(logos_json=logos_json)
        
    st.write("####")
    display_skills()

if __name__ == "__main__":
    main()