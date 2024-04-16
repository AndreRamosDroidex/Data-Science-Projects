import streamlit as st
import pickle
import time

custom_css = """
<style>
body {
    background-color: #E1AFD1; /* Set your desired background color */
}
</style>
"""
st.set_page_config(page_title="Twitter Sentiment Predict", layout="wide", page_icon="🚀", initial_sidebar_state="expanded")

st.markdown(custom_css, unsafe_allow_html=True)
st.title("Twitter Sentiment Analysis")

# load_model
model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

tweet = st.text_input("Enter yout text")
submit = st.button("Predict")

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Predicction time taken: ', round(end-start, 2), ' seconds')
    print(prediction[0])
    st.write(prediction[0])