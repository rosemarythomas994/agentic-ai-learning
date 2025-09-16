import pickle
import random
import os

# Use an absolute or relative path carefully:
model_path = os.path.join(os.path.dirname(__file__), 'intent_classifier.pkl')

with open(model_path, 'rb') as f:
    vectorizer, model, intents = pickle.load(f)

def get_response(user_input):
    X_test = vectorizer.transform([user_input])
    tag = model.predict(X_test)[0]

    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    
    return "Sorry, I didn't understand that."
