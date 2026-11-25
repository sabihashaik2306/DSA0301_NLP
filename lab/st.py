
import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, BigramTagger
from nltk.tokenize import word_tokenize

nltk.download('treebank')
nltk.download('punkt')
nltk.download('punkt_tab')

# Load tagged dataset
data = treebank.tagged_sents()

# Split dataset
train_data = data[:3000]

# Train unigram tagger
unigram = UnigramTagger(train_data)

# Train bigram tagger
bigram = BigramTagger(train_data, backoff=unigram)

# User input
sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)

result = bigram.tag(words)

print("\nStatistical POS Tagging:")
print(result)
