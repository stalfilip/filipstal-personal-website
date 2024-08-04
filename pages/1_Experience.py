from pathlib import Path
import streamlit as st
import json
from utils import display_education, display_experience, display_activities_and_diplomas, apply_markdown_styling

json_file = "assets/logos.json"
apply_markdown_styling()

with open(json_file) as f:
    logos_json = json.load(f)

st.write("## Experience")
st.write("---")
st.write("During my tenure at KTH, I've been involved in various projects and activities, ranging from freelancing as a software engineer to several internships at well-known companies.")
st.write("###")

display_education(logos_json)       
st.write("####")

display_experience(logos_json)
st.write("####")

display_activities_and_diplomas(logos_json)