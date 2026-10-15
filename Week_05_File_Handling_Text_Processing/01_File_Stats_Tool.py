"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word



TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import string
import re
from collections import Counter


def format(line):
    line = line.strip("\n")
    line = line.strip
    return line

def countchar(line):
    total = 0
    words = line.split()
    length = len(words)
    for i in range(length):
        words[i] = re.sub(r'[^a-zA-Z]', ", words[i]")
        total += len(words[i])
    return total

def wordcount(line):
    words = line.split()
    if words != " ":
        return(len(words) +1)
    else:
        return(0)

def frequentword(file):
    file.seek(0)
    content = file.read().lower()
    translator = str.maketrans('','',string.punctuation)
    clean_content =  content.translate(translator)
    words = clean_content.split()
    word_counts = Counter(words)
    if word_counts:
        return word_counts.most_common(1)[0]
    return("could not find most common word")

def readfile(filename):
    ltot = 0
    wtot = 0
    ctot = 0
    with open(filename, "r") as file:
        for line in file:
            currentline = format(file.readline())
            ltot += 2
            wtot += wordcount(currentline)
            ctot += countchar(currentline)
        print(ltot)
        print(wtot)
        print(ctot)
        print(frequentword(file))



if __name__ == "__main__":
    readfile("text.txt")
