import tkinter as tk
from tkinter import filedialog, messagebox
from difflib import SequenceMatcher

class PlagiarismChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Checker")

        self.text_area1 = tk.Text(self.root, height=10, width=50)
        self.text_area1.pack(pady=10)

        self.text_area2 = tk.Text(self.root, height=10, width=50)
        self.text_area2.pack(pady=10)

        self.check_button = tk.Button(self.root, text="Check Plagiarism", command=self.check_plagiarism)
        self.check_button.pack(pady=5)

    def check_plagiarism(self):
        content1 = self.text_area1.get("1.0", tk.END)
        content2 = self.text_area2.get("1.0", tk.END)

        similarity_ratio = self.calculate_similarity(content1, content2)

        messagebox.showinfo("Similarity Ratio", f"The similarity ratio is: {similarity_ratio}")

    def calculate_similarity(self, text1, text2):
        matcher = SequenceMatcher(None, text1, text2)
        similarity_ratio = matcher.ratio()
        return similarity_ratio

# Create the Tkinter application window
root = tk.Tk()

# Create the plagiarism checker application
app = PlagiarismChecker(root)

# Run the Tkinter event loop
root.mainloop()
