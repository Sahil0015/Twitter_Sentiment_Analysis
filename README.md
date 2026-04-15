# Twitter Sentiment Analysis

This project predicts the sentiment of a tweet using a Streamlit application backed by a trained machine learning model.

The repository contains both the training notebook and the lightweight application artifacts needed to run inference:

- `Sentiment_Analyser.ipynb` builds the dataset pipeline, trains the models, and exports the final artifacts.
- `app.py` loads the saved model and vectorizer and exposes a simple Streamlit interface.
- `model.joblib` stores the trained classifier used by the app.
- `tfidf.joblib` stores the fitted TF-IDF vectorizer used to transform tweet text.
- `twitter_sentiment.csv` is the source dataset used in the notebook.

## What the app does

The app accepts a tweet as input and returns one of four labels:

- `Irrelevant`
- `Negative`
- `Neutral`
- `Positive`

The displayed labels match the numeric encoding used in the training notebook:

- `0` = Irrelevant
- `1` = Negative
- `2` = Neutral
- `3` = Positive

## How the notebook works

The notebook follows a standard sentiment analysis workflow:

1. Load the dataset from `twitter_sentiment.csv`.
2. Keep the sentiment and tweet text columns.
3. Remove missing values and duplicate rows.
4. Explore the data with class counts, summary statistics, histograms, KDE plots, and word clouds.
5. Clean the text with NLTK-based preprocessing.
6. Convert the cleaned text into TF-IDF features.
7. Encode the sentiment labels.
8. Split the data into training and test sets.
9. Train several classifiers and compare their accuracy and precision.
10. Evaluate ensemble approaches such as voting and stacking.
11. Save the final model to `model.joblib` and the vectorizer to `tfidf.joblib`.

## Text preprocessing

The notebook’s preprocessing function removes or normalizes several common noise sources in tweets:

- retweet markers such as `RT`
- URLs
- HTML tags
- simple emoji patterns
- punctuation and non-word characters
- stop words
- inflected word forms through stemming

This gives the model a cleaner text representation before vectorization.

## Model pipeline

The inference flow in `app.py` mirrors the training pipeline:

1. Load the saved TF-IDF vectorizer.
2. Transform the user’s tweet into numeric features.
3. Load the trained classifier.
4. Predict the sentiment label.
5. Convert the numeric prediction back to a human-readable class name.

## Project structure

- `app.py` - Streamlit application for live sentiment prediction.
- `Sentiment_Analyser.ipynb` - Full exploration, training, and model export notebook.
- `twitter_sentiment.csv` - Source dataset.
- `model.joblib` - Saved sentiment classifier.
- `tfidf.joblib` - Saved TF-IDF vectorizer.
- `requirements.txt` - Python dependencies.
- `download.jpeg` - Top banner image used by the app.
- `download (1).jpeg` - Bottom banner image used by the app.

## Requirements

Install the dependencies listed in `requirements.txt`.

Typical runtime packages include:

- `streamlit`
- `scikit-learn`
- `numpy`
- `pandas`
- `nltk`
- `xgboost`
- `wordcloud`
- `matplotlib`
- `seaborn`

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure the following files are present in the project root:

```text
app.py
model.joblib
tfidf.joblib
twitter_sentiment.csv
```

## Run the app

Start the Streamlit app from the project root:

```bash
streamlit run app.py
```

Then paste a tweet into the text box and click `Predict`.

## Retrain the model

If you want to rebuild the saved artifacts:

1. Open `Sentiment_Analyser.ipynb`.
2. Run the notebook from top to bottom.
3. Allow the notebook to complete the export cells that generate `model.joblib` and `tfidf.joblib`.

## Notes

- The application is designed for inference only; training happens in the notebook.
- The notebook expects NLTK resources such as `punkt` and `stopwords`.
- The repository already includes the exported model files, so the app can run without retraining.
# Twitter Sentiment Analysis

This project predicts the sentiment of a tweet using a Streamlit application backed by a trained machine learning model.

The repository contains both the training notebook and the lightweight application artifacts needed to run inference:

- `Sentiment_Analyser.ipynb` builds the dataset pipeline, trains the models, and exports the final artifacts.
- `app.py` loads the saved model and vectorizer and exposes a simple Streamlit interface.
- `model.joblib` stores the trained classifier used by the app.
- `tfidf.joblib` stores the fitted TF-IDF vectorizer used to transform tweet text.
- `twitter_sentiment.csv` is the source dataset used in the notebook.

## What the app does

The app accepts a tweet as input and returns one of four labels:

- `Irrelevant`
- `Negative`
- `Neutral`
- `Positive`

The displayed labels match the numeric encoding used in the training notebook:

- `0` = Irrelevant
- `1` = Negative
- `2` = Neutral
- `3` = Positive

## How the notebook works

The notebook follows a standard sentiment analysis workflow:

1. Load the dataset from `twitter_sentiment.csv`.
2. Keep the sentiment and tweet text columns.
3. Remove missing values and duplicate rows.
4. Explore the data with class counts, summary statistics, histograms, KDE plots, and word clouds.
5. Clean the text with NLTK-based preprocessing.
6. Convert the cleaned text into TF-IDF features.
7. Encode the sentiment labels.
8. Split the data into training and test sets.
9. Train several classifiers and compare their accuracy and precision.
10. Evaluate ensemble approaches such as voting and stacking.
11. Save the final model to `model.joblib` and the vectorizer to `tfidf.joblib`.

## Text preprocessing

The notebook’s preprocessing function removes or normalizes several common noise sources in tweets:

- retweet markers such as `RT`
- URLs
- HTML tags
- simple emoji patterns
- punctuation and non-word characters
- stop words
- inflected word forms through stemming

This gives the model a cleaner text representation before vectorization.

## Model pipeline

The inference flow in `app.py` mirrors the training pipeline:

1. Load the saved TF-IDF vectorizer.
2. Transform the user’s tweet into numeric features.
3. Load the trained classifier.
4. Predict the sentiment label.
5. Convert the numeric prediction back to a human-readable class name.

## Project structure

- `app.py` - Streamlit application for live sentiment prediction.
- `Sentiment_Analyser.ipynb` - Full exploration, training, and model export notebook.
- `twitter_sentiment.csv` - Source dataset.
- `model.joblib` - Saved sentiment classifier.
- `tfidf.joblib` - Saved TF-IDF vectorizer.
- `requirements.txt` - Python dependencies.
- `download.jpeg` - Top banner image used by the app.
- `download (1).jpeg` - Bottom banner image used by the app.

## Requirements

Install the dependencies listed in `requirements.txt`.

Typical runtime packages include:

- `streamlit`
- `scikit-learn`
- `numpy`
- `pandas`
- `nltk`
- `xgboost`
- `wordcloud`
- `matplotlib`
- `seaborn`

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure the following files are present in the project root:

```text
app.py
model.joblib
tfidf.joblib
twitter_sentiment.csv
```

## Run the app

Start the Streamlit app from the project root:

```bash
streamlit run app.py
```

Then paste a tweet into the text box and click `Predict`.

## Retrain the model

If you want to rebuild the saved artifacts:

1. Open `Sentiment_Analyser.ipynb`.
2. Run the notebook from top to bottom.
3. Allow the notebook to complete the export cells that generate `model.joblib` and `tfidf.joblib`.

## Notes

- The application is designed for inference only; training happens in the notebook.
- The notebook expects NLTK resources such as `punkt` and `stopwords`.
- The repository already includes the exported model files, so the app can run without retraining.
