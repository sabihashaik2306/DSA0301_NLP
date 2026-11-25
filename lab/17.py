
def plural(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    elif noun.endswith("y") and len(noun) > 1 and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"

sentence = input("Enter a sentence: ")

words = sentence.split()
result = []

for word in words:
    if word.isalpha():
        result.append(plural(word))
    else:
        result.append(word)

print("Plural sentence:", " ".join(result))

