from pathlib import Path
import streamlit as st
from PIL import Image
import json
from utils import get_logo, load_css, display_hero_section, display_contact_info, display_education, display_experience, display_activities, display_skills, display_diplomas, apply_markdown_styling, thick_line, blank_space

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile.png"
json_file = current_dir / "assets" / "logos.json"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Filip Stål"
PAGE_ICON = ":wave:"
NAME = "Filip Stål"

DESCRIPTION = """
Physics student with a passion for software & finance.

During my tenure at KTH, I've been involved in various projects and activities, ranging from free lancing as software engineer to being a part of the student union.
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
    st.write("####")
    display_skills()
    blank_space()
    thick_line()

    with st.expander(label="Academic Record", expanded=False):
        display_education(logos_json)       
        display_diplomas()

    with st.expander(label="Experience"):
        display_experience(logos_json)
        
    with st.expander(label="Activities"):
        display_activities(logos_json)
        
    # display_skills()

if __name__ == "__main__":
    main()
