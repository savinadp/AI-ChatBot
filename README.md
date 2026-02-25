# Welcome to Savina's AI World...

This is a chatbot that runs entirely **locally** using Ollama and FastAPI. No API keys. No cloud costs. No external dependencies for inference.

## 🚀 Features

- 💬 ChatGPT-style web interface
- 🧠 Runs fully locally using Ollama
- 🔐 No API keys required
- ⚡ Supports multiple models (llama3, deepseek, etc.)
- 🖥️ Lightweight FastAPI backend
- 🧩 Easy to set up and run

# 📦 Requirements

- Python 3.10+
- Ollama is installed on your system
- 8GB+ RAM recommended (16GB ideal) 

## 🔧 Installation
### ✅ Install Ollama

Download and install from:
https://ollama.com

###  ✅ Pull a Model

ollama pull llama3.1:8b-instruct-q4_0

###  ✅ Install Python Dependencies
pip install -r requirements.txt

### ▶️ Running the Application
Double-click: run.bat 

OR

Type on terminal --> python -m uvicorn app:app --host 127.0.0.1 --port 8000 --> Then open in your browser: http://127.0.0.1:8000/

**Enjoy Local ChatBot. Cheers 🥂🥂**
<img width="2559" height="1269" alt="Screenshot 2026-02-24 234033" src="https://github.com/user-attachments/assets/30b5862f-5258-4989-8bb7-f94da9d1bf41" />
