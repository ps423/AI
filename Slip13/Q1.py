'''
Q.1) Write a python program to sort the sentence in alphabetical order?
[10 Marks]
'''

def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

# Example usage
sentence = input("Enter a sentence: ")
sorted_sentence = sort_sentence(sentence)
print("Sorted sentence:", sorted_sentence)
