import streamlit as st
from ui.utils import load_css
from ui.input_form import render_input_form
from ui.dashboard import render_dashboard
from backend.pipeline import run_campaign
from database.db import init_db, get_campaigns

# Page config
st.set_page_config(
    page_title="AI Marketing Copilot",
    page_icon="🚀",
    layout="wide"
)

# Initialize Database
init_db()

# Load Custom CSS
load_css()

# Sidebar Input
inputs = render_input_form()

# Main Content Area
st.title("AI Marketing Copilot 🤖")
st.markdown("Generate high-converting marketing copy in seconds.")

if inputs:
    with st.spinner("Generating your campaign..."):
        result = run_campaign(
            inputs['brand'],
            inputs['audience'],
            inputs['platform'],
            inputs['tone'],
            inputs['goal']
        )
        
        if result['status'] == 'success':
            st.session_state['latest_campaign'] = {
                'brand': inputs['brand'],
                'platform': inputs['platform'],
                'tone': inputs['tone'],
                'content': result['content']
            }
            st.success("Campaign generated successfully!")
        else:
            st.error(result['message'])

# Display Latest Campaign
if 'latest_campaign' in st.session_state:
    render_dashboard(st.session_state['latest_campaign'])

# History Section
st.markdown("---")
st.subheader("📜 Recent Campaigns")

try:
    campaigns = get_campaigns()
    if campaigns:
        for c in campaigns[:5]:
            with st.expander(f"{c['brand']} - {c['platform']} ({c['created_at']})"):
                st.markdown(f"**Tone:** {c['tone']} | **Goal:** {c['goal']}")
                st.code(c['content'], language="markdown")
    else:
        st.info("No campaigns generated yet.")
except Exception as e:
    st.error(f"Error loading history: {e}")
