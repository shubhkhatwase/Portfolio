import streamlit as st 
from PIL import Image
from streamlit_option_menu import option_menu
import webbrowser
#=================================================================================================
selected = option_menu(None,
                        ["Home","Academics","Projects","Contact",],
                        icons = ['person',"book",'list-task','phone'],default_index = 0,orientation="horizontal")
if (selected == "Home"):
    video_file = open('video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

if (selected == 'Academics'):
    #page title
    selected = option_menu("Basic information of Academics",
                            ["High School",
                            "Higher Secondary",
                            "Degree",
                            'Certificates',
                            ],orientation="horizontal")
    if(selected == "High School"):
        st.write("**Board Name:   Madhey Pradesh Board Bhopal**")
        st.write("**School Name:  Govt. High School Ganesh Ganj Khandwa**")
        st.write("**Year of Passing:  2015-16**")
        st.image("px.jpg")
        url = "https://photos.app.goo.gl/ksyYLWoTkdP7ZFyS8"
        if st.button('Open docs'):
         webbrowser.open_new_tab(url)
    if(selected == "Higher Secondary"):
        st.write("**Board Name: Madhey Pradesh Board Bhopal**")
        st.write("**School Name: Govt. Motilal Nehru Higher Secondary school Khandwa**")
        st.write("**Year of Passing = 2017-18**")
        st.image("p.jpg")
        url = "https://photos.app.goo.gl/e29gk6CWqgzDGtYp8"
        if st.button('Open docs'):
         webbrowser.open_new_tab(url)
    if(selected == "Certificates"):
       url = 'https://in.coursera.org/account/accomplishments/verify/AGNF9SUYFU65?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course'
       if st.button('Python Certificate'):
        webbrowser.open_new_tab(url)
#=================================================================================================================
if (selected == 'Contact'):
    selected = option_menu("Contact information ",
                            ["Mobile Numbers: ",
                            "E-Mail",
                            "LinkedIn",
                            'Github',
                            'Address'
                            ],orientation="horizontal")
    if(selected == "Mobile Numbers: "):
        st.write("**WhatsApp Number:   +91-9977127865**")
        st.write("**Calling Number:  +91-9302180145**")

    if(selected == "E-Mail"):
        st.write("**E-mail:   shubh7265@gmail.com**")
    if(selected == "LinkedIn"):
       url = 'linkedin.com/in/shubham-khatwase'
       st.write("Click it and reach on LinkedIn page")
       if st.button('click me'):
        webbrowser.open_new_tab(url)
    if(selected == "Github"):
       url = 'https://github.com/shubhkhatwase'
       st.write("Click it and reach on github page")
       if st.button('click me'):
        webbrowser.open_new_tab(url)
    if(selected == "Address"):
       url = 'https://goo.gl/maps/2QhxZ3QxZTAE51MQ6'
       st.write("Click it and reach on live location")
       if st.button('click me'):
        webbrowser.open_new_tab(url)