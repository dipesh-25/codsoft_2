import streamlit as st
import random


if 'user_score' not in st.session_state:
    st.session_state['user_score'] = 0

if 'computer_score' not in st.session_state:
    st.session_state['computer_score'] = 0

if 'round' not in st.session_state:
    st.session_state['round'] = 1

st.title("Rock - Paper - Scissors Game")

st.write("Choose Rock, Paper, or Scissors to play against the computer.")

choices = ["Rock", "Paper", "Scissors"]

user_choice = st.radio("Your Move:", choices, horizontal=True)

if st.button("Play Round"):
    
    computer_choice = random.choice(choices)

    
    st.subheader(f"Round {st.session_state['round']}")
    st.write(f"You chose: **{user_choice}**")
    st.write(f"Computer chose: **{computer_choice}**")

    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        result = "You win!"
        st.session_state['user_score'] += 1
    elif user_choice == "Paper" and computer_choice == "Rock":
        result = "You win!"
        st.session_state['user_score'] += 1
    elif user_choice == "Scissors" and computer_choice == "Paper":
        result = "You win!"
        st.session_state['user_score'] += 1
    else:
        result = "You lose!"
        st.session_state['computer_score'] += 1

    
    st.success(result)

   
    st.session_state['round'] += 1

    
    st.write(f"Score: You - {st.session_state['user_score']} | Computer - {st.session_state['computer_score']}")

if st.button("Reset Game"):
    st.session_state['user_score'] = 0
    st.session_state['computer_score'] = 0
    st.session_state['round'] = 1
    st.info("Game reset. Start again!")
