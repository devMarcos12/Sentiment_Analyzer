from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import os

router = APIRouter()

# Define paths for both Docker and local environments
DOCKER_MODEL_PATH = "/app/models/naive_bayes_model.pkl"
DOCKER_VECTORIZER_PATH = "/app/models/tfidf_vectorizer.pkl"
LOCAL_MODEL_PATH = "../../src/models/naive_bayes_model.pkl"
LOCAL_VECTORIZER_PATH = "../../src/models/tfidf_vectorizer.pkl"

# Check for models in Docker environment first
if os.path.exists(DOCKER_MODEL_PATH) and os.path.exists(DOCKER_VECTORIZER_PATH):
    model = joblib.load(DOCKER_MODEL_PATH)
    vectorizer = joblib.load(DOCKER_VECTORIZER_PATH)
# If not found, check for models in local environment
elif os.path.exists(LOCAL_MODEL_PATH) and os.path.exists(LOCAL_VECTORIZER_PATH):
    model = joblib.load(LOCAL_MODEL_PATH)
    vectorizer = joblib.load(LOCAL_VECTORIZER_PATH)
# If no models are found in either path, raise an error
else:
    raise FileNotFoundError(
        "Model or vectorizer not found. Searched in: "
        f"Docker path ('{DOCKER_MODEL_PATH}') and "
        f"Local path ('{LOCAL_MODEL_PATH}')"
    )

class ReviewInput(BaseModel):
    text: str = ""

@router.post("/predict/")
def predict_sentiment(review: ReviewInput):
    if not review.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty")
    
    text_vectorized = vectorizer.transform([review.text])
    prediction = model.predict(text_vectorized)[0]
    sentiment = "Positive" if prediction == 1 else "Negative"
    return {"sentiment": sentiment}