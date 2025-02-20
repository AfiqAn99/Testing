import streamlit as st
import pandas as pd

# Load tweet data
data = pd.read_excel('Book1.xlsx')

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.cyberbullying_count = 0
    st.session_state.non_cyberbullying_count = 0

# Display the current tweet
if st.session_state.index < len(data):
    tweet = data.iloc[st.session_state.index]["Tweet"]
    st.write("**Tweet:**")
    st.write(tweet)

    col1, col2 = st.columns(2)

    # Swipe buttons
    with col1:
        if st.button("Swipe Left (Not Cyberbullying)"):
            if data.iloc[st.session_state.index]["Cyberbullying"] == False:
                st.session_state.non_cyberbullying_count += 1
            st.session_state.index += 1

    with col2:
        if st.button("Swipe Right (Cyberbullying)"):
            if data.iloc[st.session_state.index]["Cyberbullying"] == True:
                st.session_state.cyberbullying_count += 1
            st.session_state.index += 1
else:
    st.write("End of Tweets! Thanks for playing.")
    st.write(f"Cyberbullying tweets identified: {st.session_state.cyberbullying_count}")
    st.write(f"Non-cyberbullying tweets identified: {st.session_state.non_cyberbullying_count}")
