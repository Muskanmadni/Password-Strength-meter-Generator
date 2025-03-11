import streamlit as st

import random

st.title('Password strength Meter And Generator')
st.write('Please enter your password below to check its strength and suggest a strong password')


# Password strength meter

password = st.text_input('Password', type='password')

if password:
    st.write('Password length minimum 8 characters:', len(password))
    st.write('Password has uppercase:', any(c.isupper() for c in password))
    st.write('Password has lowercase:', any(c.islower() for c in password))
    st.write('Password has digits:', any(c.isdigit() for c in password))
    st.write('Password has special characters:', any(not c.isalnum() for c in password))
    st.write('Password strength:', 'Strong' if len(password) >= 8 else 'Weak')

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    suggested_password = ''.join(random.choices(characters, k=12))
    st.write('Suggested strong password:', suggested_password)


    if len(password) >= 8:
        st.write('Password is strong')
    else:
        st.write('Password is weak')
else: 
    st.write('Please enter a password')

st.write('made with ❤️ by Umm e Habiba Madni')