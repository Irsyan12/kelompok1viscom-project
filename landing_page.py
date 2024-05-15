import streamlit as st

def main():
    st.markdown(
        """
        <style>
        .landing-header {
            color: #074173;
            text-align: center;
            padding: 50px 0;
        }
        .landing-text {
            color: #333333;
            text-align: justify;
            padding: 0 20%;
            font-size: 18px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 50px;
        
            background-color: #074173;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='landing-header'>Welcome to Car Detection System</h1>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <p class='landing-text'>This system aims to detect and analyze vehicles in video streams in real-time. 
        It provides information about traffic conditions based on the number of cars detected, helping to 
        improve traffic management and planning. Get started by selecting a video to view the car detection system in action!</p>
        """,
        unsafe_allow_html=True
    )

    
    if st.button("Start Car Detection System"):
        st.session_state["page"] = "car_detection_system"

if __name__ == "__main__":
    main()
