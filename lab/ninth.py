
import re

text = input("Enter cat or dog: ")

if re.fullmatch(r'cat|dog', text):
    print("Matched")
else:
    print("Not matched")
