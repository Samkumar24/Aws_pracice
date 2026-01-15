import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from fast_api import Response
import json

st.title("Welcom to the prediction")



numbers = st.text_input("enters the numbers")

if st.button("Generate output"):
    values = list(map(int , numbers.split(",")))

    response = requests.post(
        "http://127.0.0.1:8000/plot_it",
        json={'values':values})

    result = response.json()
    st.success(f"Maximum number is: {result['max_value']}")

    

    #img = Image.open(BytesIO(response.content))
    #st.image(img)
