import streamlit as st
from PIL import Image
# Set the page title
st.set_page_config(page_title="WisBunny School Website", page_icon="🐰", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

whatsapp_url = "https://wa.me/7757075828"
facebook_url = "https://www.facebook.com/your_page"
twitter_url = "https://twitter.com/intent/post?text=checkout%20the%20url&url=https%3A%2F%2Fwww.sankalpenglishmediumschoolpune.in"
linkedin_url = "https://www.linkedin.com/in/your_profile"
pinterest_url = "https://www.pinterest.com/your_profile"


col1, col2, col3,col4 = st.columns(4)
with col2:
        logo = Image.open(r"C:\Users\kartik\Downloads\wisbunnylogo.png")  # Open the image file with Pillow
        st.image(logo, width=90)  # Display the image in Streamlit
with col1:
        st.write("Where Excellence Meets Education")
with col3:
        st.write("WISBUNNY INTERNATIONAL SCHOOL")
with col4:
        st.write("Contact :7757075828")
        st.write("Contact us: info@wisbunny.edu")


welcome_photo= Image.open(r"C:\Users\kartik\Downloads\1.png")  # Open the image file with Pillow
st.image(welcome_photo, width=1300)


st.markdown("<h1 style='text-align: center; color: #f0e68c;'>Our Facilities</h1>", unsafe_allow_html=True)
photo2= Image.open(r"C:\Users\kartik\Downloads\2.png")  # Open the image file with Pillow
st.image(photo2, width=1300)

photo3= Image.open(r"C:\Users\kartik\Downloads\3.png")  # Open the image file with Pillow
st.image(photo3, width=1300)

# Example: Add a button for admissions
url = "https://docs.google.com/forms/d/e/1FAIpQLScJkXQVmpMWCRLMAp_dRQLou2Z_RF9B3i9f5fiypsS62w4j0w/viewform?usp=sf_link"
st.markdown(f'<a href="{url}"><button style="background-color:#002b36;">Apply Now</button></a>',
                unsafe_allow_html=True)


# Example: Display contact information
st.write("Contact us: info@wisbunny.edu")

# Example: Add a footer (optional)
# Define the footer layout   # BACKGROUND NOT ADDED !
st.markdown(
    """
    <style>
        body{
            background-image: url("https://th.bing.com/th/id/OLC.k22sHm9eo60Weg480x360?&rs=1&pid=ImgDetMain"); 
            background-size: cover;
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.write("---")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.subheader(":mailbox: Get In Touch With Us!")

    contact_form = """
        <form action="https://formsubmit.co/kartikkashid223@gamil.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here"></textarea>
             <button type="submit">Send</button>
        </form>
        """

    st.markdown(contact_form, unsafe_allow_html=True)


    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")
    st.write("© 2024 WisBunny School. All rights reserved.")
with c2:
    st.write("##")
    st.write("Connect with Us:")
    st.write("")
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <a href="{whatsapp_url}" target="_blank">
                <img src="https://img.icons8.com/?size=24&id=AltfLkFSP7XN&format=png" alt="WhatsApp">
            </a>
            <a href="{facebook_url}" target="_blank">
                <img src="https://img.icons8.com/?size=24&id=uLWV5A9vXIPu&format=png" alt="Facebook">
            </a>
            <a href="{twitter_url}" target="_blank">
                <img src="https://img.icons8.com/?size=24&id=6Fsj3rv2DCmG&format=png" alt="Twitter">
            </a>
            <a href="{linkedin_url}" target="_blank">
                <img src="https://img.icons8.com/?size=24&id=xuvGCOXi8Wyg&format=png" alt="LinkedIn">
            </a>
            <a href="{pinterest_url}" target="_blank">
                <img src="https://img.icons8.com/?size=24&id=XErM9A1xNUK5&format=png" alt="Pinterest">
            </a>
        </div>
        """,unsafe_allow_html=True,)




with c3:
    st.write("##")
    st.markdown("Quick Links")
    if st.button("Home🏠"):
        st.switch_page("app.py")
    if st.button("Faculty"):
        st.switch_page("pages/tab3.py")
    if st.button("Contact Us"):
        st.switch_page("pages/contact_us.py")

    # Display a styled link using HTML
    url = "https://docs.google.com/forms/d/e/1FAIpQLScJkXQVmpMWCRLMAp_dRQLou2Z_RF9B3i9f5fiypsS62w4j0w/viewform?usp=sf_link"
    st.markdown(f'<a href="{url}"><button style="background-color:#002b36;">Admission Form</button></a>',
                unsafe_allow_html=True)

    st.write("ERP Login Links")
    if st.button("Student Login!"):
        st.switch_page("pages/tab2.py")

with c4:
    st.write("##")
    st.write("Find Us :")
    st.write("""Wisbunny International School
Wisbunny compound, Entrance from Shridhar Nagar road,
Pimpri-Chinchwad Link Road,
411 033 Pune, Maharashtra

Call : 7757075828
admissions@wisbunnyschools.edu.in""")

#from streamlit_extras.stoggle import stoggle
#stoggle(
#   "Login",
 #   """🥷Student Login """
#)

st.sidebar.title("Share Us On")
st.sidebar.markdown(
    """
    <a href="https://wa.me/7757075828" target="_blank">
        <img src="https://img.icons8.com/?size=24&id=AltfLkFSP7XN&format=png" alt="WhatsApp">
    </a>
    <a href="https://www.facebook.com/your_page" target="_blank">
        <img src="https://img.icons8.com/?size=24&id=uLWV5A9vXIPu&format=png" alt="Facebook">
    </a>
    <a href="https://twitter.com/intent/post?text=checkout%20the%20url&url=https%3A%2F%2Fwww.sankalpenglishmediumschoolpune.in" target="_blank">
        <img src="https://img.icons8.com/?size=24&id=6Fsj3rv2DCmG&format=png" alt="Twitter">
    </a>
    <a href="https://www.linkedin.com/in/your_profile" target="_blank">
        <img src="https://img.icons8.com/?size=24&id=xuvGCOXi8Wyg&format=png" alt="LinkedIn">
    </a>
    <a href="https://www.pinterest.com/your_profile" target="_blank">
        <img src="https://img.icons8.com/?size=24&id=XErM9A1xNUK5&format=png" alt="Pinterest">
    </a>
    """,
    unsafe_allow_html=True,)
#if st.button("Click me!"):
#    st.switch_page("pages/tab2.py")
def step3():
    st.switch_page("pages/tab3.py")


#from socialsnap import SocialSnap
