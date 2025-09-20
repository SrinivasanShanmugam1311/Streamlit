import streamlit as st

# Title
st.title("🧮 BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.5)
height = st.number_input("Enter your height (m):", min_value=0.5, step=0.01)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    
    # Categorize BMI
    if bmi < 16:
        category = "Severe Thinness"
    elif bmi < 17:
        category = "Moderate Thinness"
    elif bmi < 18.5:
        category = "Mild Thinness"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    elif bmi < 35:
        category = "Obese Class I"
    elif bmi < 40:
        category = "Obese Class II"
    else:
        category = "Obese Class III"

    # Show result
    st.success(f"Your BMI is **{bmi:.2f}** → {category}")
