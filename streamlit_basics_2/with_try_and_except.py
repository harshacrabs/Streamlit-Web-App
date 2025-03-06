import streamlit as st

col_1,col_2 = st.columns(2)

with col_1:
    number_1 = st.number_input('Please enter first number', value=0, step=1)

with col_2:
    number_2 = st.number_input("Please enter the second number", value=0, step=1)


try:
    st.info(f'**{number_1}/{number_2}=** {number_1/number_2}')
except Exception as e:
    st.error(f'**Error:** {e}')



