# write a fist progrsm
# print("hello world")
# print("Wel come again")

# Q 2: Calculate the sum of two numbers entered by the user.
# num1=input("Enter first number : ")
# num2=input("Enter second number :")
# result=float(num1)+float(num2)
# print("The sum is :",result)


# Q 3: Convert temperature from Celsius to Fahrenheit.
# celsius=float(input("Enter temperature in celsius:"))
# faraenheit=(celsius *9/5)+32
# print("Temperature in Farenheit: ",faraenheit)

# Write a Python program to calculate the area of a
#rectangle given its length and width

# length=float(input("Enter the length of rectangle :"))
# width=float(input("Enter the width of rectangle :"))

# area=length*width
# print("Area of Rectangle is :",area)

#  Create a program that takes a user's name and age as
# input and prints a greeting message

# name=input("Enter your name :")
# age=input("Enter your age :")
# print("Hello",name,"! You are ",age,"year old")

# Write a program to check if a number is even or odd
# num=int(input("Enter a number :"))

# if num%2==0:
#     print(num ,"is even")
# else:
#     print(num,"is odd")

#  Given a list of numbers, find the maximum and minimum
# values

# numbers=[5,10,15,25,20]
# max_value=max(numbers)
# min_value=min(numbers)
# print("Maximum numbers ",max_value)
# print("Minimum numbers",min_value)

# Create a Python function to check if a given string is a
#palindrome

# def is_palidrome(s):
#     s=s.lower()
#     return s==s[::-1]
# word=input("Enter a word to chec palindrome ")
# if is_palidrome(word):
#     print(word,"is palidrome")
# else:
#     print(word,"is not palindrome")

# is_palindrome
# is_palindrome


# Calculate the compound interest for a given principal
# amount, interest rate, and time period
# def  calculate_compound_interest(principal,rate,time):
#     amount=principal*(1+rate/100)**time
#     ci=amount-principal
#     return ci
# p = float(input("Enter principal amount: "))
# r = float(input("Enter annual interest rate (%): "))
# t = int(input("Enter time (in years): "))

# calculate_compound_interest=calculate_compound_interest(p,r,t)
# print("Compound Interest is :",calculate_compound_interest)


# Write a program that converts a given number of days
# into years, weeks, and days


# days=int(input("Enter nmber of days :"))
# years=days//365
# weeks=(days%365)//7
# remaining_days=(days%365)%7

# print("Years:", years)
# print("Weeks:", weeks)
# print("Days:", remaining_days)


#  Given a list of integers, find the sum of all positive
# numbers

# mylist=[5,15,25,10]
# my_sum=sum(num for num in mylist if num > 0)
# print("Sum of positive number is :",my_sum)

# Create a program that takes a sentence as input and
#counts the number of words in it

# mystr=input("Enter a sentence :")
# mycount=len(mystr.split())
# print("number of word ",mycount)

# ,(Implement a program that swaps the values of two
#variables.

a=5
b=10
print("Swap the values",b,"and",a)
