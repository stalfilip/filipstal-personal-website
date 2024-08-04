import streamlit as st
from .Filip import profile_pic, NAME, DESCRIPTION, PDFbyte, resume_file, EMAIL, logos_json

def main_content():
    st.markdown("###")
    st.write("---")

    # --- Kontaktinformation ---
    st.write('\n')
    st.subheader("Contact Information")
    st.write("Filip Johan Andreas Stål")
    st.write("Norra stationsgatan 99")
    st.write("070 233 06 87 | filip.johan.stal@gmail.com")

    # --- EDUCATION ---
    st.write('\n')
    st.subheader("Education")
    st.write("---")
    st.write("**KTH, Royal Institute of Technology**")
    st.write("Stockholm")
    st.write("B.Sc Engineering Physics | 2021-2024")
    st.write("M.Sc Machine Learning | 2024-2026")
    st.write(
        """
        Engineering degree in Physics, with a master in computer science, Machine Learning.
        Current GPA: 4.7 / 5.0
        """
    )

    # --- EXPERIENCE ---
    st.write('\n')
    st.subheader("Experience")
    st.write("---")

    st.write(f'<div class="company-name">{get_logo("AP4", logos_json, class_name="company-logo")}<b>AP4</b></div>', unsafe_allow_html=True)
    st.write("Stockholm")
    st.write("Strategic Allocation & Quantitative Analysis | Summer 2024")
    st.write(
        """
        Summer internship as a software engineer at the funds Strategic Allocation & Quantitative Analysis division.
        """
    )

    st.write('\n')
    st.write(f'<div class="company-name">{get_logo("Oxx", logos_json, class_name="company-logo")}<b>Oxx</b></div>', unsafe_allow_html=True)
    st.write("Stockholm & London")
    st.write("Visiting Associate | Summer 2024")
    st.write(
        """
        Oxx is a b2b SaaS venture fund, currently investing in their second pan-European fund. I was part of their daily operation sourcing good companies, but also worked on a tech project regarding their internal data management.
        """
    )

    st.write('\n')
    st.write(f'<div class="company-name">{get_logo("Evolante Engineering", logos_json, class_name="company-logo")}<b>Evolante Engineering</b></div>', unsafe_allow_html=True)
    st.write("Stockholm")
    st.write("Software Engineer | Sep 2023 – Present")
    st.write(
        """
        Software engineer at a consultancy firm focused on Gen AI solutions for clients in various sectors. I’ve been head engineer at two projects.
        """
    )

    st.write('\n')
    st.write(f'<div class="company-name">{get_logo("Ampfield", logos_json, class_name="company-logo")}<b>Ampfield</b></div>', unsafe_allow_html=True)
    st.write("Stockholm, Sweden")
    st.write("Software Engineer Intern & Trading Supervisor | May 2022 – Sep 2023")
    st.write(
        """
        Ampfield is an algorithmic proprietary trading firm specializing in liquid currencies and agricultural futures. I was a part-time trading supervisor and software developer, responsible for overseeing trading and developing software for data collection and analysis. In the summer of 2023, I undertook a 5-week internship as a C++ developer building software for data collection and visualization.
        """
    )

    st.write('\n')
    st.write(f'<div class="company-name">{get_logo("Boston Consulting Group", logos_json, class_name="company-logo")}<b>Boston Consulting Group</b></div>', unsafe_allow_html=True)
    st.write("Stockholm, Sweden")
    st.write("Incoming Internship – November 2024 | 2024")
    st.write(
        """
        Incoming internship at Boston Consulting Group.
        """
    )

    # --- ACTIVITIES ---
    st.write('\n')
    st.subheader("Activities")
    st.write("---")

    st.write("**KTH Finance Society**")
    st.write("Stockholm, Sweden")
    st.write("Corporate Relations – Board Member | Feb 2023 – Present")
    st.write(
        """
        KTHFS is a student association aiming to narrow the gap between students and the industry. I recruited 40% of the consulting companies to our labour market fair 2023.
        """
    )

    # --- SKILLS ---
    st.write('\n')
    st.subheader("Skills")
    st.write("---")

    st.write(
        """
        - Languages: Fluent in Swedish (native) & English
        - Programming Languages:
        - **TypeScript & JavaScript**: Designing APIs, Cloud, AWS, GCP, AI-solutions
        - **Python**: Designing APIs, Cloud, AWS, GCP, LangChain, LLMs
        - **C++**: Database programming, API callings, FinTech
        - **Excel / Sheets**
        """
    )

    # --- DIPLOMAS ---
    st.write('\n')
    st.subheader("Diplomas")
    st.write("---")

    st.write("**Academic Diploma - Mathematics**")
    st.write("Falun, Sweden")
    st.write("Lugnetgymnasiet, Falun Educational Fund | 2020")
    st.write("2250 SEK - Highest amount in the class of 2020")
    st.write(
        """
        For his engagement in mathematics. Filip tackles hard problems with unconventional and independent solutions.
        """
    )
