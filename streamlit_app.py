from operator import truediv
from st_functions import st_button, load_css
import streamlit as st
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
with col2:
    col2.image(Image.open('eazenlogotransparentblack.png'))
    #st.header('Eazen')

st.info('Navigate to your favorite applications using the links below!')

icon_size = 24

st_button('youtube', 'https://www.youtube.com/watch?v=ayGwg0RvxDg&list=PLD72Ylz-Y01vcGTYmEaN9nz02o0yZMWy8', 'Funny Cat Videos', icon_size)
st_button('medium', 'https://medium.com/', 'Medium Article Example', icon_size)
st_button('twitter', 'https://twitter.com/', 'Twitter Example', icon_size)
st_button('linkedin', 'https://www.linkedin.com/', 'LinkedIn Example', icon_size)
