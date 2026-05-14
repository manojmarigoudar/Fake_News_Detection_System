import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Title
st.title("Fake News Detection System")

st.write("Enter a news article below to check whether it is Real or Fake.")

# User input
news_text = st.text_area("Enter News Text")

# Predict button
if st.button("Check News"):

    # Convert text into vector
    news_vector = vectorizer.transform([news_text])

    # Prediction
    prediction = model.predict(news_vector)

    # Output
    if prediction[0] == 1:
        st.success("This News is REAL")
    else:
        st.error("This News is FAKE")