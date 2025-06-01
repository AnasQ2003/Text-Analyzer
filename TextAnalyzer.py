import tkinter as tk
from collections import Counter
import re

root = tk.Tk()
root.title("Text Analyzer")
root.geometry("500x600")
root.configure(bg="#2C3E50")

def analyze_text():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        result_label.config(text="Please enter some text to analyze.")
        return

    word_list = re.findall(r'\b\w+\b', text)
    word_count = len(word_list)
    sentence_count = len(re.findall(r'[.!?]', text))
    char_count = len(text.replace(" ", ""))
    char_frequency = Counter(text.replace(" ", "").lower())

    result = (f"Word Count: {word_count}\n"
              f"Sentence Count: {sentence_count}\n"
              f"Character Count (excluding spaces): {char_count}\n"
              f"Character Frequency:\n")

    for char, freq in char_frequency.most_common(5):
        result += f"{char}: {freq}\n"

    result_label.config(text=result)

tk.Label(root, text="Text Analyzer", font=("Arial", 24, "bold"), bg="#2C3E50", fg="white").pack(pady=20)

tk.Label(root, text="Enter text:", font=("Arial", 14), bg="#2C3E50", fg="white").pack()
text_entry = tk.Text(root, font=("Arial", 12), height=10, width=50)
text_entry.pack(pady=10)

analyze_button = tk.Button(root, text="Analyze", font=("Arial", 14), bg="#27AE60", fg="white", width=10,
                           command=analyze_text)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#2C3E50", fg="white", justify="left")
result_label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), bg="#E74C3C", fg="white", width=10, command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
