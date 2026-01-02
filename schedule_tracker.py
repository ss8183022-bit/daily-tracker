import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Daily Task & Habit Tracker", layout="wide")

st.title("📅 Daily Task & Habit Tracker")
st.write("Track your progress and stay organized!")

# Example tasks
tasks = {
    "Morning Exercise": False,
    "Study for 2 hours": False,
    "Work on project": False,
    "Read a book": False,
    "Sleep by 11 PM": False
}

# Sidebar for task checkboxes
st.sidebar.header("✅ Today's Tasks")
completed = []
for task in tasks.keys():
    if st.sidebar.checkbox(task):
        completed.append(task)

# Progress bar
progress = len(completed) / len(tasks)
st.progress(progress)

st.write(f"**Progress:** {len(completed)} / {len(tasks)} tasks completed")

# Chart view
df = pd.DataFrame({
    "Task": list(tasks.keys()),
    "Status": ["Done" if t in completed else "Pending" for t in tasks.keys()]
})

fig = px.bar(df, x="Task", color="Status", title="Task Completion Status")
st.plotly_chart(fig, use_container_width=True)