# NLP Web App (NER Edition)

A simple Flask web application that allows users to register, log in, and run **Named Entity Recognition (NER)** on input text using a RapidAPI NER API.  

---

## 📂 Project Structure

```
nlp_web_app_ner/
├── app.py
├── api.py
├── db.py
├── users.json
├── requirements.txt
└── templates/
    ├── login.html
    ├── register.html
    ├── profile.html
    └── ner.html
```

- **app.py** — main Flask web server, handles routing, user sessions, rendering templates  
- **api.py** — module for interacting with the RapidAPI Named Entity Recognition API  
- **db.py** — simple file‑based user database (using `users.json`)  
- **users.json** — stores registered users (email → [name, password])  
- **templates/** — HTML templates used by the Flask app  
- **requirements.txt** — list of Python dependencies  

---

## 🛠️ Features

- User registration (email + password)  
- User login / session management  
- Protected routes (NER page only accessible when logged in)  
- Named Entity Recognition (NER) using RapidAPI  
- Displays detected entities from input text  

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.7 or newer  
- A RapidAPI account and subscription to the Named Entity Recognition API  
- Your RapidAPI key

### Installation

```bash
# Clone the repository
git clone https://github.com/NagaRamya1531-tech/nlp_web_app_ner.git
cd nlp_web_app_ner

# (Recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate        # On macOS / Linux
venv\Scripts\activate           # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Setup your `users.json`

Create a `users.json` file in the project root with this content:

```json
{}
```

This ensures your user storage starts empty.

### Configure your RapidAPI key

In `api.py`, replace:

```python
API_KEY = "YOUR_RAPIDAPI_KEY"
```

with the key you get from your RapidAPI dashboard.

Also ensure:

```python
API_HOST = "namedentityrecognition.p.rapidapi.com"
```

is correct per your API subscription. (Double-check the “Host” value in the Playground/Code Snippet section.)

### Run the application

```bash
python app.py
```

By default, the server runs at http://127.0.0.1:5000 (or the port you specify).  
Open that URL in your browser.

---

## 🧪 Usage Flow

1. Open the app in browser → You see the login page  
2. Click “Register” → Create a new user  
3. Log in with your credentials  
4. Navigate to the **NER** page  
5. Enter a block of text → Submit → You’ll see extracted entities (e.g. persons, organizations, locations)  
6. Log out when done

---

## 🔐 Session / Security Notes

- The app uses **Flask sessions** to track login status (`session['logged_in']`)  
- You must set `app.secret_key` in `app.py` (a random string) to secure sessions  
- The database is file-based (`users.json`) and **not suitable for production**  
- API key is stored in code; in a real-world app, you’d use environment variables or secrets management

---

## 🧩 Possible Improvements / Future Work

- Use a real database (SQLite, PostgreSQL, etc.) instead of a JSON file  
- Add input validation and stronger password hashing  
- Add more NLP capabilities: sentiment analysis, summarization, topic modeling  
- Style the UI with CSS / a frontend framework  
- Rate limit usage of the NER API, cache results  
- Better error handling (e.g. when API fails, or text is empty)

---

## 📄 License & Credits

This project is open-source — feel free to use, modify, or extend it.  
Thanks to RapidAPI for providing the NER API, and to Flask / its ecosystem for making web development easy.

---

*Generated on* `2025-10-05`  
