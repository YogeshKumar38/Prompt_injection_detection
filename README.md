# 🔐 Prompt Injection Detection System

An end-to-end Machine Learning project designed to detect **prompt injection attacks** in user inputs before they reach an AI system.

This project acts as a **security layer for LLM-based applications**, helping prevent malicious prompts from manipulating AI behavior.

---

## 🚀 Features

* Detects malicious vs benign prompts
* Clean ML pipeline (data → preprocessing → training → evaluation)
* Modular and scalable structure
* Dataset handled externally (Google Drive)
* Real-world AI security use case

---

## 🧠 Problem Statement

Prompt injection is a major vulnerability in AI systems where users can manipulate model behavior using specially crafted inputs.

This project classifies prompts as:

* **Malicious (1)** → Injection attempts
* **Benign (0)** → Normal prompts

---

## 🏗️ Project Structure

```
Prompt_Injection_Detection/
│
├── data/
├── src/
├── outputs/
├── legacy/
│   ├── app.py
│   └── keywords.json
│
├── README.md
└── .gitignore
```

---

## 📊 Dataset

Due to size limitations, the dataset is not included in this repository.

👉 **Download Dataset from Google Drive:**
https://drive.google.com/drive/folders/175Lkyp5oDie1I_MHw1JlpuIoBJd1FXgd?usp=drive_link

### 📁 Dataset Files

* `malicious_prompts_dataset.csv`
* `Benign_prompts_dataset.csv`

---

## 🧾 Dataset Description

This is a **hybrid NLP dataset** created by:

* Merging multiple public datasets
* Cleaning and standardizing text
* Removing duplicates and noise

### 🧠 Data Type

* Domain: **AI Security / Prompt Injection**
* Task: **Text Classification**

---

## ⚙️ How It Works

1. Load both datasets
2. Assign labels
3. Merge datasets
4. Shuffle data
5. Train model
6. Predict output

---

## 🧑‍💻 Usage Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YogeshKumar38/Prompt_injection_detection.git
cd Prompt_injection_detection
```

---

### 2. Download Dataset

* Download from Google Drive
* Place inside `data/`

```
data/
├── malicious_prompts_dataset.csv
└── Benign_prompts_dataset.csv
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Project

```bash
python src/main.py
```

---

## 📈 Future Improvements

* Add ML models
* Add Deep Learning (BERT)
* Build API (Flask / FastAPI)
* Add frontend UI
* Deploy system

---

## ⚠️ Dataset Disclaimer

This dataset is a **derived dataset**:

* No raw datasets redistributed
* Credit belongs to original creators
* Used for research and educational purposes

---

## 💡 Why This Project Matters

Prompt injection is a serious AI security threat.

This project demonstrates:

* AI security understanding
* ML implementation
* Real-world problem solving

---

## 👨‍💻 Author

**Yogesh Kumar**

---

## ⭐ Support

* Star the repo
* Fork it
* Share it

---

## 📬 Contact

GitHub: https://github.com/YogeshKumar38
