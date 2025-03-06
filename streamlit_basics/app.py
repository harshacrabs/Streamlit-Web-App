import streamlit as st

#Title

st.title("Streamlit Basics")

# Header

st.header("This is a Header")

# Subheader

st.subheader("This is a subheader")

# Text

st.text("This is plain text")

# Write dimension

st.write("This is write dimension")

# Markdown
st.markdown("https://www.google.com")

st.markdown("[Google](https://www.google.com)")

# HTML

html_page = """
<div style="background-color:blue;padding:50px">
<p style="color:yellow;font-size:50px">Welcome to Streamlit Basics!</p>
"""
st.markdown(html_page, unsafe_allow_html=True)

# Colored Text boxes

st.success("Success")
st.warning("This is a warning")
st.error("This is an error")
st.info("This is information")

st.write(" ")

#Images

from PIL import Image
img = Image.open("media/YT_Channel.png")
st.image(img, width =500, caption= "Youtube Channel")

st.write(" ")

#Video

video_file = open("media/aws_video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.write("")

# Video with link

st.video("https://youtu.be/pdR5KRCd198?feature=shared")

# Audio file

audio_file = open("media/city_vibes.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")


#Buttons

st.button("Play")

# Button with condition

if st.button("Welcome"):
    st.text("Welcome to Streamlit Basics")


# Checkbox

if st.checkbox("Checkbox"):
    st.text("Checkbox selected")


# Radio buttons

radio_button = st.radio("Your Selection", ["A", "B"])
if radio_button == "A":
    st.info("You Selected A")
else:
    st.info("You Selected B")

st.write("")


# Select Box

country = st.selectbox("Your Country", ["India", "US", "UK", "Japan"])


# Multi-Select Box

occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "Data Analyst ", "Data Engineer"])

st.write("")


# Input Text and Numbers

name = st.text_input("Your Name", "Write Something..")
st.text(name)


# Text Area

message = st.text_area("Your Message", "Write something...")

# Number input

age = st.number_input("Input a Number")

# Slider

select_value = st.slider("Select a value", 1,20)
