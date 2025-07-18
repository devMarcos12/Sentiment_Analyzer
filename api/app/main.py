from fastapi import FastAPI
from routes import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sentiment Analysis API", description="API for predicting sentiment of movie reviews.", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router)
