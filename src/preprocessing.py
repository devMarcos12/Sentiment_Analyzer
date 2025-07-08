import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

dataset_raw_path = "data/raw/dataset.csv"
dataset_clean_path = "data/processed/dataset_clean.csv"
dataset_preprocessed_path = "data/processed/dataset_preprocessed.csv"

df = pd.read_csv(dataset_raw_path, delimiter=",", encoding="utf-8", quotechar='"')

# Keep only relevant columns
df = df.iloc[:, [2, 3]]
df.columns = ["review", "sentiment"]

df["sentiment"] = df["sentiment"].replace({"neg": "negativo", "pos": "positivo", "0": "negativo", "1": "positivo"})

df = df.drop_duplicates().dropna()
print(f"Dataset cleaned: {df.shape[0]} reviews.")

df.to_csv(dataset_clean_path, index=False, encoding="utf-8")
print(f"Clean dataset saved at: {dataset_clean_path}")

df = pd.read_csv(dataset_clean_path, encoding="utf-8")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-záéíóúãõâêôç ]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('portuguese'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

df['review'] = df['review'].apply(preprocess_text)

df.to_csv(dataset_preprocessed_path, index=False, encoding="utf-8")
print(f"Preprocessed dataset saved at: {dataset_preprocessed_path}")
