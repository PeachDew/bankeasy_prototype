
import streamlit as st
import re
import random

# Page config
st.set_page_config(
    page_title="BankEasy - Fraud Detection",
    page_icon="🔎",
    layout="centered"
)


def main():
    st.title("🕵️ Fraud Detection")
    user_text = st.text_area(
        "Enter suspicious message",
        placeholder = "Paste email or text messages here"
    )
    
    risk_score = random.randint(0,100)
    if st.button("Analyse"):
        if risk_score > 80:
            st.error("**HIGH RISK** - Found red flags!")
        elif risk_score > 40:
            st.warning("**SUSPICIOUS** - Be careful!")
        else:
            st.success("**LOOKS OK** - No obvious red flags detected")


if __name__ == "__main__":
    main()
