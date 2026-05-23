import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="Student Dashboard",
    layout="wide"
)

# LOAD DATA
data = pd.read_csv("final_student_report.csv")

# TITLE
st.title("🎓 Student Result Dashboard")

st.markdown("---")

# METRICS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Students",
        len(data)
    )

with col2:
    st.metric(
        "Top Score",
        data["Avg_Total"].max()
    )

with col3:
    st.metric(
        "Average Score",
        int(data["Avg_Total"].mean())
    )

st.markdown("---")

# TOP STUDENTS
st.header("🏆 Top 3 Students")

top_students = data.sort_values(
    by="Avg_Total",
    ascending=False
)

top_3 = top_students.head(3)

col4, col5, col6 = st.columns(3)

# TOP 1
with col4:

    st.subheader("🥇 Top 1")

    st.write(
        "Name:",
        top_3["Name"].values[0]
    )

    st.write(
        "Maths:",
        top_3["Maths"].values[0]
    )

    st.write(
        "Physics:",
        top_3["Physics"].values[0]
    )

    st.write(
        "Chemistry:",
        top_3["Chemistry"].values[0]
    )

    st.write(
        "Average:",
        top_3["Avg_Total"].values[0]
    )

    st.write(
        "Grade:",
        top_3["Grade"].values[0]
    )

# TOP 2
with col5:

    st.subheader("🥈 Top 2")

    st.write(
        "Name:",
        top_3["Name"].values[1]
    )

    st.write(
        "Maths:",
        top_3["Maths"].values[1]
    )

    st.write(
        "Physics:",
        top_3["Physics"].values[1]
    )

    st.write(
        "Chemistry:",
        top_3["Chemistry"].values[1]
    )

    st.write(
        "Average:",
        top_3["Avg_Total"].values[1]
    )

    st.write(
        "Grade:",
        top_3["Grade"].values[1]
    )

# TOP 3
with col6:

    st.subheader("🥉 Top 3")

    st.write(
        "Name:",
        top_3["Name"].values[2]
    )

    st.write(
        "Maths:",
        top_3["Maths"].values[2]
    )

    st.write(
        "Physics:",
        top_3["Physics"].values[2]
    )

    st.write(
        "Chemistry:",
        top_3["Chemistry"].values[2]
    )

    st.write(
        "Average:",
        top_3["Avg_Total"].values[2]
    )

    st.write(
        "Grade:",
        top_3["Grade"].values[2]
    )

st.markdown("---")

# REMAINING STUDENTS
st.header("📋 Remaining Students")

remaining_students = top_students.iloc[3:]

remaining_students = remaining_students.reset_index(
    drop=True
)

remaining_students.index += 1

st.dataframe(
    remaining_students[
        ["Name", "Avg_Total", "Grade"]
    ],
    use_container_width=True
)

st.markdown("---")

# COUNTS
grade_count = data["Grade"].value_counts()

result_count = data["Grade"].apply(
    lambda x: "Fail" if x == "Fail" else "Pass"
).value_counts()

# VISUALIZATION SECTION
st.header("📊 Visualizations")

col7, col8 = st.columns(2)

# BAR CHART
with col7:

    st.subheader("📊 Grade Distribution")

    fig1, ax1 = plt.subplots(
        figsize=(3,3)
    )

    ax1.bar(
        grade_count.index,
        grade_count.values
    )

    ax1.set_xlabel("Grades")
    ax1.set_ylabel("Students")
    ax1.set_title("Grade Distribution")

    st.pyplot(
        fig1,
        use_container_width=False
    )

# PIE CHART
with col8:

    st.subheader("🥧 Pass vs Fail")

    fig2, ax2 = plt.subplots(
        figsize=(3,3)
    )

    ax2.pie(
        result_count.values,
        labels=result_count.index,
        autopct="%1.1f%%"
    )

    ax2.set_title("Pass vs Fail Percentage")

    st.pyplot(
        fig2,
        use_container_width=False
    )

st.markdown("---")

# HISTOGRAM
st.header("📈 Average Marks Distribution")

fig3, ax3 = plt.subplots(
    figsize=(5,3)
)

ax3.hist(
    data["Avg_Total"],
    bins=10
)

ax3.set_xlabel("Average Marks")
ax3.set_ylabel("Students")
ax3.set_title("Average Marks Histogram")

st.pyplot(
    fig3,
    use_container_width=False
)   