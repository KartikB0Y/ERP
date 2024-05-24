import streamlit as st
from PIL import Image
import mysql.connector

import app

#st.set_page_config(page_title="ERP Login ", layout="wide", page_icon=":tada: ")    # try this too "initial_sidebar_state="expanded"
def authenticate(email, password):
    # Create a connection to your MySQL database
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='StudentLogin')

    # Create a cursor object
    cursor = cnx.cursor()

    # Execute a query to check if the username and password are valid
    query = ("SELECT * FROM students WHERE email = %s AND password = %s")
    cursor.execute(query, (email, password))

    # If the query returns a result, then the username and password are valid
    user = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    return user is not None


def main():

    st.markdown(
        """
        <div style="background-color:#242526; padding:10px; border-radius:10px">
        <h1 style="color:white;text-align:center;">Student Login Page</h1>
        </div>
        """,
        unsafe_allow_html=True,
                                        )
    col1 , col2 = st.columns((1, 2))
    with col1:
        st.write("####    Welcome to ERP Login")
        logo = Image.open(r"C:\Users\kartik\Downloads\wisbunnylogo.png")  # Open the image file with Pillow
        st.image(logo, width=300)  # Display the image in Streamlit
    with col2:
        with st.container():
            st.write("##")

            email = st.text_input("Email Id", max_chars=50)
            st.write("##")
            password = st.text_input("Password", type="password")
            st.write("##")
            if st.button("Sign In"):
                if email and password:  # Check if username and password are not empty
                    if authenticate(email, password):  # Check if username and password are valid
                        st.success(f"Welcome {email}!")
                        app.step3()     # Direct to tab3


                    else:
                        st.error("Invalid Username or Password")
                else:
                    st.error("Email or Password should not be empty")

            if st.button("Forgot Password"):
                st.error("Please contact admin")



if __name__ == "__main__":
    main()
