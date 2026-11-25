
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["apple"]],
    "V": [["eats"], ["likes"]]
}

def parse(symbol, words):
    if symbol not in grammar:
        return (words[0] == symbol, words[1:]) if words else (False, words)

    for rule in grammar[symbol]:
        remaining = words[:]
        success = True

        for item in rule:
            result, remaining = parse(item, remaining)
            if not result:
                success = False
                break

        if success:
            return True, remaining

    return False, words


sentence = input("Enter a sentence: ").lower().split()

result, remaining = parse("S", sentence)

if result and not remaining:
    print("Sentence is accepted")
else:
    print("Sentence is rejected")
