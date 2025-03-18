import streamlit as st
import random

def main():
    st.set_page_config(page_title="Guess the Number Game", page_icon="🎲")
    st.title("🎲 Guess the Number Game")

    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

    st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.number:
            st.write("📉 Too low! Try again.")
        elif guess > st.session_state.number:
            st.write("📈 Too high! Try again.")
        else:
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state.number} in {st.session_state.attempts} attempts.")
            st.session_state.number = random.randint(1, 100)  # Reset for a new game
            st.session_state.attempts = 0


if __name__ == "__main__":
    main()
