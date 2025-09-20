import streamlit as st
import re

# Page config
st.set_page_config(
    page_title="BankEasy",
    page_icon="🛡️",
    layout="centered"
)


def main():
    st.title("🛡️ BankEasy")
    st.subheader("Your All-in-One Banking Companion") 
    st.write("**Protect yourself from fraud and master your finances, all in one simple app**")
    


if __name__ == "__main__":
    main()
