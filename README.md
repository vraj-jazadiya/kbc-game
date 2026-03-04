# 🎮 Kaun Banega Crorepati – CLI Game (Python)

A command-line quiz game inspired by the popular TV show **Kaun Banega Crorepati**.
The game fetches live trivia questions from an online API and lets players answer questions to climb the prize ladder.

---

## 🚀 Features

* 🎯 **Dynamic Trivia Questions** using an API
* 🪜 **KBC Prize Money Ladder**
* 🎮 **Interactive CLI Gameplay**
* 🧠 **Difficulty Levels**

  * Easy
  * Medium
  * Hard
* 🃏 **Lifelines**

  * **Skip Question** (once per game)
  * **50-50** (removes two wrong answers)
* 💰 **Real-time Prize Tracking**
* 🎨 **Colored Terminal UI** using `rich`

---

## 🖥 Example Gameplay

```
Enter your name: Jay

Welcome to Kaun Banega Crorepati

Select Difficulty Level
1. Easy
2. Medium
3. Hard

Enter choice: 2

Question 1 for ₹1000

Which planet is known as the Red Planet?

A. Venus
B. Mars
C. Saturn
D. Mercury

Lock your answer (A/B/C/D | skip | quit | 5050):
```

---

## 🛠 Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/kbc-cli-game.git
cd kbc-cli-game
```

### 2. Create virtual environment (recommended)

```
python -m venv .venv
```

Activate:

Windows

```
.venv\Scripts\activate
```

Linux / Mac

```
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶ Run the Game

```
python main.py
```

---

## 📦 Dependencies

* `requests`
* `rich`

Install manually if needed:

```
pip install requests rich
```

---

## 🧩 Project Structure

```
kbc-cli-game
│
├── main.py
├── trivia_api.py
├── requirements.txt
└── README.md
```

---

## ⚠ Notes

* Questions are fetched from an online trivia API.
* Internet connection is required.
* The **Skip** lifeline removes the current question without increasing the prize level.

---

# 🔮 Next Version (Planned Features)

### 🌍 Global Leaderboard

* Store player scores
* Worldwide rankings

### 🗄 Database Integration

* MongoDB Atlas support
* Persistent score tracking

### 🔐 Anti-Cheat Protection

* Signed score submissions
* Game session validation

### 🎮 Additional Lifelines

* Ask the Audience
* Phone a Friend
* Replace Question

### 🎨 Improved Terminal UI

* Progress bars
* Better layouts with Rich

### 📊 Player Statistics

* Games played
* Highest score
* Accuracy rate

### 🌐 Online Multiplayer Mode

* Compete with friends
* Live leaderboard updates

---

## 🤝 Contributing

Pull requests are welcome!
If you'd like to improve gameplay or add features, feel free to fork the repo.

---

## 📜 License

MIT License

---

⭐ If you like this project, consider starring the repository!
