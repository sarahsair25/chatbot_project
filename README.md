
<img width="1536" height="1024" alt="flask NLP chatbot" src="https://github.com/user-attachments/assets/8c25675b-e976-4c7a-ba49-7ce3c1522037" />


# Flask Chatbot

A simple web-based chatbot built with Flask.

## How to Run

1) Clone the repository:
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

    Create a virtual environment:

Windows (PowerShell)

python -m venv .venv
.venv\Scripts\Activate.ps1

macOS/Linux

python3 -m venv .venv
source .venv/bin/activate

    Install dependencies:

pip install -r requirements.txt

    Run the app:

python app.py

Open:

    http://127.0.0.1:5000

Project Structure

chatbot_project/
├── app.py
├── chatbot.py
├── corpus.txt
├── templates/
│   └── index.html
└── static/
    └── style.css


---

## 5) Push to GitHub
In the project folder:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main

### Download NLTK data (first run only)
Run this once:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('omw-1.4')"

Data: Text corpus (corpus.txt)
<img width="1536" height="1024" alt="ChatGPT Image Dec 29, 2025, 01_27_48 PM" src="https://github.com/user-attachments/assets/f0378313-379c-476d-9aa7-a6ee6ab6a112" />





Built to practice backend development, applied NLP, and clean Python architecture, with an emphasis on clarity, reliability, and real-world integration rather than model complexity.
