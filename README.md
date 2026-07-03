<h1 align="center">⌨️ Typing Test</h1>

<p align="center">
  A desktop typing-speed trainer built with <b>Python</b> and <b>PyQt5</b>.<br>
  Measure your typing speed and accuracy in Russian and English, and track your personal bests.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyQt5-5.15+-41CD52?logo=qt&logoColor=white" alt="PyQt5">
  <img src="https://img.shields.io/badge/SQLite-database-003B57?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</p>

---

## ✨ Features

- 🇷🇺 / 🇬🇧 **Two languages** — practice on word lists of 10 000 Russian and ~9 900 English words.
- ⏱️ **60-second challenge** — type as much as you can before the timer runs out.
- 🎯 **Live feedback** — each character you type is outlined **green** when correct and **red** when wrong.
- 📊 **Speed & accuracy** — results are reported in characters-per-minute together with an accuracy percentage.
- 👤 **Accounts** — register and log in; passwords are stored **salted and hashed** (PBKDF2-HMAC-SHA256).
- 🏆 **Personal bests** — your top Russian and English scores are saved per account.
- 🔁 **Session memory** — the app remembers the last signed-in user between launches.

## 🛠️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Language   | Python 3.10+                      |
| UI         | PyQt5 (Qt Designer `.ui` layouts) |
| Storage    | SQLite (`sqlite3`)                |
| Security   | `hashlib` PBKDF2 + `secrets`      |

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or newer

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Keysiks/PYQT_Project-Typing_Test.git
cd PYQT_Project-Typing_Test

# 2. (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python main.py
```

The SQLite database is created automatically on first launch — no manual setup required.

## 🎮 How to Use

1. **Register** a new account (or **Log in** if you already have one).
2. Press **Начать** (*Start*) to open the game screen.
3. Choose a **language** and the **number of words**, then press **Сформировать текст** (*Generate text*).
4. Press **Старт** and begin typing — correct characters turn green, mistakes turn red.
5. When the timer ends, your **speed** and **accuracy** are shown and your **personal best** is updated.

## 📁 Project Structure

```
PYQT_Project-Typing_Test/
├── main.py                 # Application entry point
├── requirements.txt
├── src/                    # Application logic
│   ├── paths.py            # Centralised resource paths
│   ├── head_menu.py        # Main menu window
│   ├── enter_form.py       # Login window
│   ├── register_form.py    # Registration window
│   ├── game_form.py        # Typing test screen (core gameplay)
│   ├── best_results.py     # Personal-best screen
│   ├── result_form.py      # Post-round results
│   ├── result_error.py     # "Please log in" notice
│   ├── about_programm.py   # About window
│   ├── save_session.py     # Remember the last user
│   ├── password_utils.py   # Salted PBKDF2 password hashing
│   └── check_password.py   # Password-strength validation
├── ui/                     # Qt Designer .ui layouts
├── data/                   # Russian & English word lists
└── assets/                 # Icons and images
```

## 🔒 Security Notes

- Passwords are never stored in plain text — they are hashed with **PBKDF2-HMAC-SHA256** (100 000 iterations) and a per-user random salt.
- Registration enforces a minimum length, mixed case, and rejects common keyboard sequences.

## 📄 License

Released under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ and PyQt5 by <b>Kirill Redko</b></p>
