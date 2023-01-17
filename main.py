#!/usr/bin/env python
# made by @odinhr
import tkinter as tk
from tools import countWords, browseFile

def displayResults(word_count, keyword_percentage):
    results_label.config(text=f'Total words: {word_count}. Keyword density percentage: {keyword_percentage}%')

def processFile():
    filepath = browseFile()
    keywords = keyword_entry.get().split(',')
    word_count, keyword_percentage = countWords(filepath, keywords)
    displayResults(word_count, keyword_percentage)

root = tk.Tk()
root.geometry("500x150")
root.title("Keywords analyzer")

keyword_label = tk.Label(text="Keywords (comma separated):")
keyword_label.pack()

keyword_entry = tk.Entry()
keyword_entry.pack()

browse_button = tk.Button(text="Browse txt file", command=processFile)
browse_button.pack()

results_label = tk.Label(text="")
results_label.pack()

root.mainloop()