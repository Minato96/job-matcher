import re
from spacy.lang.en.stop_words import STOP_WORDS

def clean_text(text):
    """cleans the text by removing all the punctuations and convert text into lower case"""

    text = re.sub(r'[^\w\s]', '', text)
    
    text = text.lower()
    
    tokens = text.split()
    cleaned_tokens = [word for word in tokens if word not in STOP_WORDS]
    
    return " ".join(cleaned_tokens)