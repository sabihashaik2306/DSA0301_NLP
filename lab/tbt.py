
import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, brill, brill_trainer
from nltk.tokenize import word_tokenize

nltk.download('treebank')
nltk.download('punkt')
nltk.download('punkt_tab')

# Load training data
data = treebank.tagged_sents()

# Split training data
train_data = data[:3000]

# Initial tagger
initial_tagger = UnigramTagger(train_data)

# Transformation templates
templates = brill.brill24()

# Train Brill tagger
trainer = brill_trainer.BrillTaggerTrainer(
    initial_tagger, templates
)

tagger = trainer.train(train_data[:2000], max_rules=50)

# User input
sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)

result = tagger.tag(words)

print("\nTBL POS Tagging:")
print(result)
