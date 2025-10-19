import streamlit as st
import plotly.express as px
import pandas as pd
import time

# -------------------
# PAGE CONFIG - MUST BE FIRST!
# -------------------
st.set_page_config(
    page_title="Arfin Naim Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------
# LOAD EXTERNAL CSS
# -------------------
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ {file_name} not found. Using default styling.")

local_css("style.css")

# -------------------
# HELPER FUNCTIONS
# -------------------
def animated_counter(label, count, duration=2):
    """Display animated counter"""
    placeholder = st.empty()
    for i in range(count + 1):
        time.sleep(duration / max(count, 1))
        placeholder.markdown(
            f"""
            <div style='text-align: center; padding: 20px;'>
                <div style='font-size: 3em; font-weight: bold; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;'>{i}</div>
                <p style='font-size: 1.1em; color: #cbd5e1; margin-top: 10px;'>{label}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

def create_skill_card(skill_name, percentage):
    """Create individual skill card"""
    return f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
    '>
    <div style='font-size: 1.3em;'>{skill_name}</div>
    <div style='font-size: 1.5em; margin-top: 10px;'>{percentage}%</div>
    </div>
    """

# -------------------
# HERO SECTION
# -------------------
st.markdown("""
<div style='
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 80px 40px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
    margin-bottom: 40px;
'>
    <h1 style='font-size: 3.5em; margin: 0; color: white;'>Hi, I'm Arfin Naim</h1>
    <h3 style='font-size: 1.8em; margin-top: 15px; color: rgba(255,255,255,0.95);'>I transform data into actionable insights</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------
# ABOUT ME SECTION
# -------------------
st.header("👤 About Me")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/profile.jpg", width=300, caption="Arfin Naim")

with col2:
    col_edu, col_work = st.columns(2)

    with col_edu:
        st.markdown("### 🎓 Education")
        st.markdown("""
        - **Master of Science (MSc)** in Applied Statistics & Data Science, Jahangirnagar University — *Enrolled 2027*  
        - **Bachelor of Science (BSc)** in Computer Communication Engineering, IIUC — *CGPA: 3.606 (2023)*  
        - **HSC** in Science, Bangladesh Naubahini College — *GPA: 3.5/5 (2019)*  
        - **SSC** in Science, Government Muslim High School — *GPA: 5/5 (2017)*
        """)

    with col_work:
        st.markdown("### 💼 Work Experience")
        st.markdown("""
**Data Analyst – Vibes** | Feb 2025 – Oct 2025  
- Sales analytics & performance dashboards  
- AI-based CCTV automation  
- Product performance evaluation  

**Data & Sales Team Lead – Sunnah Dress** | June 2024 – Nov 2024  
- Led sales team & trend analysis  
- Strategic reporting & insights  

**Data & Inventory Assistant – Chocolate Craft** | July 2023 – Apr 2024  
- Inventory management & sales tracking  
- Process optimization  
""")

# -------------------
# TECHNICAL SKILLS SECTION
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
        st.markdown(create_skill_card(skill, val), unsafe_allow_html=True)

# -------------------
# STRENGTHS & PASSION
# -------------------
st.markdown("---")
st.subheader("🌟 Strengths & Passion")

col_soft, col_passion = st.columns(2)

with col_soft:
    st.markdown("""
    #### 💪 Strengths
    - ✓ Problem-solving & analytical thinking  
    - ✓ Effective communication & collaboration  
    - ✓ Detail-oriented & results-driven  
    - ✓ Quick learner & adaptable
    """)

with col_passion:
    st.markdown("""
    #### 🚀 Passion
    - 🎯 Data-driven storytelling  
    - 📊 Building interactive dashboards  
    - 💡 AI & Data Science innovation  
    - 🔬 Exploring new technologies
    """)

# -------------------
# INTERESTS / HOBBIES
# -------------------
st.markdown("---")
st.subheader("📍 Personal Interests")

col1, col2, col3, col4 = st.columns(4)
col1.markdown("#### 🍫 Chocolate Crafting\nCreative projects")
col2.markdown("#### 📊 Data Storytelling\nTransforming data into narratives")
col3.markdown("#### 💡 Tech Learning\nNew programming techniques")
col4.markdown("#### 🚀 Innovation\nBuilding impactful solutions")

# -------------------
# ANIMATED COUNTERS
# -------------------
st.markdown("---")
st.subheader("📈 Quick Stats")

col1, col2, col3, col4 = st.columns(4)
with col1:
    animated_counter("Projects Completed", 8)
with col2:
    animated_counter("Datasets Analyzed", 25)
with col3:
    animated_counter("Happy Clients", 10)
with col4:
    animated_counter("Skills Mastered", 6)

st.markdown("---")

# -------------------
# SKILLS RADAR CHART
# -------------------
st.header("📊 Skills & Tools")

skills_df = pd.DataFrame({
    'Skill': ['Python', 'R', 'SQL', 'ML', 'Visualization', 'EDA'],
    'Proficiency': [90, 80, 85, 75, 95, 85]
})

fig = px.line_polar(
    skills_df,
    r='Proficiency',
    theta='Skill',
    line_close=True,
    markers=True,
    title="Technical Proficiency Radar"
)

fig.update_traces(
    fill='toself',
    line_color='#667eea',
    fillcolor='rgba(102, 126, 234, 0.3)'
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor='rgba(102, 126, 234, 0.2)',
            tickfont=dict(color='#cbd5e1')
        ),
        angularaxis=dict(
            gridcolor='rgba(102, 126, 234, 0.2)',
            tickfont=dict(color='#cbd5e1')
        )
    ),
    font=dict(color='#cbd5e1'),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -------------------
# CORE COMPETENCIES & TOOLS
# -------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### 🎯 Core Competencies
    - ✓ Data Analysis & Visualization
    - ✓ Machine Learning Models
    - ✓ SQL Database Management
    - ✓ Automation & Scripting
    - ✓ Dashboard Development
    - ✓ Statistical Analysis
    """)

with col2:
    st.markdown("""
    #### 🛠️ Tools & Technologies
    `Python` `R` `SQL` `Pandas` `NumPy` `Scikit-learn` `Plotly` `Streamlit` `Excel` `Git` `Tableau` `Power BI`
    """)

st.markdown("---")

# -------------------
# PROJECT PORTFOLIO
# -------------------
st.header("🚀 Projects Portfolio")

coding_projects = [
    {
        "title": "Python Automation Script",
        "desc": "Automated daily tasks using Python scripts, reducing manual work by 60%.",
        "image": "assets/project1.png",
        "demo": "#",
        "github": "https://github.com/yourusername/python-automation"
    },
    {
        "title": "Web Scraper",
        "desc": "Scraped and processed web data for business intelligence and reporting.",
        "image": "assets/project2.png",
        "demo": "#",
        "github": "https://github.com/yourusername/web-scraper"
    }
]

data_science_projects = [
    {
        "title": "Data Analysis Portal",
        "desc": "Interactive Streamlit app for real-time data analysis with advanced visualizations.",
        "image": "assets/project1.jpg",
        "demo": "https://dataanalysis01.streamlit.app/",
        "github": "https://github.com/arfinnaim02/Data-Analysis-Portal"
    },
    {
        "title": "Customer Segmentation",
        "desc": "ML-powered clustering for targeted marketing insights and customer profiling.",
        "image": "assets/project4.png",
        "demo": "#",
        "github": "https://github.com/yourusername/customer-segmentation"
    }
]

col1, col2 = st.columns(2)

with col1:
    st.subheader("💻 Coding Projects")
    for proj in coding_projects:
        st.markdown(f"""
        <div class='project-card'>
            <h3>🚀 {proj['title']}</h3>
            <p>{proj['desc']}</p>
            <img src="{proj['image']}" width="100%" style="border-radius:10px; margin: 15px 0;">
            <div style='margin: 15px 0;'>
                <a class='button' href='{proj['demo']}' target='_blank'>🔗 Live Demo</a>
                <a class='button' href='{proj['github']}' target='_blank'>🐙 View Code</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.subheader("📊 Data Science Projects")
    for proj in data_science_projects:
        st.markdown(f"""
        <div class='project-card'>
            <h3>🚀 {proj['title']}</h3>
            <p>{proj['desc']}</p>
            <img src="{proj['image']}" width="100%" style="border-radius:10px; margin: 15px 0;">
            <div style='margin: 15px 0;'>
                <a class='button' href='{proj['demo']}' target='_blank'>🔗 Live Demo</a>
                <a class='button' href='{proj['github']}' target='_blank'>🐙 View Code</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# -------------------
# CONTACT SECTION
# -------------------
st.header("📧 Contact Me")
st.markdown("Reach me via Email, LinkedIn, GitHub or Kaggle!")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.link_button("📧 Email", "mailto:arfinnaim04@gmail.com")
with col2:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/arfinnaim04/")
with col3:
    st.link_button("🐙 GitHub", "https://github.com/arfinnaim02")
with col4:
    st.link_button("📊 Kaggle", "https://www.kaggle.com/arfinnaim02")

st.markdown("---")

# -------------------
# FOOTER
# -------------------
st.markdown("""
<h5 style='text-align:center; color:#9ca3af; margin-top: 50px;'>
© 2025 Arfin Naim. All rights reserved. | Built with ❤️ using Streamlit
</h5>
""", unsafe_allow_html=True)