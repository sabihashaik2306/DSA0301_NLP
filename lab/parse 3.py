
import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'The' | 'a'
N -> 'student' | 'book'
V -> 'reads'
""")

parser = ChartParser(grammar)

sentence = "The student reads a book"
words = sentence.split()

for tree in parser.parse(words):
    tree.pretty_print()
    tree.draw()
