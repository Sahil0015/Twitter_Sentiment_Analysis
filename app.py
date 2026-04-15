from pathlib import Path

import joblib
import streamlit as st

import warnings

warnings.filterwarnings("ignore")


APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "model.joblib"
VECTORIZER_PATH = APP_DIR / "tfidf.joblib"
TOP_IMAGE_PATH = APP_DIR / "download.jpeg"
BOTTOM_IMAGE_PATH = APP_DIR / "download (1).jpeg"

LABEL_MAP = {
    0: "Irrelevant",
    1: "Negative",
    2: "Neutral",
    3: "Positive",
}


st.set_page_config(
    page_title="Twitter Tweets Sentiment Analyser",
    page_icon="🐦",
    layout="centered",
)


@st.cache_resource
def load_model_assets():
    missing_assets = [path.name for path in (MODEL_PATH, VECTORIZER_PATH) if not path.exists()]
    if missing_assets:
        raise FileNotFoundError(f"Missing required asset(s): {', '.join(missing_assets)}")

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer


def render_sidebar() -> None:
    st.sidebar.title("Sentiment Labels")
    st.sidebar.write("0: Irrelevant")
    st.sidebar.write("1: Negative")
    st.sidebar.write("2: Neutral")
    st.sidebar.write("3: Positive")
    st.sidebar.caption("The app uses the saved TF-IDF vectorizer and trained model artifacts from this repository.")


def predict_sentiment(tweet: str, model, vectorizer) -> str:
    vector = vectorizer.transform([tweet])
    sentiment_prediction = model.predict(vector)[0]
    return LABEL_MAP.get(sentiment_prediction, "Unknown")


def main() -> None:
    render_sidebar()

    if TOP_IMAGE_PATH.exists():
        st.image(str(TOP_IMAGE_PATH), use_column_width=True)

    st.title("Twitter Tweets Sentiment Analyser")
    st.write("Enter a tweet below to predict whether it is irrelevant, negative, neutral, or positive.")

    tweet = st.text_area("Tweet:", placeholder="Type or paste a tweet here...")

    try:
        model, vectorizer = load_model_assets()
    except Exception as exc:
        st.error(f"Unable to load model assets: {exc}")
        st.stop()

    if st.button("Predict"):
        if not tweet:
            st.error("Not a valid tweet")
        else:
            try:
                with st.spinner("Predicting sentiment..."):
                    sentiment = predict_sentiment(tweet, model, vectorizer)
                st.success(f"Predicted Sentiment: {sentiment}")
            except Exception as exc:
                st.error(f"Prediction failed: {exc}")

    if BOTTOM_IMAGE_PATH.exists():
        st.image(str(BOTTOM_IMAGE_PATH), use_column_width=True)


if __name__ == "__main__":
    main()
