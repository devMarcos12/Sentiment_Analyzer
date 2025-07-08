# Sentiment Analyzer

This repository contains a complete Sentiment Analysis project, utilizing Machine Learning and a Frontend interface for user interaction. The project was developed to study and implement machine learning models to classify sentiments based on texts extracted from the internet.

## Objectives

### General

The main objective of this project is to analyze sentiments in texts written in Portuguese, classifying them as positive or negative.

### Specific

* Collect and clean a sentiment analysis dataset;
* Apply text preprocessing to improve data quality;
* Train and evaluate a Naïve Bayes model for sentiment classification;
* Create an API using FastAPI to make the trained model available;
* Build a React interface for interaction with the model.

### Technologies Used

* Scikit-learn (for Machine Learning model training)
* FastAPI (for API creation)
* NLTK (for natural language processing)
* React.js (for the application frontend)
* Docker (for application containerization)

## Model Performance

![accuracy](https://github.com/user-attachments/assets/5f1a847c-dfe5-42ac-be4d-c64fe822b89f)

## How to run the project (with Docker)

1. Required Folder Structure

Before starting, create the following folder structure inside the src directory:

```
src/
  data/
    raw/
    processed/
  models/
```

2. Download the Dataset

https://www.kaggle.com/datasets/luisfredgs/imdb-ptbr/code

Rename the downloaded file to dataset.csv and place it inside the src/data/raw/ folder.

Your final path should look like this:

src/data/raw/dataset.csv

### Training the Model with Docker

First, build the training image:

```bash
docker build -t sentiment-analyzer-training src/
```

### Preprocessing Data

This command runs the preprocessing script. It mounts the `data` directory from your local machine into the container, so the script can read the raw dataset and save the processed files back to your machine.

```bash
docker run --rm -v $(pwd)/src/data:/app/data sentiment-analyzer-training preprocessing.py
```

### Training the Model

This command runs the training script. It mounts the `data` directory to access the preprocessed data and the `models` directory to save the trained model files.

```bash
docker run --rm -v $(pwd)/src/data:/app/data -v $(pwd)/src/models:/app/models sentiment-analyzer-training train.py
```

### Backend (API)

1.  **Build the Docker image:**
    ```bash
    docker build -t sentiment-analyzer-api api/
    ```

2.  **Run the container:**
    ```bash
    docker run -d -p 8000:8000 -v $(pwd)/models:/app/models sentiment-analyzer-api
    ```

### Frontend (React App)

1.  **Build the Docker image:**
    ```bash
    docker build -t sentiment-analyzer-interface interface/
    ```
    *Note: The Dockerfile has been updated to use `node:18` and `npm audit fix --force` to ensure dependencies are secure and up-to-date.*

2.  **Run the container:**
    ```bash
    docker run -d -p 3000:3000 sentiment-analyzer-interface
    ```

Access the application at [http://localhost:3000](http://localhost:3000).
