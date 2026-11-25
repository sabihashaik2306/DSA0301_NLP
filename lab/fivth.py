
import re

text = "Accuracy: 92.5, F1: 0.88"

result = re.findall(r'\d+\.\d+', text)

print(result)
