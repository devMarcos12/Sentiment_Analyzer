from fastapi import FastAPI
from app.routes import predict

app = FastAPI(title="Sentiment Analysis API", description="API for predicting sentiment of movie reviews.", version="1.0")

app.include_router(predict.router)
