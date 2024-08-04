from pathlib import Path
import streamlit as st
from PIL import Image
import json

from utils import get_logo, load_css, display_hero_section, display_logos, display_skills, apply_markdown_styling, thick_line, blank_space

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Filipstal.pdf"
profile_pic_path = current_dir / "assets" / "profile.png"
json_file = current_dir / "assets" / "logos.json"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Filip Stål"
PAGE_ICON = ":coffee:"
NAME = "Filip Stål"

DESCRIPTION = """
Physics student with a passion for software and finance.

During my tenure at KTH, I've been involved in various projects and activities, ranging from freelancing as a software engineer to several internships at well-known companies.
"""

EMAIL = "filip.johan.stal@gmail.com"

def main():
    
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")

    # --- LOAD CSS, PDF & PROFILE PIC ---
    load_css(css_file)
    apply_markdown_styling()
    
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        
    profile_pic = Image.open(profile_pic_path)

    # --- LOAD SOCIAL MEDIA LOGOS FROM JSON ---
    with open(json_file) as f:
        logos_json = json.load(f)

    # --- Display Sections ---
    display_hero_section(profile_pic, NAME, DESCRIPTION, PDFbyte, resume_file, EMAIL, logos_json)
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        display_logos(logos_json)
        
    st.write("####")
    display_skills()
    blank_space()
    thick_line()

if __name__ == "__main__":
    main()
