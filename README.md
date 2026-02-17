# T/F-Quizler-
DAY - 34/100 - Project - python X T/F Quizler

# 🧠 Quizler — True / False Quiz App

A GUI-based Quiz Application built using **Python**, **Tkinter**, and the **Open Trivia API**.

This quiz downloads live True/False questions from the internet and displays them using a clean graphical interface.

---

## 🚀 Features

✔ Live Trivia Questions (API based)  
✔ True / False quiz system  
✔ GUI built with Tkinter  
✔ Score tracking  
✔ Question progress display  
✔ Instant feedback colors (Green / Red)  
✔ Automatic next question transition  
✔ End-of-quiz message  

---

## 🖥️ Interface

The app contains:

- Question display area (Canvas)
- ✔ True button
- ❌ False button
- Score display
- Question number indicator

---

## 📂 Project Structure

Quizler/
│
├── 34_QUIZ.py # Main program
├── QUIZ_BRAIN.py # Quiz logic
├── QUIZ_UI.py # GUI interface
│
├── TRUE.png # True button image
└── FALSE.png # False button image

---

## ⚙️ Installation

Install required package:

```bash
pip install requests
Tkinter comes pre-installed with Python.

🌐 API Used
Open Trivia Database API:

https://opentdb.com/api.php?amount=50&type=boolean
This API provides live True/False trivia questions in JSON format.

---

## ▶️ How to Run

Make sure Python is installed.

Run:

```bash
python 34_QUIZ.py
🌐 API Used
Open Trivia Database:

https://opentdb.com/api.php?amount=50&type=boolean
❗ FileNotFoundError Fix (Images)
If you see:

FileNotFoundError
Reason
Using absolute paths like:

E:\folder\image.png
works only on one computer.

✔ Correct Fix (Used in this project)
Wrong_img_path = "FALSE.png"
True_img_path = "TRUE.png"
Images must be inside the project folder.

❗ Python Import Error Fix (.py Files)
If you see:

ModuleNotFoundError
or

No module named QUIZ_BRAIN
Reason
Python files are in different folders.

✔ Correct Setup
All .py files must be together:

34_QUIZ.py
QUIZ_BRAIN.py
QUIZ_UI.py
Same folder = imports work automatically.

🧠 Concepts Practiced
Object-Oriented Programming (OOP)

API requests using requests

JSON data handling

Tkinter GUI

Event-driven programming

Canvas text updates

Button commands & callbacks

👨‍💻 Author
Robin Gupta

Built while learning Python GUI + API integration.

📜 License
This project is for educational and learning purposes.


---
