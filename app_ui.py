import streamlit as st
import requests

st.title("🏭 Inventory Chatbot")

msg = st.text_input("Ask something...")

if st.button("Send"):
    res = requests.post("http://127.0.0.1:5000/chat", json={"message": msg})
    st.write(res.json()["response"])