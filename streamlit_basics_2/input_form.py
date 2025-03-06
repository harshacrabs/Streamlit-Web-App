import streamlit as st


with st.form('feedback_form'):
    st.header("Feedback Form")
# Creating columns to organize the form
    col_1,col_2 = st.columns(2)

    with col_1:
        name = st.text_input("Please enter your name")
        rating = st.slider('Please rate this channel', 0,10,5)

    with col_2:
        dob = st.date_input("Please enter your date of birth")
        recommend = st.radio("Would you recommend this channel to others?", ("Yes", "No"))

        submit_button = st.form_submit_button('Submit')

if submit_button:
    st.write('**Name:**', name, '**Date of Birth**:', dob,
             '**Rating**:',rating, 
             '**Would Recommend**', recommend)
