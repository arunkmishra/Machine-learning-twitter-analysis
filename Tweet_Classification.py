import pickle

with open('static/Multinomial_Naive_Bayes.pkl', 'rb') as f:
    classification_model = pickle.load(f)

with open('static/Vocab_model.pkl', 'rb') as f:
    vocab_model = pickle.load(f)

def predict(tweet):
    # coverting tweet to DTM
    tweet_dtm = vocab_model.transform(tweet)
    result = classification_model.predict(tweet_dtm)
    return result
