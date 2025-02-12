import streamlit as st
import joblib

import warnings
warnings.filterwarnings('ignore')

# Cache the model and vectorizer so they are loaded only once
@st.cache_resource
def load_model():
    # Load your model and vectorizer using joblib
    model = joblib.load('model.joblib')
    vectorizer = joblib.load('tfidf.joblib')
    return model, vectorizer

# Load the model and vectorizer once at the start
model, vectorizer = load_model()

# Mapping of numeric labels to sentiment names
label_map = {
    0: "Irrelevant",
    1: "Negative",
    2: "Neutral",
    3: "Positive"
}

# Create Streamlit App
st.image('download.jpeg')
st.title("Twitter Tweets Sentiment Analyser")

# Display the sentiment labels for the user
st.write("### Sentiment Labels:")
st.write("0: Irrelevant")
st.write("1: Negative")
st.write("2: Neutral")
st.write("3: Positive")

st.write("Enter the tweet below to predict its sentiment:")

tweet = st.text_area("Tweet:")

if st.button("Predict"):
    if not tweet:
        st.error("Not a valid tweet")
    else:
        # Transform the input tweet using the loaded vectorizer
        vector = vectorizer.transform([tweet])
        
        # Predict the sentiment using the loaded model
        sentiment_prediction = model.predict(vector)[0]
        
        # Map the prediction to the sentiment label
        sentiment = label_map[sentiment_prediction]

        #Display the predicted sentiment
        st.success(f"Predicted Sentiment: {sentiment}")   
        
st.image('download (1).jpeg')
