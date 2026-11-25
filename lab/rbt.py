
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

def rule_based_tagging(sentence):
    words = word_tokenize(sentence)

    tagged_words = []

    for word in words:
        if word.lower() in ["is", "am", "are", "was", "were"]:
            tag = "VB"
        elif word.lower() in ["a", "an", "the"]:
            tag = "DT"
        elif word.lower() in ["he", "she", "they", "we", "i"]:
            tag = "PRP"
        elif word.endswith("ing"):
            tag = "VBG"
        elif word.endswith("ly"):
            tag = "RB"
        elif word.endswith("ed"):
            tag = "VBD"
        elif word.endswith("s"):
            tag = "NNS"
        else:
            tag = "NN"

        tagged_words.append((word, tag))

    return tagged_words


sentence = input("Enter a sentence: ")
result = rule_based_tagging(sentence)

print("\nRule-Based POS Tagging:")
print(result)
