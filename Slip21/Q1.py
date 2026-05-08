'''
Q.1) Write a python program to remove punctuations from the given string?
[10 Marks]
'''

import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Example usage
text = input("Enter a string: ")
result = remove_punctuation(text)
print("String without punctuation:", result)
