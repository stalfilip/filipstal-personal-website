import streamlit as st
import json
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
json_file = current_dir / "assets" / "logos.json"

# --- LOAD SOCIAL MEDIA LOGOS FROM JSON ---
with open(json_file) as f:
    logos_json = json.load(f)

def thick_line(color="white", size=1):
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
        width: 30px;
        # height: 20px;
        # border-radius: 50%;
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
    
def display_hero_section(profile_pic, DESCRIPTION, EMAIL):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(profile_pic, width=300)
        
    with col2:
        st.markdown("### **Filip Stål**")
        st.write(DESCRIPTION)
        st.write('\n')
        st.markdown(f"<div style='text-align: center;'>✉️ <a href='mailto:{EMAIL}'>Email me</a></div>", unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')

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

def display_education(logos_json):
    st.write('\n')
    st.write("#### Education")
    thick_line("black")
    st.write(f'<div class="company-name">{get_logo("KTH", logos_json, class_name="company-logo", type="misc")}<b>    KTH, Royal Institute of Technology</b></div>', unsafe_allow_html=True)
    st.write("*B.Sc Engineering Physics | M.Sc Machine Learning*")
    st.write("Stockholm | 2021-2026")
    st.write(
        """
        Engineering degree in Physics, with a master in computer science, Machine Learning.
        Current GPA: 4.7 / 5.0
        """
    )

def display_experience(logos_json):
    st.write('\n')
    # st.write("#### Experience")
    thick_line("black")
    
    # AP4
    st.write(f'<div class="company-name">{get_logo("AP4", logos_json, class_name="company-logo", type="misc")}<b>    AP4</b></div>', unsafe_allow_html=True)
    st.write('\n')
    st.write("*Strategic Allocation & Quantitative Analysis*")
    st.write("Stockholm | Summer 2024")
    st.write(
        """
        Summer internship as a software engineer at the funds Strategic Allocation & Quantitative Analysis division.
        
        Building on the funds quant platform, and also developed a data visualization tool."""
    )
    st.write('---')

    # Oxx
    st.write(f'<div class="company-name">{get_logo("OXX", logos_json, class_name="company-logo", type="misc")}<b>    Oxx</b></div>', unsafe_allow_html=True)
    st.write('\n')    
    st.write("*Visiting Associate*")
    st.write("Stockholm & London | Spring 2024")
    st.write(
        """
        Oxx is a b2b SaaS venture fund, currently investing in their second pan-European fund. I was part of their daily operation sourcing good companies, but also worked on a tech project regarding their internal data management.
        
        The tech project covered building a centralized data management system for the fund, which included data collection, cleaning, and visualization. I was the main developer on the project, and working closely with the investment team to ensure the system met their needs.
        """
    )
    st.write('---')

    # Evolante Engineering
    st.write(f'<div class="company-name">{get_logo("Evolante", logos_json, class_name="company-logo", type="misc")}<b>    Evolante Engineering</b></div>', unsafe_allow_html=True)
    st.write('\n')    
    st.write("*Software Engineer*")
    st.write("Stockholm | Sep 2023 – Present")
    blank_space(1)
    st.markdown(
        """
        **Evolante** is a sector agnostic consultancy firm focused on AI & Machine Learning solutions. [Read more](https://www.evolante.se/)
        """
    )
    
    st.markdown(
        """
        I've been involved in two projects: 
        
        -  Technical assistance at a swedish retail company, mostly focused on integrating their Shopify store with their internal systems. [Read about the project ](https://www.evolante.se/project/shopify-sync-och-integration)
        
        - Building a AI based search engine for a Stockholm based startup. The project included designing the arcitechure of the search engine, as well as building and deploying the API. 
        I was the head engineer on the project from our side, and was responsible for the technical decisions and the implementation of the project. I also worked closley with a project leader from our consultancy firm, and the developers at the startup.
        """)
    
    
    st.write('---')
    
    # Lovable
    st.write(f'<div class="company-name">{get_logo("Lovable", logos_json, class_name="company-logo", type="misc")}<b>    Lovable</b></div>', unsafe_allow_html=True)
    st.write('\n')    
    st.write("*Operations Contractor*")
    st.write("Stockholm | Oct 2023 – Feb 2024")
    
    st.markdown(
        """
        Code generation startup, powered by AI. I helped the co-founders with the daily operations regarding both the tech and the business side. As the first employee except the co-founders, I was involved in the early stages of releasing the first product to the public, including structuring the release on twitter product hunt and other platforms. Combined, the posts reached over a half a million people.
        
        - [Twitter Post](https://x.com/antonosika/status/1737113683392942237) - 450k+ views\n
        - [Product Hunt Post](https://www.producthunt.com/products/gptengineer-app/awards) - Product of the day, and of the week    
        """
    )
    st.write('---')

    # Ampfield
    st.write(f'<div class="company-name">{get_logo("Ampfield", logos_json, class_name="company-logo", type="misc")}<b>    Ampfield</b></div>', unsafe_allow_html=True)
    st.write('\n')    
    st.write("*Software Engineer Intern & Trading Supervisor*")
    st.write("Stockholm, Sweden | May 2022 – Sep 2023")
    st.write(
        """
        Ampfield is an algorithmic proprietary trading firm specializing in liquid currencies and agricultural futures. 
        I was en part-time trading supervisor and software developer, responsible for overseeing trading and developing software for their quant platform \n
        In the summer of 2023, I worked as a C++ developer building software for data collection and visualization. 
        """
    )
    st.write('---')

    # Boston Consulting Group
    st.write(f'<div class="company-name">{get_logo("BCG", logos_json, class_name="company-logo", type="misc")}<b>    Boston Consulting Group</b></div>', unsafe_allow_html=True)
    st.write('\n')    
    st.write("*Incoming Internship*")
    st.write("Stockholm, Sweden | November 2024")
    st.write(
        """
        Incoming internship at Boston Consulting Group.
        """
    )

def display_activities_and_diplomas(logos_json):
    st.write("#### Activities")
    thick_line("black")
    
    # KTH Finance Society
    st.write(f'<div class="company-name">{get_logo("KTHFS", logos_json, class_name="company-logo", type="academic")}<b>KTH Finance Society</b></div>', unsafe_allow_html=True)
    st.write("*Corporate Relations – Board Member*")
    st.write("Stockholm, Sweden | Feb 2023 – Present")
    st.write(
        """
        KTHFS is a student association aiming to narrow the gap between students and the industry. I recruited 40% of the consulting companies to our labour market fair 2023.
        """
    )
    st.write("---")
    
    # F.Capital Management
    st.write(f'<div class="company-name">{get_logo("F.CAP", logos_json, class_name="company-logo", type="academic")}<b>F.Capital Management</b></div>', unsafe_allow_html=True)
    st.write("*Head of Corporate Relations*")
    st.write("Stockholm, Sweden | Okt 2022 – Dec 2023")
    st.write(
        """
        F.Capital Management invest a share of the Physics Chapters liquid assets.
        """
    )
    st.write("---")

    # Fusion – Fysiksektionens arbetsmarknadsdag
    st.write(f'<div class="company-name">{get_logo("Fusion", logos_json, class_name="company-logo", type="academic")}<b>Fusion - Labour Market Fair</b></div>', unsafe_allow_html=True)
    st.write("*Account manager*")
    st.write("Stockholm, Sweden | 2022 & 2023")
    st.write(
        """
        Participated in the project group for Fusion 2023. My role evolved around the recruitment of companies for the fair. I recruited seven companies in total, and more than half of my sales resulted in a more extensive package.
        """
    )
    blank_space(3)
    st.write("#### Diplomas")
    thick_line("black")
    st.write("**Henrik Göransson's Sandviken scholarship fund**")
    st.write("*47 000 SEK*")
    st.write(
        """
        For great academic results during my bachelor's degree.
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

def display_skills():
    st.subheader("Miscellaneous")
    thick_line("black")

    skills = {
        "Software Development": [
            ("Backend", "Python, TypeScript, C++"),
            ("AI", "Finetune LLMs, embeddings, RAG"),
            ("Frontend", "TypeScript, JavaScript, React, Node.js, HTML, CSS"),
            ("App Development", "Streamlit, Next"),
            ("Testing", "K6, Pytest"),
            ("Database", "SQL, MongoDB, Firebase, Pinecone, Marqo, PostgreSQL, Strapi"),
            ("DevOps", "Docker, Git, Argo Workflows, CI/CD, CircleCI, Terraform"),
            ("Cloud", "AWS, GCP, Render"),
            ("Version Control", "Git, GitHub, GitLab"),
            ("Data Analysis", "Pandas, NumPy, Scikit-learn, Excel")
        ],
        "Languages": [
            ("Swedish", "Native"),
            ("English", "Fluent")
        ]
    }

    for category, items in skills.items():
        st.write(f"#### {category}")
        table = "| **Area** | **Description** |\n|----------|------------------|\n"
        table += "\n".join([f"| {area} | {description} |" for area, description in items])
        st.markdown(table)
        st.write("\n")