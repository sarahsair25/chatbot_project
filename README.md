# chatbot_project
Flask NLP Chatbot 🤖A web-ba
What It Does

Accepts user messages via a Flask API

Processes text using NLTK (tokenization & lemmatization)

Generates responses using TF-IDF + cosine similarity

Returns results to a simple HTML/CSS frontend

Tech Stack

Backend: Python, Flask

NLP / ML: NLTK, scikit-learn (TF-IDF, cosine similarity)

Frontend: HTML, CSS

Data: Text corpus (corpus.txt)
<img width="1536" height="1024" alt="ChatGPT Image Dec 29, 2025, 01_27_48 PM" src="https://github.com/user-attachments/assets/f0378313-379c-476d-9aa7-a6ee6ab6a112" />

Key Features

Clean REST-style Flask API (/chat)

Text preprocessing pipeline (normalization, lemmatization, stop-word removal)

Defensive input handling & edge-case protection

GitHub-ready, maintainable project structure

Easily extensible to transformer-based models or deployment platforms

Project Structure
chatbot_project/
├── app.py
├── chatbot.py
├── corpus.txt
├── templates/
│   └── index.html
└── static/
    └── style.css



Built to practice backend development, applied NLP, and clean Python architecture, with an emphasis on clarity, reliability, and real-world integration rather than model complexity.
