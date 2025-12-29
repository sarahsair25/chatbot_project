import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load corpus
with open("corpus.txt", "r", encoding="utf-8") as file:
    corpus = file.read().lower()

sent_tokens = nltk.sent_tokenize(corpus)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def get_response(user_input):
    sent_tokens.append(user_input)

    tfidf = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
    tfidf_matrix = tfidf.fit_transform(sent_tokens)

    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    idx = similarity.argsort()[0][-2]

    flat = similarity.flatten()
    flat.sort()
    score = flat[-2]

    sent_tokens.pop()

    if score == 0:
        return "I'm sorry, I don't understand that."
    else:
        return sent_tokens[idx]