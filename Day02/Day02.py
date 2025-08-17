# Q 1: Create variables for storing a person's name, age, and
#average test score.

# name="Zain"
# age=21
# average_test_score=86.6
# print(name,age,average_test_score)

# Q 2: Concatenate two strings and print the result.

# firsname="Zain"
# lastname="Ali Shah"
# concate=firsname +" "+lastname
# print(concate)

# Q 3: Create a list of fruits and access elements using
# indexing.

# fruits=["apple","banana","orange","mango"]
# print(fruits[0])

# Q 4: Given a list of numbers, find the sum and average.
# numbers=[10,20,30,40,50]
# sum_numbers=sum(numbers)
# ave=sum_numbers/len(numbers)
# print("SUM ",sum_numbers)
# print("Average",ave)

# % Create a program that takes a temperature in Celsius and
# converts it to Kelvin)

# celsius=float(input("Enter temperature in celsius :"))
# Kelvin=celsius+273.15
# print(Kelvin,"IN Kelvin temperature")

# % Implement a program that checks if a given string is a
# palindrome)

# def  is_palindrome(s):
#     s=s.lower()
#     return s==s[::-1]
# word=input("ENter a senctene: ")
# if is_palindrome(word):
#     print(word,"is palindrome")
# else:
#     print(word,"is not palindrome")


# % Create a function to reverse a given string)

# def reverse_sting(s):
#     return s[::-1]

# print(reverse_sting("Helo world"))


# % Given a list of names, concatenate them into a single
# string separated by spaces)
# 
# def generate_full_name(first_name,last_name):
#     return  first_name + " " +last_name

# print(generate_full_name("Zain","Ali Shah"))


# % Write a Python program to check if a given string is a
# pangram (contains all letters of the alphabet))

# def is_pangram(s):
#     s=s.lower()
#     alphabet="abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in s:
#             return False
#         return True
# sentence = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(sentence))


#  Calculate the area and circumference of a circle given its
# radius)


# import math
# radius=float(input("Enter the radius of the circle :"))
# area=math.pi*radius*radius
# circumference=2*math.pi*radius
# print("Area:", area)
# print("Circumference:", circumference)

# minutes = int(input("Enter minutes: "))

# hours = minutes // 60   # total hours
# remaining_minutes = minutes % 60   # baqi minutes

# print(f"{minutes} minutes = {hours} hour(s) and {remaining_minutes} minute(s)")
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

# Example
sentence = "Hello World"
print("Number of vowels:", count_vowels(sentence))
