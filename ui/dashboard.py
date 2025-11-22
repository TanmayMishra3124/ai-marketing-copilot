import streamlit as st
import re

def parse_sections(content):
    """
    Parses the generated content into sections based on numbered headers.
    Assumes format like '1. **Title**'
    """
    sections = {}
    lines = content.split('\n')
    current_section = "Overview"
    current_text = []
    
    for line in lines:
        # Match lines starting with a number followed by a dot and bold text
        match = re.match(r'^\d+\.\s+\*\*(.*?)\*\*', line)
        if match:
            # Save previous section
            if current_text:
                sections[current_section] = "\n".join(current_text).strip()
            
            # Start new section
            current_section = match.group(1)
            current_text = [] # Don't include the header in the text body to avoid redundancy
        else:
            current_text.append(line)
    
    # Save the last section
    if current_text:
        sections[current_section] = "\n".join(current_text).strip()
        
    return sections

def render_dashboard(campaign):
    st.markdown(f"## 🎯 Campaign for **{campaign['brand']}**")
    st.markdown(f"**Platform:** `{campaign['platform']}` | **Tone:** `{campaign['tone']}`")
    st.divider()
    
    content = campaign['content']
    sections = parse_sections(content)
    
    # If parsing failed to find multiple sections, just show the whole thing
    if len(sections) <= 1:
        st.subheader("Generated Content")
        st.code(content, language="markdown")
    else:
        for title, text in sections.items():
            if text.strip():
                st.subheader(title)
                st.code(text, language="markdown")
