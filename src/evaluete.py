import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load trained model and vectorizer
model = joblib.load("models/naive_bayes_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Load test dataset
df_test = pd.read_csv("data/processed/dataset_preprocessed.csv", encoding="utf-8")

# Convert text to numerical features
X_test = vectorizer.transform(df_test['review'])
y_test = df_test['sentiment'].map({'positivo': 1, 'negativo': 0})

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.4f}')
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Display Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
