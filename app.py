
import streamlit as st

# App title
st.title("Grade Calculator")
st.write("Calculate your test percentage!")

# Get marks from the user
mark = st.number_input("Enter marks scored:", min_value=0)

total = st.number_input("Enter total marks:", min_value=1)

# Calculate button
if st.button("Calculate Percentage"):

    # Calculate percentage
    percentage = (mark / total) * 100

    # Display percentage
    st.success(f"You got: {percentage:.2f}%")

    # Give an automatic comment
    if percentage >= 90:
        comment = "Keep it up, Ayush !"

    elif percentage >= 80:
        comment = "Good shit yo!"

    elif percentage >= 70:
        comment = "Starting to lose track"

    elif percentage >= 60:
        comment = "Come on you got this!"

    elif percentage >= 50:
        comment = "okay dude wtf!"

    else:
        comment = "More studying is needed!"

    # Display comment
    st.write(comment)
