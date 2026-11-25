
import re

text = "My email is abc@gmail.com and my number is 9876543210"

email = re.search(r'\w+@\w+\.\w+', text)
phone = re.search(r'\d{10}', text)

if email:
    print("Email:", email.group())

if phone:
    print("Phone:", phone.group())

pattern = r"Python"
sentence = "I love Python programming"

if re.search(pattern, sentence):
    print("Pattern found")
else:
    print("Pattern not found")
