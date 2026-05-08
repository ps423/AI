'''
Q.1) Write a python program to remove stop words for a given passage from a text file using NLTK?
[10 Marks]
'''

import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Example usage
text = "This is a sample passage with some stop words that should be removed"
result = remove_stopwords(text)
print("Original:", text)
print("Without stopwords:", result)
