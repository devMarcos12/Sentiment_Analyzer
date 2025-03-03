import joblib
import pandas as pd

model = joblib.load("models/naive_bayes_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def predict_sentiment(review_text):
    review_vectorized = vectorizer.transform([review_text])
    prediction = model.predict(review_vectorized)[0]
    sentiment = "positivo" if prediction == 1 else "negativo"
    return sentiment

new_reviews = [
    "Esse filme foi simplesmente incrível, adorei cada segundo!",
    "O pior filme que já vi, história fraca e atuação péssima.",
    "Gostei bastante, mas achei um pouco longo demais.",
    "Horrível, não recomendo para ninguém!",
    "Muito ruim, com certeza assistiria de novo!"
]

for review in new_reviews:
    sentiment = predict_sentiment(review)
    print(f"Avaliação: {review}\nSentimento previsto: {sentiment}\n")
