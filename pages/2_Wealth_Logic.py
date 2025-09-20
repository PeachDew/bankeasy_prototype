

import streamlit as st
import re
import random

# Page config
st.set_page_config(
    page_title="BankEasy - Wealth Logic",
    page_icon="🔎",
    layout="centered"
)


def main():
    st.title("💰 Wealth Logic")
    st.markdown("""
# Investing Basics in the Philippines
## Why Invest Instead of Just Saving?
- Protect your money from inflation  
  Prices of goods in the Philippines rise 3–5% yearly. Regular savings accounts typically earn less than 1%.  
- Grow wealth over time  
  Investing lets you earn from interest, dividends, or asset growth.  
- Reach your life goals  
  A comfortable retirement, your child’s education, or a future home.  

---

## Core Principles to Live By
1. Start early → Compounding works better with more time.  
2. Set a clear goal → Short-term (1–3 years), medium-term (3–7 years), long-term (7+ years).  
3. Diversify → Mix safer assets (bonds, deposits) and growth assets (stocks, equity funds).  
4. Know your risk appetite → Conservative, moderate, or aggressive.  

---

## Investment Options in the Philippines

### 1. Bank Savings & Time Deposits
- Very safe, insured by PDIC up to ₱500,000  
- Good for emergency funds  
- Low returns (1–3%)  

---

### 2. Bonds
- Government Bonds (e.g., RTBs, Premyo Bonds): backed by PH government, fixed returns, minimum ₱5,000  
- Corporate Bonds: usually higher interest but higher risk  

---

### 3. Stocks
- Shares of companies listed in the PSE  
- High risk, high potential returns  
- Suited for long-term investors willing to handle market volatility  

---

### 4. Mutual Funds & UITFs
- Pooled investments managed by professionals  
- Available in banks and investment companies  
- Types: Equity (stocks), Bond, Balanced, Money Market  

---

### 5. Real Estate
- Property value tends to rise long term  
- Can generate rental income  
- Requires larger capital and management  

---

### 6. Pag-IBIG MP2 Program
- Government-backed, voluntary savings program  
- Historically 6–8% annual returns, tax-free  
- Fixed 5-year term  

---

## Starter Roadmap
1. Build emergency savings and pay off high-interest debt  
2. Begin with Pag-IBIG MP2 and bond funds  
3. Add equity funds or selected PSE stocks for long-term growth  
4. Consider real estate or starting a business once you have larger capital  
                """)

if __name__ == "__main__":
    main()
