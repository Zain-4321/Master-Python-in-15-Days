#STRING MANIPULATIONS

# print("Hello String")

# Q 1: Create a program that checks if a given string is a
# palindrome.

# def is_palindrome(s):
#     s=s.lower()
#     return s==s[::-1]
# print(is_palindrome("madam"))

# Q 2: Write a function to count the number of vowels in a
# given string.

# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     count=0
#     for i in s:
#         if i in vowels:
#             count+=1
#     return count
    
    
# # print(count_vowels("Zain Ali Shah"))
# print(count_vowels("Hello World"))

#  Given a list of words, concatenate them into a single
# string separated by spaces'

# str1="Zain"
# str2="Ali"

# result=str1+ " " +str2
# print(result)

# Create a function to reverse a given string'

# def reverse_string(s):
#      return s[::-1]

# print(reverse_string("Hello World"))

# Write a program that takes a sentence as input and
# counts the number of words in it'

# def counts_words(word):
#     words=word.split()
#     return len(words)

# print(counts_words("Hello World,this is Zain Ali Shah"))

# Implement a function that checks if a given string is a
# pangram (contains all letters of the alphabet)'

# def is_pangrame(s):
#     alphabet=set("abcdefghigklmnopqrstuwxyz")
#     return alphabet.issubset( set(s.lower()))

# print(is_pangrame("The quick brown fox jumps over the lazy dog"))

# Given a string, write a function to remove all vowels from
# it and return the modified string


# def remove_vowels(text):
#     vowels = "aeiouAEIOU"
#     result = ""
#     for char in text:
#         if char not in vowels:
#             result += char
#     return result

# # Example
# print(remove_vowels("Hello World"))   
# print(remove_vowels("Zain Ali Shah"))   


# Write a Python program to find the length of the longest
# word in a sentence'

# def find_longest_word_length(sentence):
#     words = sentence.split()
#     longest_word = max(words,key=len)
#     return len(longest_word)

# # Example
# print(find_longest_word_length("Hello World"))
# print(find_longest_word_length("Zain Ali Shah"))
# print(find_longest_word_length("Zain Ali Shah ki passand wa bha wa "))

# # Create a function that takes a sentence as input and
# returns the sentence in reverse order'

def reverse_string(s):
     return s[::-1]
r=input("Enter a sentence :")
print(reverse_string(r))

def count_names_starting_with_vowel(names):
    vowels = "aeiouAEIOU"
    count = 0
    for name in names:
        if name and name[0] in vowels:  # pehla letter vowel hai?
            count += 1
    return count

# Example
print(count_names_starting_with_vowel(["Ali", "Omar", "Usman", "Zain", "Ibrahim"]))  
# Output: 4
def remove_duplicates(text):
    result = ""
    for char in text:
        if char not in result:  # agar pehle add nahi hua
            result += char
    return result

# Example
print(remove_duplicates("programming"))  # Output: progamin
def word_in_sentence(sentence, word):
    words = sentence.split()  # sentence ko words me tod do
    return word in words      # check if word is present

# Example
print(word_in_sentence("Zain loves programming", "programming"))  # True
print(word_in_sentence("Zain loves programming", "python"))       # False
