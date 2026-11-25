
import re

text = "Courses are CSE305, AI204 and CSE101"

result = re.findall(r'\b[A-Z]{3}\d{3}\b', text)

print(result)
