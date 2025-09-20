import streamlit as st
from datetime import date

# Title
st.title("🎂 Age Calculator")

# Limit range (1980 → today)
min_date = date(1980, 1, 1)
max_date = date.today()

# Input: Date of Birth with range
dob = st.date_input("Select your Date of Birth:", 
                    min_value=min_date, 
                    max_value=max_date)

# Button to calculate age
if st.button("Calculate Age"):
    today = date.today()
    
    # Calculate age
    age = today.year - dob.year 
    
    # Show result
    st.success(f"Your age is: **{age} years**")
