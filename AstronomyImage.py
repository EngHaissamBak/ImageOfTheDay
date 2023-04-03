# Astronomy Image of the day

import streamlit as st
import requests

# My Nasa Api Key
api_key = "glLyS2rRlWXGzFtyOQPM1yFiRHy3ADokHV1F46ME"

# URLS
core_url = "https://api.nasa.gov/planetary/apod"
# we have parameters api_key = DEMO_KEY and
# query example : https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
param_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
print(param_url)

# get the HTTP response of the url
response = requests.get(param_url)
print(response)  # --> <Response [200]>

# get the data of this response as dictionary data structure
data = response.json()
print(data)

# get the image title ,image  url , and image explanation
title = data["title"] # provide the key of dictionary data to get its value and store it in variable
explanation = data["explanation"] # provide the key of dictionary data to get its value and store it in variable
img_url  = data["url"] # provide the key of dictionary data to get its value and store it in variable
print(title)
print(img_url)
print(explanation)


# IMAGE SECTION
# get the http response of the image
img_response = requests.get(img_url)
print(img_response)  # if response <Response [200]? means you dont need to put headers
# get the bytes codes of the image
img_code = img_response.content
# create the image from code as file.jpg
with open("pic.jpg" , "wb") as file:
    file.write(img_code)

# creating the portofolio web using streamlit
st.set_page_config("wide")
st.title(title)
st.image("pic.jpg")
st.write(explanation)