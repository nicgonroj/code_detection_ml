from sklearn.externals import joblib
#import re
from pathlib import Path

__version__ = "1.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/random_forest_classifier-{__version__}.pkl", "rb") as f:
    model = joblib.load(f)



stop_words = joblib.load('stopwords.pkl')
tfidf_vectorizer = joblib.load('model/tfidf_vectorizer-1.1.0.pkl')


def predict_pipeline(text):
    text= text.apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))
    text = text.upper()
    text = tfidf_vectorizer.fit_transform(text)    
    pred = model.predict([text])
    return pred
