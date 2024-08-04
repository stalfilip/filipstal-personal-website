import streamlit as st
import pandas as pd


def thick_line(color="black", size=1):
    colors = {
        "black": "#000000",
        "white": "#FFFFFF",
        "gray": "#808080"
    }
    selected_color = colors.get(color.lower(), "#000000")  # Default to black if color is not found
    st.markdown(f"<hr style='height:{size}px;border:none;background-color:{selected_color};' />", unsafe_allow_html=True)

def get_logo(platform, json_data, class_name="social-logo", type="misc"):
    try:
        info = json_data[type].get(platform, None)
        if info:
            return f'<a href="{info["link"]}" target="_blank"><img src="{info["logo"]}" class="{class_name}"></a>'
        else:
            return ""
    except KeyError:
        st.error(f"KeyError: '{type}' or '{platform}' not found in JSON data")
        return ""

def load_css(css_file):
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def apply_markdown_styling():
    st.markdown("""
    <style>
    .social-logo {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        margin-right: 10px;
    }
    .company-logo {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin-right: 10px;
    }
    .company-name {
        display: flex;
        align-items: center;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

def blank_space(size: int = 1):
    str = ""
    for _ in range(4 - size):
        str += '#'
    st.write(str)
    
def display_hero_section(profile_pic, NAME, DESCRIPTION, PDFbyte, resume_file, EMAIL, logos_json):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(profile_pic, width=300)
        
    with col2:
        st.markdown("### **Filip Stål**")
        st.write(DESCRIPTION)
        st.markdown(f"✉️ [Email me](mailto:{EMAIL})")
        st.download_button(
            label=" 📄 Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
            use_container_width=True,
        )
        
def write_markdown_centered(text):
    st.markdown(f"<div class='centered'>{text}</div>", unsafe_allow_html=True)
        

def display_logos(logos_json):
        blank_space(1)
        st.write('\n')
        misc_logos = logos_json.get("misc", {})
        cols_2 = st.columns(len(misc_logos))
        for index, platform in enumerate(misc_logos.keys()):
            with cols_2[index]:
                st.markdown(get_logo(platform, logos_json, class_name="misc-logo", type="misc"), unsafe_allow_html=True)        
        
        social_logos = logos_json.get("social", {})
        cols = st.columns(len(social_logos)+2)
        for index, platform in enumerate(social_logos.keys()):
            with cols[index+1]:
                st.markdown(get_logo(platform, logos_json, class_name="social-logo", type="social"), unsafe_allow_html=True)
        



def display_contact_info():
    st.subheader("Contact Information")
    st.write("Filip Johan Andreas Stål")
    st.write("Norra stationsgatan 99")
    st.write("070 233 06 87 | filip.johan.stal@gmail.com")

def display_education(logos_json):
    st.write('\n')
    st.subheader("Education")
    thick_line("black")
    st.write(f'<div class="company-name">{get_logo("KTH", logos_json, class_name="company-logo", type="misc")}<b>KTH, Royal Institute of Technology</b></div>', unsafe_allow_html=True)
    st.write("*B.Sc Engineering Physics*")
    st.write("Stockholm | 2021-2024")
    st.write(
        """
        Engineering degree in Physics, with a master in computer science, Machine Learning.
        Current GPA: 4.7 / 5.0
        """
    )
    st.write('---')
    st.write(f'<div class="company-name">{get_logo("KTH", logos_json, class_name="company-logo", type="misc")}<b>KTH, Royal Institute of Technology</b></div>', unsafe_allow_html=True)
    st.write("*M.Sc Machine Learning*")
    st.write("Stockholm | 2024-2026")
    st.write(
        """
        Engineering degree in Physics, with a master in computer science, Machine Learning.
        """
    )

def display_experience(logos_json):
    st.write('\n')
    st.subheader("Experience")
    thick_line("black")
    
    # AP4
    st.write(f'<div class="company-name">{get_logo("AP4", logos_json, class_name="company-logo", type="misc")}<b>AP4</b></div>', unsafe_allow_html=True)
    st.write("*Strategic Allocation & Quantitative Analysis*")
    st.write("Stockholm | Summer 2024")
    st.write(
        """
        Summer internship as a software engineer at the funds Strategic Allocation & Quantitative Analysis division.
        """
    )
    st.write('---')

    # Oxx
    st.write(f'<div class="company-name">{get_logo("OXX", logos_json, class_name="company-logo", type="misc")}<b>Oxx</b></div>', unsafe_allow_html=True)
    st.write("*Visiting Associate*")
    st.write("Stockholm & London | Summer 2024")
    st.write(
        """
        Oxx is a b2b SaaS venture fund, currently investing in their second pan-European fund. I was part of their daily operation sourcing good companies, but also worked on a tech project regarding their internal data management.
        """
    )
    st.write('---')

    # Evolante Engineering
    st.write(f'<div class="company-name">{get_logo("Evolante", logos_json, class_name="company-logo", type="misc")}<b>Evolante Engineering</b></div>', unsafe_allow_html=True)
    st.write("*Software Engineer*")
    st.write("Stockholm | Sep 2023 – Present")
    st.write(
        """
        Software engineer at a consultancy firm focused on Gen AI solutions for clients in various sectors. I’ve been head engineer at två projects.
        """
    )
    st.write('---')
    
    # Lovable
    st.write(f'<div class="company-name">{get_logo("Lovable", logos_json, class_name="company-logo", type="misc")}<b>Lovable</b></div>', unsafe_allow_html=True)
    st.write("*Software Engineer*")
    st.write("Stockholm | Sep 2023 – Present")
    st.write(
        """
        Software engineer at a consultancy firm focused on Gen AI solutions for clients in various sectors. I’ve been head engineer at två projects.
        """
    )
    st.write('---')

    # Ampfield
    st.write(f'<div class="company-name">{get_logo("Ampfield", logos_json, class_name="company-logo", type="misc")}<b>Ampfield</b></div>', unsafe_allow_html=True)
    st.write("*Software Engineer Intern & Trading Supervisor*")
    st.write("Stockholm, Sweden | May 2022 – Sep 2023")
    st.write(
        """
        Ampfield is an algorithmic proprietary trading firm specializing in liquid currencies and agricultural futures. I was en part-time trading supervisor and software developer, responsible for overseeing trading and developing software for data collection and analysis. In the summer of 2023, I undertook en 5-week internship as en C++ developer building software for data collection and visualization.
        """
    )
    st.write('---')

    # Boston Consulting Group
    st.write(f'<div class="company-name">{get_logo("BCG", logos_json, class_name="company-logo", type="misc")}<b>Boston Consulting Group</b></div>', unsafe_allow_html=True)
    st.write("*Incoming Internship*")
    st.write("Stockholm, Sweden | November 2024 | 2024")
    st.write(
        """
        Incoming internship at Boston Consulting Group.
        """
    )

def display_activities(logos_json):
    st.write('\n')
    st.subheader("Activities")
    
    # Lägg till en tjock linje under huvudtiteln
    thick_line("black")
    
    # KTH Finance Society
    st.write(f'<div class="company-name">{get_logo("KTHFS", logos_json, class_name="company-logo", type="misc")}<b>KTH Finance Society</b></div>', unsafe_allow_html=True)
    st.write("*Corporate Relations – Board Member*")
    st.write("Stockholm, Sweden | Feb 2023 – Present")
    st.write(
        """
        KTHFS is a student association aiming to narrow the gap between students and the industry. I recruited 40% of the consulting companies to our labour market fair 2023.
        """
    )
    st.write("---")
    
    # F.Capital Management
    st.write(f'<div class="company-name">{get_logo("F.CAP", logos_json, class_name="company-logo", type="misc")}<b>F.Capital Management</b></div>', unsafe_allow_html=True)
    st.write("*Head of Corporate Relations*")
    st.write("Stockholm, Sweden | Okt 2022 – Dec 2023 | 1 år 3 mån")
    st.write(
        """
        F.Capital Management invest a share of the Physics Chapters liquid assets.
        """
    )
    st.write("---")

    # Fusion – Fysiksektionens arbetsmarknadsdag
    st.write(f'<div class="company-name">{get_logo("Fusion", logos_json, class_name="company-logo", type="misc")}<b>Fusion - Labour Market Fair</b></div>', unsafe_allow_html=True)
    st.write("*Event Manager - Fusion 2022*")
    st.write("Stockholm, Sweden | Nov 2021 – Mars 2022 | 5 mån")
    st.write(
        """
        Fusion is a labor market fair for physics & mathematics students @KTH. My post involved talking to companies and planning events prior to the fair. I mostly hosted lunch lectures, both digital and in-person events.
        """
    ) 
    st.write("---")
    st.write("*Account Manager - Fusion 2023*")
    st.write("Stockholm, Sweden | Maj 2022 – Jan 2023 | 9 mån")
    st.write(
        """
        Participated in the project group for Fusion 2023. My role evolved around the recruitment of companies for the fair. I recruited seven companies in total, and more than half of my sales resulted in a more extensive package.
        """
    ) 

def display_skills():
    st.subheader("Overview")
    thick_line("black")

    # Mjukvaruutveckling
    st.write("#### Software Development")
    st.markdown("""
    <table style="width:100%">
        <tr>
            <th style="text-align:left; background-color:black; color:white;">Area</th>
            <th style="text-align:left; background-color:black; color:white;">Description</th>
        </tr>
        <tr>
            <td>Backend</td>
            <td>Python, TypeScript, C++</td>
        </tr>
        <tr>
            <td>AI</td>
            <td>Finetune LLMs, embeddings, RAG</td>
        </tr>
        <tr>
            <td>Frontend</td>
            <td>Typescript, JavaScript, React, Node.js, HTML, CSS, Streamlit</td>
        </tr>
        <tr>
            <td>Database</td>
            <td>SQL, MongoDB, Pinecone, PostgreSQL, Firebase</td>
        </tr>
        <tr>
            <td>DevOps</td>
            <td>Docker, Git, Argo Workflows, CI/CD</td>
        </tr>
        <tr>
            <td>Version Control</td>
            <td>Git, GitHub, GitLab</td>
        </tr>
        <tr>
            <td>Data Analysis</td>
            <td>Pandas, NumPy, Scikit-learn, TensorFlow, Excel</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
    # Språk
    st.write("#### Languages")
    st.markdown("""
    <table style="width:50%">
        <tr>
            <th style="text-align:left; background-color:black; color:white;">Language</th>
            <th style="text-align:left; background-color:black; color:white;">Proficiency</th>
        </tr>
        <tr>
            <td>Swedish</td>
            <td>Native</td>
        </tr>
        <tr>
            <td>English</td>
            <td>Fluent</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
def display_diplomas():
    st.write('###')
    st.subheader("Diplomas")
    thick_line("black")
    st.write("**Henrik Göransson's Sandviken scholarship fund**")
    st.write("47 000 SEK")
    st.write(
        """
        For great academic results and engagement during my bachelor's degree.
        """
    )
    st.write('---')
    st.write("**Mathematics - Falun Educational Fund**")
    st.write("2250 SEK - Highest amount in the class of 2020")
    st.write(
        """
        For his engagement in mathematics. Filip tackles hard problems with unconventional and independent solutions.
        """
    )
    st.write('---')
    st.write("**Ljungsberg Scolarship Fund**")
    st.write("20 000 SEK")
    st.write(
        """
        For his engagement in mathematics. Filip tackles hard problems with unconventional and independent solutions.
        """
    )
    st.write('---')
