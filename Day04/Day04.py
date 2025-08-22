# FUNCTIONS IN PYTHON



# Q 1: Write a function to calculate the area of a circle
# given its radius.
# import math
# def area_of_circle(radius):
#     return math.pi*(radius**2)
    
# r=float(input("Enter the radius of circle : "))

# print(area_of_circle(r))

# Q 2: Create a function to check if a number is prime.
# import math
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(29))


# Q 3: Implement a function that reverses a given string.
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("Zain ALi Shah"))


# Given a list of numbers, create a function to find the sum
# of all positive numbers

# def sum_of_positive_numbers(numbers):
#     return sum(num for num in numbers if num >0)

# print(sum_of_positive_numbers([1,2,3,4,5,6,7,8,9,10]))

#  Write a Python function to check if a given string is a
# palindrome

# def is_palindrome(s):
#     s=s.lower()
#     return s==s[::-1]
# # print(is_palindrome("Madam"))
# # print(is_palindrome("hello"))
# print(is_palindrome("eye"))

# Implement a function that returns the factorial of a given
# number using recursion

# def factorial(n):
#  if n==0 or n==1:
#      return 1
#  else:
#     return n*factorial(n-1)
# print(factorial(7))
         
         
# Create a function to find the square of each element in a
# given list

# def square_of_elements(numbers):
#     return [num ** 2 for num in numbers]

# print(square_of_elements([1,2,3,4,5,6,7]))

# Q Write a function to check if a number is even or odd and
# return "Even" or "Odd" accordingly

# def eve_or_odd(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"
    
# r=int(input("Enter a Number : "))
# print(eve_or_odd(r))

# Calculate the area of a triangle given its base and height
# using a function

# def area_of_triangle(base,height):
#     return 0.5 * base *height

# print(area_of_triangle(5,10))

# Create a function that takes a list of strings and returns
# the list sorted alphabetically*

# def sorted_list_alpha(strings):
#     return sorted(strings)

# print(sorted_list_alpha(["banana","orange","mango","apple","cherry","dew","egg"]))

# Write a function that takes two lists and returns their
# intersection (common elements)

# def intersection(list1,list2):
#     return [num for num in list1 if num in list2]

# print(intersection([1,2,3,4,5,9,8],[4,5,6,7,8,9]))

# Implement a function to check if a given year is a leap
# year or not*


# def leap_year(year):

#   if(year%400==0):
#       print(year,"Leap Year")
#   elif (year%100==0):
#     print(year,"NoT a Leap Year")
#   elif (year%4==0):
#     print(year,"A Leap year")
#   else:
#     print(year,"Not A Leap Year")
#     return year
# r=int(input("Enter a year :"))
# print(leap_year(r))


# Create a function that takes a number as input and prints
# its multiplication table.

# def multiplication_table(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)

# r=int(input("Enter a Number of table :"))
# print(multiplication_table(r))

