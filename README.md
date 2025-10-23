# 🏓 Ping Pong Game (Python + Pygame)

A simple **real-time Ping Pong game** built with **Python** and **Pygame**.  
Includes paddle-ball collision fixes, a game over screen, replay options, and sound effects.

---

## 🚀 Features
- ✅ **Fixed ball collision** – no tunneling through paddles.  
- ✅ **Angled bounces** – ball direction depends on where it hits the paddle.  
- ✅ **Game Over screen** – announces winner when target score is reached.  
- ✅ **Replay menu** – play Best of 3 / 5 / 7, or exit.  
- ✅ **Sound effects** – paddle hit, wall bounce, and scoring.  
- ✅ **AI opponent** – right paddle auto-tracks the ball.  
- ✅ **Player controls** – move left paddle with **W / S** keys.  

---

## 🎮 Controls
- **Player (Left Paddle)** → `W` (up), `S` (down)  
- **AI (Right Paddle)** → automatic  
- **Menu** →  
  - `3` → Best of 3 (first to 2)  
  - `5` → Best of 5 (first to 3)  
  - `7` → Best of 7 (first to 4)  
  - `ESC` → Exit  

---

## 📂 Project Structure

PING-PONG-/
│
├── main.py                  # Entry point (game loop, scoring, replay menu)
│
├── game/                    # Game logic modules
│   ├── ball.py              # Ball class (movement, collision, angled bounce, sounds)
│   └── paddle.py            # Paddle class (player + AI movement)
│
├── sounds/                  # Sound effects
│   ├── paddle.wav           # Sound when ball hits paddle
│   ├── wall.wav             # Sound when ball bounces on top/bottom wall
│   └── score.wav            # Sound when a point is scored
│
├── requirements.txt         # Python dependencies (pygame, etc.)
├── .gitignore               # Git ignore file (ignores .venv, __pycache__, etc.)
└── README.md                # Project documentation


---

## ⚡ Installation & Running
### 1. Clone the repository
```bash
git clone https://github.com/2005-Aneeshdutt/PING-PONG-.git
cd PING-PONG-


2. Create a virtual environment (recommended)
bash
Copy code
python -m venv .venv
Activate it:

Windows:

bash
Copy code
.\.venv\Scripts\activate
Mac/Linux:

bash
Copy code
source .venv/bin/activate


3. Install dependencies
bash
Copy code
pip install -r requirements.txt


4. Run the game
bash
Copy code
python main.py
🛠 Requirements
Python 3.10+

pygame (installed via requirements.txt)

📝 Code Flow
main.py → Entry point, game loop, scoring, replay menu.

game/ball.py → Ball movement, wall bounce, paddle collision + angled bounce.

game/paddle.py → Player controls (W/S) + AI auto movement.

sounds/ → Contains .wav files for paddle hit, wall bounce, and scoring.

👨‍💻 Author
Developed by Aneesh Dutt
