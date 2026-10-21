import streamlit as st

# Set up page configurations
st.set_page_config(page_title="Books", layout="wide")

# App content
st.title("YA Books")
st.write("Sup gng")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}!")