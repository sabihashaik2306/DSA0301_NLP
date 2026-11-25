
def automaton(s):
    state = 0

    for ch in s:
        if ch not in "ab":
            return False

        if state == 0:
            state = 1 if ch == 'a' else 0
        elif state == 1:
            state = 1 if ch == 'a' else 2
        elif state == 2:
            state = 1 if ch == 'a' else 0

    return state == 2


s = input("Enter a string containing a and b: ")

if automaton(s):
    print(s, "Accepted")
else:
    print(s, "Rejected")

