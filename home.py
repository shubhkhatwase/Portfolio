import streamlit as st 
from PIL import Image

import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
    
col1,col2 = st.columns(2)
with col1:
    st.header("Shubham Khatwase")
    st.subheader("I'm aspiring Data Scientist.")
    st.write("""**In the era of Data Science,
    I'm glad to being part of this new era of
    Artificial Intelligence and Machine Learning.**""")

with col2:
    image = Image.open("img.png")
    st.image(image,width = 160)

import time 

latest_iteration = st.empty()
bar = st.progress(1)

for i in range(100):
    latest_iteration.text(f'Loading.... {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1) 

'...and now we\'re done!'

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')