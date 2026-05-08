'''
Q.1) Write a Python program to accept a string. Find and print the number of upper case alphabets and lower case alphabets.
[10 Marks]
'''

def count_case_letters(text):
    upper_count = 0
    lower_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    return upper_count, lower_count

# Example usage
text = input("Enter a string: ")
upper, lower = count_case_letters(text)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
