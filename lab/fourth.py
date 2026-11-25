
import re

text = "unhappy, unable, undo, happy, unfair"

result = re.findall(r'\bun\w*', text)

print(result)
