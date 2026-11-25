
import re

text = input("Enter 5 digits: ")

if re.fullmatch(r'\d{5}', text):
    print("Valid")
else:
    print("Invalid")
