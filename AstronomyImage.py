# Astronomy Image of the day

import streamlit as st
import requests

st.set_page_config("wide")
st.title("Galaxy by the lake")
st.image("pic.jpg")
desc = f"""
dasdasdasdsadasdasdsadasdasd
asdsadsadsadsadasdsadsadasdsd
asdsadsadsadasdasdsadasdasdsad
adsadsadsadasdasdasdsadasdasdas
"""
st.write(desc)

# My Nasa Api Key
api_key = "glLyS2rRlWXGzFtyOQPM1yFiRHy3ADokHV1F46ME"

# URLS
core_url = "https://api.nasa.gov/planetary/apod"
# we have parameters api_key = DEMO_KEY and date =today from the website query parameters
param_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date=today"
print(param_url)

# get the HTTP response of the url
response = requests.get(param_url)
print(response)

# IMAGE SECTION
# get the image url
img_url = "https://apod.nasa.gov/apod/image/2304/Ring_HubbleSchmidt_1548.jpg"
# get the http response of the image
img_response = requests.get(img_url)
print(img_response)  # if response <Response [200]? means you dont need to put headers
# get the bytes codes of the image
img_code = img_response.content
# create the image from code as file.jpg
with open("pic.jpg" , "wb") as file:
    file.write(img_code)