import streamlit as st

st.title("Aplikasi Perhitungan Kadar")

Bobot = st.number_input('Masukkan nilai bobot')
Volume = st.number_input('Masukkan nilai volume')

tombol = st.button('Hitung Nilai Kadar')

if tombol :
    nilai_kadar = Bobot*100/Volume
    st.success(f'Nilai Kadar sebesar {nilai_kadar}')