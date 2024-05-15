import random
import streamlit as st
import time
from datetime import datetime

def main():
    st.markdown(
        '''
        <style>
        .st-emotion-cache-6qob1r {
            background-color: #074173;
        }
        .sidebarTitle {
            color: #C5FF95;
            font-weight: bold;
            display: flex;
            justify-content: center;
        }
        .Datetime {
            color: #5DEBD7;
            display: flex;
            justify-content: center;
        }
        .sidebarItem {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        </style>
        '''
    , unsafe_allow_html=True)
    
    st.sidebar.markdown("<h1 class='sidebarTitle'>Car Detection System</h1>", unsafe_allow_html=True)
    
    current_time = datetime.now().strftime("%A %d %B %Y")
    st.sidebar.markdown(f"<h5 class='Datetime'>{current_time}</h5>", unsafe_allow_html=True)

    # st.sidebar.image("mobil.png", width=150)
    option = st.sidebar.selectbox(
    "Select the video to show",
    ("Video 1", "Video 2", "Video 3"))

    # Set session_state to car_detection_system to directly show car detection system
    st.session_state["page"] = "car_detection_system"

    show_car_detection_system(option)

def show_car_detection_system(video_option):
    if video_option == "Video 1":
        st.video('video1.mp4', format='mp4', start_time=0, loop=True, autoplay=True)
    elif video_option == "Video 2":
        st.video('video2.mp4', format='mp4', start_time=0, loop=True, autoplay=True)
    elif video_option == "Video 3":
        st.video('video3.mp4', format='mp4', start_time=0, loop=True, autoplay=True)

    placeholder = st.empty()  # Create an empty placeholder

    while True:
        mobil = random.randint(0, 100)
        background_color = ""
        status = ""
        color = ""
        if mobil > 60:
            background_color = "rgba(255, 0, 0, 0.8)"  # Red with 50% transparency
            status = "Macet"
            color = "white"
        elif mobil > 30:
            background_color = "rgba(255, 255, 0, 0.8)"  # Yellow with 50% transparency
            status = "Padat Lancar"
            color = "black"
        else:
            background_color = "rgba(0, 128, 0, 0.8)"  # Green with 50% transparency
            status = "Lancar"
            color = "white"

        # Clear previous content
        placeholder.empty()

        # Show the updated car detection system status
        placeholder.markdown(f"<div style='color:{color};display: flex; justify-content: space-between; align-items: center; background-color: {background_color}; padding: 10px; border-radius: 10px;'><span>Mobil yang terdeteksi: {mobil}</span><span>Status: {status}</span></div>", unsafe_allow_html=True)

        time.sleep(2)

if __name__ == "__main__":
    main()
