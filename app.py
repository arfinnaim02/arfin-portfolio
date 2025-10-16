import streamlit as st
from streamlit_lottie import st_lottie
import requests
import plotly.express as px
import pandas as pd
import time

# -------------------
# LOAD EXTERNAL CSS
# -------------------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# -------------------
# PAGE CONFIG
# -------------------
st.set_page_config(page_title="Arfin Naim Portfolio", page_icon="💻", layout="wide")

# -------------------
# HELPER FUNCTIONS
# -------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def animated_counter(label, count, duration=2):
    placeholder = st.empty()
    for i in range(count+1):
        time.sleep(duration/count)
        placeholder.markdown(f"<div class='counter'>{i}</div><p>{label}</p>", unsafe_allow_html=True)

# -------------------
# HERO SECTION
# -------------------
st.markdown("<div class='hero'><h1>Hi, I'm Arfin Naim</h1><h3>I transform data into actionable insights</h3></div>", unsafe_allow_html=True)
st.markdown("---")

# -------------------
# ABOUT ME
# -------------------
st.header("About Me")

# Main columns: Profile Image + Content
col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/profile.jpg", width=420, caption="Arfin Naim", use_container_width=False)

with col2:
    col_edu, col_work = st.columns(2)

    with col_edu:
        st.markdown("### 🎓 Education")
        st.markdown("""
        - **Master of Science (MSc)** in Applied Statistics & Data Science, Jahangirnagar University — *Enrolled 2027*  
        - **Bachelor of Science (BSc)** in Computer Communication Engineering, International Islamic University Chittagong — *CGPA: 3.606 (2023)*  
        - **HSC** in Science, Bangladesh Naubahini College, Chittagong — *GPA: 3.5/5 (2019)*  
        - **SSC** in Science, Government Muslim High School — *GPA: 5/5 (2017)*
        """)

    with col_work:
        st.markdown("### 💼 Work Experience")
        st.markdown("""
**Data Analyst – Vibes** | Feb 2025 – Oct 2025  
- Analyzed sales data and prepared dashboards to support decisions.  
- Evaluated product performance and customer behavior.  
- Implemented AI-based CCTV automation for employee performance.  

**Data & Sales Team Lead – Sunnah Dress, Mirpur** | June 2024 – Nov 2024  
- Led sales team and analyzed product trends.  
- Prepared reports to support management decisions.  

**Data & Inventory Assistant – Chocolate Craft Emporium (Remote)** | July 2023 – Apr 2024  
- Maintained inventory and tracked sales performance.  
- Optimized workflow and collaborated with team members.  
""")

# -------------------
# Technical Skills (like Interests section)
# -------------------
st.markdown("---")
st.subheader("🛠 Technical Skills")

skills = {
    "Python": 90,
    "R": 80,
    "SQL": 85,
    "ML": 75,
    "Visualization": 95,
    "EDA": 85
}

skill_cols = st.columns(len(skills))
for i, (skill, val) in enumerate(skills.items()):
    with skill_cols[i]:
        st.markdown(f"""
        <div style='
            background-color:#0072ff; 
            color:white; 
            padding:15px; 
            border-radius:15px; 
            text-align:center;
            font-weight:bold;
            font-size:16px;
        '>
        {skill}<br>{val}%
        </div>
        """, unsafe_allow_html=True)

# -------------------
# Soft Skills & Passion
# -------------------
st.markdown("---")
st.subheader("🌟 Strengths & Passion")
col_soft, col_passion = st.columns(2)
with col_soft:
    st.markdown("""
    - Problem-solving & analytical thinking  
    - Effective communication & collaboration  
    - Detail-oriented & results-driven  
    - Quick learner & adaptable
    """)
with col_passion:
    st.markdown("""
    - Passionate about transforming data into actionable insights  
    - Building interactive dashboards & visualization tools  
    - Aspiring to contribute to innovative AI & Data Science projects  
    - Exploring new technologies & programming techniques
    """)

# -------------------
# INTERESTS / HOBBIES
# -------------------
st.markdown("---")
st.subheader("📍 Personal Interests")
col1, col2, col3 = st.columns(3)
col1.markdown("🍫 Chocolate crafting & creative projects")
col2.markdown("📊 Data-driven storytelling")
col3.markdown("💡 Learning new programming techniques")

# -------------------
# ANIMATED COUNTERS
# -------------------
col1, col2, col3 = st.columns(3)
with col1: animated_counter("Projects Completed", 8)
with col2: animated_counter("Datasets Analyzed", 25)
with col3: animated_counter("Happy Clients / Collaborators", 10)

st.markdown("---")

# -------------------
# SKILLS SECTION (Radar Chart)
# -------------------
st.header("Skills & Tools")
skills_df = pd.DataFrame({
    'Skill': ['Python','R','SQL','ML','Visualization','EDA'],
    'Proficiency':[90, 80, 85, 75, 95, 85]
})
fig = px.line_polar(skills_df, r='Proficiency', theta='Skill', line_close=True, markers=True)
fig.update_traces(fill='toself', line_color='#ffffff')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -------------------
# PROJECT PORTFOLIO
# -------------------
st.header("Projects Portfolio")

col1, col2 = st.columns(2)

def display_projects(projects, col):
    for proj in projects:
        col.markdown(f"""
        <div class='project-card'>
            <h3>🚀 {proj['title']}</h3>
            <p>{proj['desc']}</p>
            <img src="{proj['image']}" width="100%" style="border-radius:10px;">
            <br><br>
            <a class='button' href='{proj['demo']}' target='_blank'>🔗 Live Demo</a>
            <a class='button' href='{proj['github']}' target='_blank'>🐙 View Code</a>
        </div>
        """, unsafe_allow_html=True)

coding_projects = [
    {"title": "Python Automation Script", "desc": "Automated daily tasks using Python scripts.", "image": "assets/project1.png", "demo": "#", "github": "https://github.com/yourusername/python-automation"},
    {"title": "Web Scraper", "desc": "Scraped and processed web data for reporting.", "image": "assets/project2.png", "demo": "#", "github": "https://github.com/yourusername/web-scraper"}
]

data_science_projects = [
    {"title": "Sales Dashboard", "desc": "Interactive dashboard analyzing sales trends & KPIs.", "image": "assets/project3.png", "demo": "#", "github": "https://github.com/yourusername/sales-dashboard"},
    {"title": "Customer Segmentation", "desc": "Clustering customers for marketing insights.", "image": "assets/project4.png", "demo": "#", "github": "https://github.com/yourusername/customer-segmentation"}
]

with col1:
    st.subheader("💻 Coding Projects")
    display_projects(coding_projects, col1)

with col2:
    st.subheader("📊 Data Science Projects")
    display_projects(data_science_projects, col2)

# -------------------
# CONTACT SECTION
# -------------------
st.header("Contact Me")
st.markdown("Reach me via Email, LinkedIn, GitHub or Kaggle!")
col1, col2 = st.columns(2)
with col1:
    st.write("📧 Email: your_email@example.com")
    st.write("💼 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)")
with col2:
    st.write("🐙 GitHub: [github.com/yourusername](https://github.com/yourusername)")
    st.write("📊 Kaggle: [kaggle.com/yourusername](https://kaggle.com/yourusername)")

st.markdown("<h5 style='text-align:center;color:gray;'>© 2025 Arfin Naim</h5>", unsafe_allow_html=True)
