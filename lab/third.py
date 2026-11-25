
import re

text = "Dates are 27/09/2026 and 15/08/2025"

result = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)

print(result)
