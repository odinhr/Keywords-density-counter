#!/usr/bin/env python
import tkinter as tk
from tkinter import filedialog

def browseFile():
    filepath = filedialog.askopenfilename()
    return filepath

def countWords(filepath, keywords):
    with open(filepath, 'r') as f:
        text = f.read()
    word_list = text.split()
    word_count = len(word_list)
    keyword_count = 0
    for word in word_list:
        if word in keywords:
            keyword_count += 1
    keyword_percentage = (keyword_count / word_count) * 100
    return word_count, keyword_percentage

