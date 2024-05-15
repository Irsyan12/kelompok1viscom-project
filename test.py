import cv2
import streamlit as st
import time
from datetime import datetime

# Load Haar Cascade untuk deteksi mobil
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

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
        ''', 
        unsafe_allow_html=True
    )

    st.sidebar.markdown("<h1 class='sidebarTitle'>Car Detection System</h1>", unsafe_allow_html=True)
    
    current_time = datetime.now().strftime("%A %d %B %Y")
    st.sidebar.markdown(f"<h5 class='Datetime'>{current_time}</h5>", unsafe_allow_html=True)

    option = st.sidebar.selectbox(
        "Select the video to show",
        ("Video 1", "Video 2", "Video 3")
    )

    st.session_state["page"] = "car_detection_system"

    show_car_detection_system(option)

def detect_cars(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame, len(cars)

def show_car_detection_system(video_option):
    placeholder = st.empty()
    status_placeholder = st.empty()
    video_file = 'video1.mp4' if video_option == "Video 1" else 'video2.mp4' if video_option == "Video 2" else 'video3.mp4'
    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        st.error(f"Tidak dapat mengakses video {video_file}.")
        return

    start_time = time.time()
    fps = cap.get(cv2.CAP_PROP_FPS)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame, car_count = detect_cars(frame)

        mobil = car_count
        background_color = ""
        status = ""
        color = ""
        if mobil > 60:
            background_color = "rgba(255, 0, 0, 0.8)"
            status = "Macet"
            color = "white"
        elif mobil > 30:
            background_color = "rgba(255, 255, 0, 0.8)"
            status = "Padat Lancar"
            color = "black"
        else:
            background_color = "rgba(0, 128, 0, 0.8)"
            status = "Lancar"
            color = "white"

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        placeholder.image(frame, channels="RGB")
        status_placeholder.markdown(
            f"<div style='color:{color};display: flex; justify-content: space-between; align-items: center; background-color: {background_color}; padding: 10px; border-radius: 10px;'><span>Mobil yang terdeteksi: {mobil}</span><span>Status: {status}</span></div>",
            unsafe_allow_html=True
        )

        # Control the frame rate
        elapsed_time = time.time() - start_time
        time_to_wait = max(1./fps - elapsed_time, 0)
        time.sleep(time_to_wait)
        start_time = time.time()

    cap.release()

if __name__ == "__main__":
    main()
