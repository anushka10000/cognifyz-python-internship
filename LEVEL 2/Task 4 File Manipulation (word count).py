from collections import Counter
import os

file_path = r'c:\Users\eswar\Downloads\COGNIFYZ TECHNOLOGIES INTERNSHIP\LEVEL 2\sample.txt'  # Make sure this file exists!

# Change directory to where the script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
else:
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().lower().split()

    word_counts = Counter(words)

    for word in sorted(word_counts):
        print(f"{word}: {word_counts[word]}")