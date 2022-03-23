import streamlit as st
import joblib
st.title("SPAM HAM CLASSIFIER")
text_model=joblib.load('spam-ham')
ip=st.text_input("Enter your message: ")
op=text_model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
