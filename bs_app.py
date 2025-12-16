import streamlit as st
import pandas as pd
import plotly.express as px
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AK Solutions | HR Analytics Dashboard",
    page_icon="🏢",
    layout="wide"
)

# ---------------- SIDEBAR MENU ----------------
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Department Analysis", "Role Analysis", "About"]
)

# ---------------- DEPARTMENT - ROLE MAPPING ----------------
department_roles = {
    "Marketing": ["Executive"],
    "Sales": ["Senior Engineer", "Junior Engineer", "Executive", "Manager"],
    "Finance": ["Senior Engineer"],
    "Operations": ["Senior Engineer", "Executive"],
    "IT": ["Intern"],
    "HR": ["Executive", "Manager"]
}

locations = ["Bangalore", "Hyderabad", "Chennai", "Pune", "Delhi"]

# ---------------- EMPLOYEE DATA ----------------
employees = []
random.seed(10)

for emp_id in range(1, 151):
    dept = random.choice(list(department_roles.keys()))
    role = random.choice(department_roles[dept])

    employees.append({
        "Employee ID": emp_id,
        "Department": dept,
        "Role": role,
        "Location": random.choice(locations),
        "Experience (Years)": random.randint(0, 15),
        "Salary (LPA)": random.randint(3, 35),
        "Performance Score": random.randint(60, 100),
        "Work Hours / Week": random.randint(35, 55)
    })

df = pd.DataFrame(employees)

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

dept_filter = st.sidebar.multiselect(
    "Department",
    df["Department"].unique(),
    default=df["Department"].unique()
)

role_filter = st.sidebar.multiselect(
    "Role",
    df["Role"].unique(),
    default=df["Role"].unique()
)

filtered_df = df[
    (df["Department"].isin(dept_filter)) &
    (df["Role"].isin(role_filter))
]

# ================= DASHBOARD =================
if menu == "Dashboard":
    st.title("🏢 AK Solutions – HR Analytics Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("👥 Total Employees", filtered_df.shape[0])
    c2.metric("🎭 Total Roles", filtered_df["Role"].nunique())
    c3.metric("💰 Avg Salary (LPA)", round(filtered_df["Salary (LPA)"].mean(), 2))
    c4.metric("⭐ Avg Performance", round(filtered_df["Performance Score"].mean(), 2))

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            filtered_df,
            x="Role",
            color="Role",
            title="🎭 Role-wise Employee Count"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.pie(
            filtered_df,
            names="Role",
            hole=0.4,
            title="🎯 Employee Distribution by Role"
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    fig3 = px.scatter(
        filtered_df,
        x="Experience (Years)",
        y="Salary (LPA)",
        color="Role",
        size="Performance Score",
        title="📈 Salary vs Experience (Role-wise)"
    )
    st.plotly_chart(fig3, use_container_width=True)

# ================= DEPARTMENT ANALYSIS =================
elif menu == "Department Analysis":
    st.title("🏬 Department & Role Analysis")

    fig = px.bar(
        filtered_df,
        x="Department",
        color="Role",
        barmode="group",
        title="Department-wise Role Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.box(
        filtered_df,
        x="Department",
        y="Salary (LPA)",
        color="Role",
        title="Department-wise Salary by Role"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ================= ROLE ANALYSIS =================
elif menu == "Role Analysis":
    st.title("🎭 Role-wise Analytics Dashboard")

    avg_salary_role = (
        filtered_df
        .groupby("Role")["Salary (LPA)"]
        .mean()
        .reset_index()
    )

    fig1 = px.bar(
        avg_salary_role,
        x="Role",
        y="Salary (LPA)",
        color="Role",
        title="💰 Average Salary by Role"
    )
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.violin(
        filtered_df,
        x="Role",
        y="Performance Score",
        color="Role",
        box=True,
        title="⭐ Performance Distribution by Role"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📋 Role-wise Employee Data")
    st.dataframe(filtered_df, use_container_width=True)

# ================= ABOUT =================
elif menu == "About":
    st.title("ℹ️ About AK Solutions")

    st.markdown("""
    **AK Solutions** is a technology-focused organization delivering enterprise
    applications, analytics dashboards, and ERP solutions.

    This HR Analytics Dashboard enables:
    - Role-based workforce insights
    - Department & salary analytics
    - Performance evaluation
    - Data-driven HR decisions

    **Technologies Used**
    - Python
    - Streamlit
    - Pandas
    - Plotly

    🚀 Designed for ERP, HR Analytics & Business Intelligence.
    """)


# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 AK Solutions | HR Analytics Dashboard")
