import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def clean_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))  
    filtered = [word for word in tokens if word.lower() not in stop_words]
    return " ".join(filtered)
