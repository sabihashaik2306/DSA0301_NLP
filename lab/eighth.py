
import re

text = input("Enter a lowercase word: ")

if re.fullmatch(r'[a-z]+', text):
    print("Valid")
else:
    print("Invalid")
