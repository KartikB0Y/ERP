import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title('School Web App')

# Add a sidebar
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Attendance', 'Class History'])

# Home page
if page == 'Home':
    st.header('Welcome to our school website!')

    # Create a simple bar chart
    st.subheader('Student Performance')
    chart_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["Maths", "Science", "English"])
    st.bar_chart(chart_data)

# Attendance page
elif page == 'Attendance':
    st.header('Attendance')

    # Create a table for attendance
    attendance_data = pd.DataFrame({
        'Student': ['John', 'Mary', 'Peter', 'Jeff', 'Bill', 'Lisa', 'Jose'],
        'Attendance': ['Present', 'Absent', 'Present', 'Present', 'Absent', 'Present', 'Present']
    })
    st.table(attendance_data.set_index('Student'))

# Class History page
elif page == 'Class History':
    st.header('Class History')

    # Create a table for class history
    history_data = pd.DataFrame({
        'Class': ['English', 'Maths', 'Science', 'History', 'Geography'],
        'Teacher': ['Mrs. Smith', 'Mr. Johnson', 'Dr. Clarke', 'Ms. Tennyson', 'Prof. Larsen'],
        'Time': ['9:00', '10:00', '11:00', '13:00', '14:00']
    })
    st.table(history_data.set_index('Class'))
