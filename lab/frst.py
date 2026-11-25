
import re

text = "I am learning #NLP and #AI"

result = re.findall(r'#[A-Za-z]+', text)

print(result)
