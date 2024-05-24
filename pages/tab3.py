# This is a sample Python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Title of the app
def page3():
    st.title('School Web App')

# Add a sidebar
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home(profile)',"Notifications",'Attendance', "subjects", 'My TimeTable',"Fees", "performance","Change_password" ])

# Home page
if page == 'Home(profile)':


    st.markdown(
        """
        <div style="background-color:#242526; padding:10px; border-radius:5px">
        <h3 style="color:white;text-align:center;">Student Profile</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )


    c1,c2 = st.columns((1,2))
    with c1:
        st.write("####   Welcome Sahil Kashid ")
        logo = Image.open(r"C:\Users\kartik\Downloads\boy.jpg")  # Open the image file with Pillow
        st.image(logo, width=210)  # Display the image in Streamlit

    with ((c2)):
        with st.container():
            st.write("####")
            st.write("")
            st.write("Roll no.: 22")
            st.write("Grade : 6th")
            st.write("Gender : Male")
            st.write("Aadhar Card No :243138917743")
            st.write("Date of Birth :05-03-2014")
            st.write("Place of Birth :DHULE")
            st.write("Age :10")
            st.write("Nationality :Indian")
            st.write("Blood Group : B+")
            st.write("Category : OPEN")
            st.write("Permanent Address:NAVNATH NAGAR, PLOT NO 72 SAI BABA MANDIR DHULECity : Dhule    Dist : Dhule    State : MAHARASHTRA     Pincode : 424002")







#Notification
elif page == 'Notifications':
    import streamlit as st
    from streamlit_custom_notification_box import custom_notification_box as scnb
    import time

    # List of notifications
    notifications = [
        {"title": "Exam Date: Software Engineering", "date": "June 1, 2024"},
        {"title": "Assignment Submission: Web Development", "date": "May 30, 2024"},
        {"title": "School Holiday: Independence Day", "date": "July 4, 2024"},
        # Add more notifications as needed
    ]


    def AlertBox(wht_msg):
        styles = {
            'material-icons': {'color': '#FF0000'},
            'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
            'notification-text': {'': ''},
            'close-button': {'': ''},
            'link': {'': ''}
        }
        scnb(icon='info', textDisplay=wht_msg, externalLink='', url='', styles=styles)


    def main():
        st.title("My School Web App")

        # Notifications on main page
        st.subheader("Notifications")
        for notification in notifications:
            with st.spinner('🔔'):
                # Display each notification
                AlertBox(f"{notification['title']} on {notification['date']}")
                time.sleep(2)  # Pause to simulate spinning

        # Main content
        st.write("Please go through the Notifications")


    if __name__ == "__main__":
        main()

# Attendance page
elif page == 'Attendance':
    st.header('Attendance')

    # Create a table for attendance

    # Define the data for the timetable
    data = {
        "DATE-DAY": ["29 Jan Mon", "30 Jan Tue", "31 Jan Wed", "1 Feb Thu", "2 Feb Fri"],
        "English": ["P", "P", "A", "P", "P"],
        "Hindi": ["P", "P", "A", "P", "P"],
        "Marathi": ["P", "P", "A", "P", "P"],
        "Maths": ["P", "P", "A", "P", "P"],
        "Science": ["P", "P", "A", "P", "P"],
        "EVS": ["P", "P", "A", "P", "P"],
        "Drawing": ["P", "P", "A", "P", "P",],
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Calculate the total number of presents and absents for each subject
    total_presents = df.iloc[:, 1:].apply(lambda x: (x == "P").sum(), axis=0)
    total_absents = df.iloc[:, 1:].apply(lambda x: (x == "A").sum(), axis=0)


     #Append the totals to the DataFrame
    #df = df.append(pd.Series(total_presents, name="Total Presents"))
    #df = df.append(pd.Series(total_absents, name="Total Absents"))

    # Display the DataFrame as a table in Streamlit
    st.table(df)
    import matplotlib.pyplot as plt

    # Assuming 'df' is your DataFrame
    # Remove the 'DATE-DAY' column for the plot
    df_plot = df.drop('DATE-DAY', axis=1)

    # Convert 'P' to 1 and 'A' to 0
    df_plot = df_plot.replace({'P': 1, 'A': 0})

    # Calculate the sum for each subject
    df_sum = df_plot.sum()

    # Create the plot
    df_sum.plot(kind='bar', figsize=(10, 6))

    # Set the title and labels
    plt.title('Attendance Graph')
    plt.xlabel('Subjects')
    plt.ylabel('Attendance')

    # Show the plot
    plt.show()








# Class History page
elif page == 'Class History':
    st.header('Class History')

    # Create a table for class history
    history_data = pd.DataFrame({
        'Class': ['English', 'Maths', 'Science', 'History', 'Geography'],
        'Teacher': ['Mrs. Smith', 'Mr. Johnson', 'Dr. Clarke', 'Ms. Tennyson', 'Prof. Larsen'],
        'Time': ['9:00', '10:00', '11:00', '13:00', '14:00'] })

    st.table(history_data.set_index('Class'))


elif page == 'My TimeTable':
    timetable = {
        "Time": ["10:00 AM - 11:00", "11:00 PM - 12:00", "12:00 PM - 1:00", "1:00 PM - 2:00", "2:00 PM - 3:00"],
        "Monday": ["Maths", "English", "History", "Geography", "Marathi"],
        # ... add other days and subjects accordingly
    }


    # Function to display timetable on Streamlit app
    def display_timetable(timetable_data):
        st.write("## School Timetable")
        st.table(timetable_data)

    display_timetable(timetable)


elif page == "subjects":
    st.header('Subjects')
    sub = ["Maths", "Science", "English", "History", "Geography","EVS","Marathi"]
    st.table(sub)

elif page=='performance':
    # Create a simple bar chart
    st.subheader('Student Performance')
    chart_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["Maths", "Science", "English"])
    st.bar_chart(chart_data)

