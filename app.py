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
    "Visualization": 95,
    "SQL": 85,
    "ML": 75,
    "Excel": 90,
    "Power BI": 70,
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
st.write("")

# CSS Styling for the Boxes
st.markdown("""
<style>
.interest-box {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    color: white;
    border-radius: 12px;
    padding: 20px;
    margin: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
    height: 100%;
}
.interest-box:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}
.interest-title {
    font-size: 18px;
    font-weight: 600;
    color: #38bdf8;
    margin-bottom: 6px;
}
.interest-desc {
    font-size: 14px;
    color: #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

# Four columns for interests
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="interest-box">
        <div class="interest-title">🔍 E-Commerce Trend & Growth Lab</div>
        <div class="interest-desc">Discovering market insights through data, AI, and digital strategy.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="interest-box">
        <div class="interest-title">📊 Data Storytelling Lab</div>
        <div class="interest-desc">Turning complex datasets into engaging, actionable narratives.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="interest-box">
        <div class="interest-title">💡 Continuous Tech Learning</div>
        <div class="interest-desc">Exploring modern frameworks, AI tools, and coding innovations.</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="interest-box">
        <div class="interest-title">🚀 Innovation & Impact</div>
        <div class="interest-desc">Designing smart, scalable, and meaningful data-driven solutions.</div>
    </div>
    """, unsafe_allow_html=True)


# -------------------
# ANIMATED COUNTERS
# -------------------
st.markdown("---")
st.subheader("📈 Quick Stats")

col1, col2, col3, col4 = st.columns(4)
with col1:
    animated_counter("Projects Completed", 17)
with col2:
    animated_counter("Datasets Analyzed", 9)
with col3:
    animated_counter("Happy Clients", 7)
with col4:
    animated_counter("Skills Mastered", 9)

st.markdown("---")

# -------------------
# SKILLS RADAR CHART
# -------------------
st.header("📊 Skills & Tools")

skills_df = pd.DataFrame({
    'Skill': ['Python', 'Visualization', 'SQL', 'ML', 'Excel', 'Power BI', 'EDA'],
    'Proficiency': [90, 95, 85, 75, 90, 70, 85]
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
# CORE COMPETENCIES & TOOLS (Smart UI)
# -------------------
st.markdown("## 💼 Core Competencies & Tools")
st.write("")  # small space

# Custom CSS styling
st.markdown("""
<style>
.skill-box {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    color: white;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
}
.skill-box:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}
.skill-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
    color: #38bdf8;
}
.skill-item {
    display: inline-block;
    background: #334155;
    color: #e2e8f0;
    padding: 6px 12px;
    border-radius: 8px;
    margin: 4px 4px;
    font-size: 14px;
    transition: all 0.2s ease;
}
.skill-item:hover {
    background: #38bdf8;
    color: black;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="skill-box">
        <div class="skill-title">🎯 Core Competencies</div>
        <div class="skill-item">Data Analysis & Visualization</div>
        <div class="skill-item">Machine Learning & Predictive Modeling</div>
        <div class="skill-item">Statistical Analysis & Inference</div>
        <div class="skill-item">SQL Database Management</div>
        <div class="skill-item">Automation & Scripting</div>
        <div class="skill-item">Dashboard Development</div>
        <div class="skill-item">Collaboration with AI Tools (ChatGPT, LLMs)</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-box">
        <div class="skill-title">🛠️ Tools & Technologies</div>
        <div class="skill-item">Python</div>
        <div class="skill-item">R</div>
        <div class="skill-item">SQL</div>
        <div class="skill-item">Power BI</div>
        <div class="skill-item">Excel</div>
        <div class="skill-item">Pandas</div>
        <div class="skill-item">NumPy</div>
        <div class="skill-item">Scikit-learn</div>
        <div class="skill-item">Streamlit</div>
        <div class="skill-item">Plotly</div>
        <div class="skill-item">TensorFlow</div>
        <div class="skill-item">Git</div>
        <div class="skill-item">ChatGPT API</div>
    </div>
    """, unsafe_allow_html=True)

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
        "title": "Data Analysis Dashboard",
        "desc": "An interactive Streamlit dashboard for real-time sales and delivery insights.",
        "image": "assets/project1.jpg",
        "demo": "https://example.com",
        "github": "https://github.com/yourusername/data-analysis-dashboard"
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
st.markdown("---")
st.header("📧 Contact Me")
st.markdown("Let’s connect and collaborate! Reach out via any of the platforms below 👇")
st.write("")

# Custom CSS
st.markdown("""
<style>
.contact-card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    color: white;
    border-radius: 12px;
    padding: 20px;
    margin: 10px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
}
.contact-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
    background: linear-gradient(145deg, #0f172a, #1e293b);
}
.contact-icon {
    font-size: 28px;
    margin-bottom: 6px;
}
.contact-text {
    font-size: 15px;
    color: #e2e8f0;
}
a.contact-link {
    text-decoration: none;
    color: #38bdf8;
    font-weight: 600;
}
a.contact-link:hover {
    color: #0ea5e9;
}
</style>
""", unsafe_allow_html=True)

# Contact cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="contact-card">
        <div class="contact-icon">📧</div>
        <div class="contact-text">Email Me</div>
        <a class="contact-link" href="mailto:arfinnaim04@gmail.com">arfinnaim04@gmail.com</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-card">
        <div class="contact-icon">💼</div>
        <div class="contact-text">LinkedIn</div>
        <a class="contact-link" href="https://www.linkedin.com/in/arfinnaim04/" target="_blank">linkedin.com/in/arfinnaim04</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="contact-card">
        <div class="contact-icon">🐙</div>
        <div class="contact-text">GitHub</div>
        <a class="contact-link" href="https://github.com/arfinnaim02" target="_blank">github.com/arfinnaim02</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="contact-card">
        <div class="contact-icon">📊</div>
        <div class="contact-text">Kaggle</div>
        <a class="contact-link" href="https://www.kaggle.com/arfinnaim02" target="_blank">kaggle.com/arfinnaim02</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")


# -------------------
# FOOTER
# -------------------
st.markdown("""
<h5 style='text-align:center; color:#9ca3af; margin-top: 50px;'>
© 2025 Arfin Naim. All rights reserved. 
""", unsafe_allow_html=True)