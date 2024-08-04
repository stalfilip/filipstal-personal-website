import streamlit as st

st.write("#### Assistant")
st.write("---")
st.write("This is an AI powered chatbot that gives you advice on 'affärsrådgivning'.")

# Skapa en knapp som omdirigerar användaren direkt när de klickar på den
if st.button('Go to Bluebook'):
    st.write('<meta http-equiv="refresh" content="0; url=https://www.app.bluebook.se/">', unsafe_allow_html=True)
