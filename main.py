import streamlit as st
import cv2
import numpy as np

def count_faces(frame):
    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around the faces and count them
    face_count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_count += 1

    return frame, face_count

def main():
    st.title('Face Counting System using OpenCV and Streamlit')
    st.write('This system counts the number of faces detected in the webcam feed.')

    # Open video capture from webcam
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        st.error('Unable to open webcam.')

    # Create an empty placeholder to display the webcam frame
    frame_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error('Unable to capture frame from webcam.')
            break

        # Perform face counting
        frame_processed, face_count = count_faces(frame)

        # Display the frame with face detection
        frame_placeholder.image(frame_processed, channels="BGR", caption="Face Detection Result")

        st.write('Total number of faces detected:', face_count)

        # Stop capturing when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Clear the previous frame
        frame_placeholder.empty()

    cap.release()

if __name__ == '__main__':
    main()
