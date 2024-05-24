import streamlit as st
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
st.markdown("*Connect with us for a journey where dreams meet reality!*")

# Define the header layout
st.markdown(
    """
    <style>
        .header {
            padding: 60px; /* Larger padding */
            text-align: wide;
            background-color: #1abc9c; /* The specified color format */
            color: white;
            font-size: 30px; /* Bigger font size */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create the header
st.markdown("<div class='header'>WisBunny School</div>", unsafe_allow_html=True)

#st.set_page_config(page_title="WisBunny School Website", page_icon="🐰", layout="wide")
col1, col2, col3 = st.columns(3)
with col2:
        logo = Image.open(r"C:\Users\kartik\Downloads\wisbunnylogo.png")  # Open the image file with Pillow
        st.image(logo, width=90)  # Display the image in Streamlit
with col1:
        st.write("Where Excellence Meets Education")
with col3:
        st.write("Contact :7757075828")
        st.write("Contact us: info@wisbunny.edu")