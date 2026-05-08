'''
Q.1) Write a python program to implement Lemmatization using NLTK
[10 Marks]
'''

import nltk
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('wordnet')
nltk.download('omw-1.4')

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)

# Example usage
text = "The cats are running and mice are hiding"
result = lemmatize_text(text)
print("Original:", text)
print("Lemmatized:", result)
