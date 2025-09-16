# train/train_chatbot.py

import sys
import os

# Add backend folder to sys.path so we can import model.utils
sys.path.append(os.path.abspath('../backend'))

import json
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from model.tokenizer import tokenize

if __name__ == '__main__':
    #Create model directory
    model_dir = '../backend/model'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        print(f"Created model directory: {model_dir}")
    else:
        print(f"Model directory already exists: {model_dir}")

    # Load intents json
    with open('../data/intents.json', 'r', encoding='utf-8') as f: #Opens for reading
        intents = json.load(f) #parses the JSON file into a Python dictionary.
    print(f"Loaded {len(intents['intents'])} intents")

    # Prepare training data
    #texts, labels = [], []
    #texts — list of all example phrases (patterns) from every intent.
    labels — list of corresponding tags (intent names).
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            texts.append(pattern)
            labels.append(intent['tag'])
    print(f"Number of training samples: {len(texts)}")
    print(f"Sample texts: {texts[:3]}")
    print(f"Sample labels: {labels[:3]}")

    # Vectorize texts using your tokenizer  Convert text to features
    vectorizer = CountVectorizer(tokenizer=tokenize, token_pattern=None)
    X = vectorizer.fit_transform(texts)
    y = np.array(labels)
    print(f"Vectorizer vocabulary size: {len(vectorizer.vocabulary_)}")

    # Train Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X, y)
    print(f"Model classes: {model.classes_}")

    # Save vectorizer, model, and intents for backend usage
    model_path = os.path.join(model_dir, 'intent_classifier.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump((vectorizer, model, intents), f)
    print(f"✅ Chatbot model trained and saved to {model_path}")
