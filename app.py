import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Academic Performance Dashboard")
st.markdown("Advanced Dashboard – 8 Semesters | 5 Subjects per Semester")

# ---------------- DATA CREATION ----------------
semesters = {
    "Sem 1": ["Maths-I", "Physics", "Chemistry", "English", "Programming"],
    "Sem 2": ["Maths-II", "Electronics", "EVS", "OOPS", "Data Structures"],
    "Sem 3": ["DBMS", "OS", "Computer Networks", "Java", "Discrete Maths"],
    "Sem 4": ["Python", "SE", "Microprocessors", "Statistics", "Web Tech"],
    "Sem 5": ["AI", "ML", "CN-II", "Cloud Computing", "IoT"],
    "Sem 6": ["Data Science", "Big Data", "DevOps", "Cyber Security", "UI/UX"],
    "Sem 7": ["Deep Learning", "NLP", "Blockchain", "AR/VR", "Elective-I"],
    "Sem 8": ["Project", "Internship", "Elective-II", "Seminar", "Ethics"]
}

students = ["Aarav", "Diya", "Rahul", "Sneha", "Arjun"]

records = []

import random
random.seed(42)

for sem, subjects in semesters.items():
    for student in students:
        for subject in subjects:
            records.append({
                "Student Name": student,
                "Semester": sem,
                "Subject": subject,
                "Marks": random.randint(55, 95),
                "Attendance (%)": random.randint(75, 100)
            })

df = pd.DataFrame(records)

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

semester_filter = st.sidebar.selectbox(
    "Select Semester",
    ["All"] + sorted(df["Semester"].unique().tolist())
)

student_filter = st.sidebar.selectbox(
    "Select Student",
    ["All"] + sorted(df["Student Name"].unique().tolist())
)

filtered_df = df.copy()

if semester_filter != "All":
    filtered_df = filtered_df[filtered_df["Semester"] == semester_filter]

if student_filter != "All":
    filtered_df = filtered_df[filtered_df["Student Name"] == student_filter]

# ---------------- KPIs ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("👨‍🎓 Students", filtered_df["Student Name"].nunique())
col2.metric("📚 Subjects", filtered_df["Subject"].nunique())
col3.metric("📊 Avg Marks", round(filtered_df["Marks"].mean(), 2))
col4.metric("🕒 Avg Attendance", round(filtered_df["Attendance (%)"].mean(), 2))

st.markdown("---")

# ---------------- CHARTS ----------------
left, right = st.columns(2)

with left:
    st.subheader("📈 Subject-wise Marks")
    fig1 = px.bar(
        filtered_df,
        x="Subject",
        y="Marks",
        color="Student Name",
        barmode="group"
    )
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.subheader("📊 Attendance Distribution")
    fig2 = px.box(
        filtered_df,
        x="Semester",
        y="Attendance (%)",
        color="Semester"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- LINE CHART ----------------
st.subheader("📉 Performance Trend Across Semesters")
trend_df = filtered_df.groupby("Semester")["Marks"].mean().reset_index()

fig3 = px.line(
    trend_df,
    x="Semester",
    y="Marks",
    markers=True
)
st.plotly_chart(fig3, use_container_width=True)

# ---------------- DATA TABLE ----------------
st.subheader("📋 Detailed Student Records")
st.dataframe(filtered_df, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Advanced Student Dashboard | Python • Streamlit • Plotly")
