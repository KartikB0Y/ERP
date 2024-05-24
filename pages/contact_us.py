from PIL import Image

import streamlit as st

# WISBUNNY School Slogan
st.markdown("# 🐰 **WISBUNNY School** 🎓")
st.markdown("---")

# School Slogan
st.markdown("## 🌟 School Slogan:")
st.markdown("**_\"Where Excellence Meets Education\"_**", unsafe_allow_html=True)
st.markdown("<span style='color:#00bfff;'>A commitment to fostering an environment of learning and growth.</span>", unsafe_allow_html=True)
st.markdown("---")

# School Logo
#st.markdown("## 🛡️ School Logo:")
#st.markdown("<span style='color:#800080;'>The emblem of quality education and holistic development.</span>", unsafe_allow_html=True)
#st.markdown("---")

# Contact Details
st.markdown("## ☎️ Contact Details:")
st.markdown("- **Phone Number:** <span style='color:#008000;'>+7757075828</span>", unsafe_allow_html=True)
st.markdown("- **Email Address:** <span style='color:#ff0000;'>info@wisbunny.edu</span>", unsafe_allow_html=True)
st.markdown("- **Location:** Wisbunny compound, Entrance from Shridhar Nagar road, Pimpri-Chinchwad Link Road, 411 033 Pune, Maharashtra")
st.markdown("---")



st.subheader(":mailbox: Get In Touch With Us!")


contact_form = """
    <form action="https://formsubmit.co/kartikkashid222@gamil.com" method="POST">
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
st.markdown("---")
st.markdown("<h2 style='text-align: wide; color: white;'>Connect with us for a journey where dreams meet reality!</h2>", unsafe_allow_html=True)
#st.markdown("*Connect with us for a journey where dreams meet reality!*")
c3,c4 = st.columns(2)
with c3:
    st.write("##")
    st.markdown("Quick Links")
    if st.button("Home🏠"):
        st.switch_page("app.py")
    if st.button("Faculty"):
        st.switch_page("pages/tab3.py")

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
st.write("© 2024 WisBunny School. All rights reserved.")