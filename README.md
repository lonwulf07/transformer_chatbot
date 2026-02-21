# 🤖 Transformer Chatbot using Blended Skill Talk

A full production‑ready conversational AI chatbot built using Hugging
Face Transformers, trained on the Blended Skill Talk dataset, deployed
with Streamlit, containerized using Docker, and version‑controlled with
GitHub.

------------------------------------------------------------------------

# 📌 Project Overview

This project demonstrates how to:

• Train a conversational Transformer model\
• Use a real‑world dialogue dataset\
• Deploy using Streamlit\
• Containerize using Docker\
• Prepare production‑ready AI project

------------------------------------------------------------------------

# 🧠 Dataset

Dataset used:

Blended Skill Talk

Features:

• Human‑like conversations\
• Multi‑turn dialogue\
• Emotional and contextual responses

------------------------------------------------------------------------

# ⚙️ Tech Stack

Python\
PyTorch\
Hugging Face Transformers\
Streamlit\
Docker

------------------------------------------------------------------------

# 📁 Project Structure


transformer_chatbot/
│
├── app/
│   └── streamlit_app.py
│
├── models/
│   └── chatbot-model/
│
├── notebooks/
│   └── training.ipynb
│
├── src/
│   └── inference.py
│
├── Dockerfile
├── requirements.txt
├── README.md


------------------------------------------------------------------------

# 🚀 Training

Training was done using Google Colab GPU.

Steps:

• Load dataset\
• Format conversation\
• Tokenize\
• Train GPT‑2 model\
• Save model

------------------------------------------------------------------------

# 💬 Run Locally

Install dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app/streamlit_app.py

Open browser:

http://localhost:8501

------------------------------------------------------------------------

# 🐳 Run using Docker

Build Image:

docker build -t transformer-chatbot .

Run Container:

docker run -p 8501:8501 transformer-chatbot

------------------------------------------------------------------------

# 🧪 Example

User: Hello

Bot: Hi! How are you today?

------------------------------------------------------------------------

# 📊 Features

Transformer based chatbot\
Real conversation dataset\
Streamlit UI\
Docker support\
Production ready

------------------------------------------------------------------------

# 🎯 Future Improvements

Better fine‑tuning\
Use larger models\
Deploy on cloud

------------------------------------------------------------------------

# 👨‍💻 Author

Mohit Sharma

------------------------------------------------------------------------

# ⭐ If you like this project, please star the repository!
