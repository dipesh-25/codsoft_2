import streamlit as st


st.title("Simple Calculator")


num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")


operation = st.selectbox("Choose an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))


def calculate(n1, n2, op):
    if op == "Addition":
        return n1 + n2
    elif op == "Subtraction":
        return n1 - n2
    elif op == "Multiplication":
        return n1 * n2
    elif op == "Division":
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero"


if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.subheader(f"Result: {result}")
