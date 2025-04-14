# 🧠 Image-Captionz (AI-Powered Quote Generator Backend)

This repository contains the backend for the **AI-Powered Quote Generator** – a web-based application that generates unique, inspirational quotes using a fine-tuned GPT-2 model. The model was trained on a dataset of 500,000 quotes, and the backend supports generating, testing, and managing the quote generation process.

## 🚀 Features

- Generate AI-based motivational and inspirational quotes
- Fine-tuned GPT-2 model for contextual quote generation
- REST API powered by Flask (or FastAPI, if applicable)
- Easy integration with frontend/UI

## 📁 Project Structure

```
├── .idea/                      # IDE-specific settings
├── app.py                      # Main application file
├── Data collection.ipynb       # Data scraping or preparation notebook
├── requirements.txt            # Python dependencies
├── test.py                     # Testing script
├── tempCodeRunnerFile.python   # Temporary code (optional to keep)
├── README.md                   # Project overview
```

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/<your-username>/image-captionz.git
cd image-captionz
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## ▶️ Running the App

```bash
python app.py
```

The backend will start running on `http://127.0.0.1:5000/` (or the defined port).

## 🧪 Testing

You can run test scripts or notebooks like `test.py` or `Data collection.ipynb` to verify functionality or preprocess data.

## 📄 Requirements

All dependencies are listed in `requirements.txt`. Notable libraries may include:
- `transformers`
- `flask`
- `torch`
- `pandas`

## 📚 Authors

- Suyash Tambe
- Sneh Patel
- Shreyasee Shinde

## 📌 Notes

- This repo focuses on **backend** logic, data handling, and AI model integration.
- For frontend, see the corresponding UI repo (if applicable).
