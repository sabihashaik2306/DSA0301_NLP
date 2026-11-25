
import re

text = input("Enter uppercase letters: ")

if re.fullmatch(r'[A-Z]+', text):
    print("Valid")
else:
    print("Invalid")
