from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
import nltk

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

def tokenize(text):
    return [lemmatizer.lemmatize(word.lower()) for word in tokenizer.tokenize(text)]
