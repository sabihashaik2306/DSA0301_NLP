
import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
VP -> V NP | VP PP
NP -> Pronoun | Det N | NP PP
PP -> P NP
Pronoun -> 'I'
Det -> 'the' | 'a'
N -> 'man' | 'telescope'
V -> 'saw'
P -> 'with'
""")

parser = ChartParser(grammar)

sentence = input("Enter sentence: ")
words = sentence.split()

trees = list(parser.parse(words))

print("Number of parse trees:", len(trees))

if trees:
    for i, tree in enumerate(trees, 1):
        print("\\nParse Tree", i)
        tree.pretty_print()
        tree.draw()
else:
    print("No parse tree found")
