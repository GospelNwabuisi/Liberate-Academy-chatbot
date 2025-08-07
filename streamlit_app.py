from app import get_response

import streamlit as st
from app import get_response  # Make sure app.py has the get_response() function
import os

# --- Set Page Config ---
st.set_page_config(
    page_title="Liberate Academy Chatbot",
    page_icon="logo.jpeg",  # Ensure this file exists in the same folder
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Load Logo ---
logo_path = "logo.jpeg"
if os.path.exists(logo_path):
    st.image(logo_path, width=400)  # Bigger logo for better clarity
else:
    st.warning("⚠️ Logo not found. Please check the file name and location.")

# --- Custom Styles (green/yellow theme) ---
st.markdown("""
    <style>
        body {
            background-color: #e6f2e6;
        }
        .stApp {
            background-color: #e6f2e6;
        }
        .title {
            font-size: 28px;
            color: #2e7d32;
            font-weight: bold;
            margin-bottom: 0.5em;
        }
        .subtitle {
            font-size: 18px;
            color: #2e7d32;
            margin-bottom: 0.2em;
        }
        .chat-bubble {
            background-color: #a5d6a7;
            padding: 10px;
            border-radius: 12px;
            margin: 5px 0;
        }
        .user-message {
            text-align: right;
        }
        .bot-message {
            text-align: left;
        }
        .stTextInput > div > div > input {
            border: 2px solid #fbc02d;
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #fbc02d;
            color: black;
            border-radius: 8px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='title'>Liberate Academy Chatbot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Liberate Academy | Emesiri Street Off Sokoh Estate Road, Warri, Nigeria</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Contact: 08100987608 | 08035638671</div>", unsafe_allow_html=True)

# --- Initialize Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Input Field ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask me something about the school:", key="user_input")
    submitted = st.form_submit_button("Send")

# --- Chat Logic ---
if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": response})

# --- Display Chat Messages ---
for msg in st.session_state.messages:
    role_class = "user-message" if msg["role"] == "user" else "bot-message"
    speaker = "You" if msg["role"] == "user" else "Liberate Academy Chatbot"
    st.markdown(f"<div class='chat-bubble {role_class}'><strong>{speaker}:</strong> {msg['content']}</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <hr style='margin-top: 2rem; border-top: 1px solid #ccc;'>
    <div style='text-align: center; font-size: 0.85rem; color: #777;'>
        © 2025 Liberate Academy – All rights reserved.<br>
        Support: 08100987608 | 08035638671
    </div>
""", unsafe_allow_html=True)
