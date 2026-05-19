import streamlit as st

st.set_page_config(
    page_title="AI Lab Calculation Coach",
    layout="wide"
)

st.title("AI Lab Calculation Coach")

st.write("""
Welcome to the AI-guided chemistry lab assistant.

This tool helps students:
- organize raw data
- set up calculations
- check unit consistency
- receive scaffolded hints
- improve scientific reasoning

The AI will not provide direct final answers.
""")

lab = st.selectbox(
    "Choose a lab module",
    [
        "Lab 1",
        "Lab 2",
        "Lab 3"
    ]
)

st.header(lab)

st.subheader("Step 1: Enter Raw Data")

raw_data = st.text_area(
    "Enter measurements, observations, and values:"
)

st.subheader("Step 2: Show Calculation Setup")

setup = st.text_area(
    "Show your equation setup and unit conversions:"
)

if st.button("Get Hint"):

    if "mL" in setup and "L" not in setup:
        st.warning(
            "Hint: Check whether all volume units are in the correct form before calculating."
        )

    else:
        st.info(
            "Hint: Verify that your units cancel properly and that your equation matches the quantities you identified."
        )
