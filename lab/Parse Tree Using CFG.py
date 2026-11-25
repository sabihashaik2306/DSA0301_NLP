
import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'this' | 'that'
N -> 'girl' | 'boy' | 'book'
V -> 'reads' | 'writes' | 'likes'
""")

sentence = input("Enter a sentence: ").lower().split()

parser = nltk.ChartParser(grammar)

found = False

for tree in parser.parse(sentence):
    print("Parse Tree:")
    print(tree)
    tree.pretty_print()
    found = True

if not found:
    print("No parse tree found")
