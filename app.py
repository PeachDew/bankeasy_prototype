import streamlit as st
import re

# Page config
st.set_page_config(
    page_title="Scam Guard",
    page_icon="🛡️",
    layout="centered"
)

# Simple scam keywords to check for
SCAM_KEYWORDS = {
    'urgent': ['urgent', 'immediate', 'expires today', 'act now'],
    'money': ['guaranteed profit', 'easy money', 'get rich quick', 'wire transfer'],
    'personal': ['ssn', 'social security', 'password', 'pin', 'bank account'],
    'authority': ['irs', 'police', 'legal action', 'arrest warrant']
}

def check_for_scams(text):
    """Simple scam detection - count suspicious keywords"""
    text_lower = text.lower()
    scam_score = 0
    found_keywords = []
    
    for category, keywords in SCAM_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                scam_score += 1
                found_keywords.append(f"{category}: {keyword}")
    
    return scam_score, found_keywords

def main():
    st.title("🛡️ Scam Guard")
    st.write("Simple fraud detection tool - paste suspicious messages below")
    
    # Main input
    user_text = st.text_area(
        "Enter suspicious message:",
        height=150,
        placeholder="Paste email, text, or message here..."
    )
    
    if st.button("Check for Scams"):
        if user_text:
            score, keywords = check_for_scams(user_text)
            
            # Show results
            if score >= 3:
                st.error(f"🚨 HIGH RISK - Found {score} red flags!")
                st.write("**Don't respond to this message!**")
            elif score >= 1:
                st.warning(f"⚠️ SUSPICIOUS - Found {score} red flags")
                st.write("**Be very careful - verify before responding**")
            else:
                st.success("✅ Looks OK - no obvious red flags")
            
            # Show what was found
            if keywords:
                st.write("**Red flags detected:**")
                for keyword in keywords:
                    st.write(f"- {keyword}")
        else:
            st.warning("Please enter some text to check")
    
    # Simple tips section
    st.markdown("---")
    st.subheader("Quick Tips")
    st.write("""
    **Common scam signs:**
    - Urgent deadlines
    - Requests for personal info
    - Too-good-to-be-true offers
    - Threats from "authorities"
    
    **When in doubt:** Don't respond, verify independently!
    """)

if __name__ == "__main__":
    main()
