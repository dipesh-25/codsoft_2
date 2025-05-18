import streamlit as st
import random
import string


st.title(" Password Generator")


length = st.number_input(
    label="Enter password length",
    min_value=4,
    max_value=64,
    value=12,
    help="Choose how many characters your password should have"
)

include_special_chars = st.checkbox("Include special characters (e.g., !, @, #, *)", value=True)


def generate_password(length, use_special):
    try:
        chars = string.ascii_letters + string.digits
        if use_special:
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
    except Exception as error:
        return f" Error generating password: {error}"

if st.button("Generate Password"):
    password = generate_password(length, include_special_chars)
    st.success("Generated Password:")
    st.code(password)
