import streamlit as st

# Membuat navigasi menggunakan radio button
page = st.sidebar.radio("Navigation", ["Halaman 1", "Halaman 2"])

# Menampilkan konten halaman 1
if page == "Halaman 1":
    st.title("Halaman 1")
    st.write("Ini adalah konten dari halaman 1")

# Menampilkan konten halaman 2
elif page == "Halaman 2":
    st.title("Halaman 2")
    st.write("Ini adalah konten dari halaman 2")