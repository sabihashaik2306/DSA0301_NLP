
import re

text = "Hello @student01 and @user123"

result = re.findall(r'@[A-Za-z0-9_]+', text)

print(result)
