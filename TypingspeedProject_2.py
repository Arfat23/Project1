import tkinter as tk
from tkinter import messagebox
import time
import random
# Sample sentences to type
sentences = [
"Artificial Intelligence is the future of technology.",
"Practice typing every day to improve your speed.
"Python is a beginner friendly programming language.",
"Data is the new oil in the modern world.",
"Machine Learning is a subset of Artificial Intelligence."
class TypingSpeedTester:
def _init_(self, root):
self.root = root
self.root.titIe("Typing Speed Tester")
self.root.geometry("700x400")
self.root.config(bg="#eOf7fa")
self.start_time = None
self.target_text = tk.StringVar()
# Heading
tk.LabeI(root, text="Typing Speed Tester", font=("AriaI", 20, "bold"),
fg="#00796b").pack(pady=10)
# Target Sentence
self.sentence_label = tk.LabeI(root, text=
"#eOf7fa",
, font=("AriaI", 14), wrapIength=600,
self.sentence_IabeI.pack(pady=10)