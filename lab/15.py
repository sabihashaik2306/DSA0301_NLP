
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet', quiet=True)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

word = input("Enter a word: ")

print("Stem:", stemmer.stem(word))
print("Lemma:", lemmatizer.lemmatize(word))

