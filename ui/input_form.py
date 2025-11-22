import streamlit as st

def render_input_form():
    st.sidebar.header("🚀 Campaign Details")
    
    with st.sidebar.form("campaign_form"):
        brand = st.text_input("Brand / Product Name", placeholder="e.g. TechNova")
        audience = st.text_input("Target Audience", placeholder="e.g. Startups, CTOs")
        platform = st.selectbox("Platform", ["Facebook", "Instagram", "LinkedIn", "Twitter", "Email", "Push Notification"])
        tone = st.selectbox("Tone", ["Professional", "Casual", "Urgent", "Witty", "Empathetic"])
        goal = st.text_area("Campaign Goal", placeholder="e.g. Drive signups for the new beta.")
        
        submitted = st.form_submit_button("Generate Campaign ✨")
        
        if submitted:
            if not brand or not audience:
                st.error("Please fill in Brand and Audience.")
                return None
            return {
                "brand": brand,
                "audience": audience,
                "platform": platform,
                "tone": tone,
                "goal": goal
            }
    return None
