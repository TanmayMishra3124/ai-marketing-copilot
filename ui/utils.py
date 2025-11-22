import streamlit as st

def load_css():
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            height: 3em;
        }
        .reportview-container {
            background: #f0f2f6;
        }
        div.stCode {
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
