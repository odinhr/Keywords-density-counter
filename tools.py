#!/usr/bin/env python

def wordCounter(text):
    text=text.lower()
    separatedText = text.split()
    wordsNumber = len(separatedText)
    return wordsNumber

def keywordsCounter(text,keyword):
    text=text.lower()
    keyword=keyword.lower()
    counter = text.count(keyword)
    return counter

def densityCalculator(text,keyword):
    numberOfKeywords=wordCounter(keyword)
    totalWords = wordCounter(text)
    keywordOcurrences = keywordsCounter(text,keyword)
    densityPercentage = (100*numberOfKeywords*keywordOcurrences)/totalWords
    return densityPercentage, totalWords

