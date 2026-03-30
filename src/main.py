import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ==============================
# 📁 HANDLE FILE PATHS PROPERLY
# ==============================
base_path = os.path.dirname(os.path.dirname(__file__))

malicious_path = os.path.join(base_path, "Data", "malicious_prompt_dataset.csv")
benign_path = os.path.join(base_path, "Data", "Benign_prompt_dataset.csv")

# ==============================
# 📥 LOAD DATASETS
# ==============================
malicious = pd.read_csv(malicious_path)
benign = pd.read_csv(benign_path)

# ==============================
# 🧹 CLEAN DATA (VERY IMPORTANT)
# ==============================

# Remove NaN values
malicious = malicious.dropna(subset=["Prompt"])
benign = benign.dropna(subset=["Prompt"])

# Remove empty strings
malicious = malicious[malicious["Prompt"].str.strip() != ""]
benign = benign[benign["Prompt"].str.strip() != ""]

# Reset index
malicious = malicious.reset_index(drop=True)
benign = benign.reset_index(drop=True)

# ==============================
# ⚖️ BALANCE DATASET (40k EACH)
# ==============================
malicious = malicious.sample(n=40000, random_state=42)
benign = benign.sample(n=40000, random_state=42)

# Merge datasets
data = pd.concat([malicious, benign]).reset_index(drop=True)

print("Total samples:", len(data))
print("Malicious:", len(malicious))
print("Benign:", len(benign))

# ==============================
# 🔀 SPLIT DATA
# ==============================
X = data["Prompt"]
y = data["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 🧠 TEXT VECTORIZATION
# ==============================
vectorizer = TfidfVectorizer(max_features=5000)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ==============================
# 🤖 TRAIN MODEL
# ==============================
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# ==============================
# 📊 EVALUATE MODEL
# ==============================
y_pred = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ==============================
# 💾 SAVE MODEL (IMPORTANT)
# ==============================
import pickle

model_path = os.path.join(base_path, "outputs", "model.pkl")
vectorizer_path = os.path.join(base_path, "outputs", "vectorizer.pkl")

# Create outputs folder if not exists
os.makedirs(os.path.join(base_path, "outputs"), exist_ok=True)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(vectorizer_path, "wb") as f:
    pickle.dump(vectorizer, f)

print("\n✅ Model and vectorizer saved in 'outputs/' folder")