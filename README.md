<p align="center">
  <img src="https://github.com/BishopMagiPrg/primeiro-projeto-python/blob/main/assets/logo.png" alt="Mystic Forest Logo" width="600">
</p>

# 🌲 Mystic Forest

**Mystic Forest** is a text-based Python adventure game designed as a learning project to explore game mechanics, storytelling, and modular code architecture.

This project is in **active development**, evolving from a simple terminal-based game into a more complex and interactive experience using `pygame`.

---

## 📊 Badges

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/status-active-yellow)

---

## 🚀 Features

- Text-based narrative with interactive choices
- Modular file and function organization
- Turn-based combat system
- Inventory tracking
- Riddle-based win condition
- Partial graphical output (using Pygame)
- English language

---

## 🧱 Project Structure

```
mystic_forest/
├── game.py # Main game loop\n
├── menu.py # Menu system and scene navigation\n
├── scenes.py # Game scenes and storyline\n
├── combat.py # Turn-based combat logic\n
├── inventory.py # Inventory system\n
├── riddle.py # Final challenge\n
├── utils/ # Utility modules and shared code\n
│ ├── init.py\n
│ ├── draw.py # Drawing utilities for GUI\n
│ └── config.py # Window config, colors, paths\n
├── assets/\n
│ └── mystic_forest.jpg\n
└── requirements.txt # Python dependencies\n
```

---

## 📦 Requirements

Install required libraries using:

```bash
pip install -r requirements.txt
```
**requirements.txt**
```text
pygame
```

---

🎯 Purpose
This project is built for learning and experimentation, allowing the developer to:

- Practice Python programming
- Understand modular architecture
- Explore game mechanics like inventory, health, progression
- Transition from CLI to GUI with pygame
- Build a foundation for more advanced game development

---

💻 How to Run
Make sure you're in the mystic_forest directory and run:

```bash
python game.py
```

Ensure all modules and assets are in place. The image file mystic_forest.jpg must be located in assets/.

---

🔮 Planned Features
- Save/load functionality
- Character class selection and stats
- Dynamic enemies and random events
- Animations and sound effects
- Full graphical interface with interactive elements
- Expanded narrative with branching paths

---

🤝 Contributing
This is a personal learning project, but ideas, feedback, and pull requests are welcome! Help shape the forest 🌲

---

📄 License
This project is licensed under the [MIT License](https://opensource.org/license/mit).

---

✨ Credits
Created and maintained by **Bishop.Magician**.
Developed as a journey to explore **how games work through code**.

<p align="center"> 🧙‍♂️ _Enter the forest... and may your path be wise._ </p> ```
