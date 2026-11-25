
import re

print(re.fullmatch(r'a*', '').group())
print(re.fullmatch(r'a+', 'a').group())

print(bool(re.fullmatch(r'a*', '')))
print(bool(re.fullmatch(r'a+', '')))
