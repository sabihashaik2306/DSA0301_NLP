
import re

text = input("Enter a word: ")

if re.fullmatch(r'\w+ing', text):
    print("Matched")
else:
    print("Not matched")
