
# Control flow and loop
# print("Hello Welcome Back Day 03")
#Q 1: Write a program that checks if a given number is
#positive, negative, or zero.
# num=float(input("Enter a number :"))
# if num>0:
#     print("The number is positive ")
# elif num<0:
#     print("The number is negative ")
# else:
#     print("The number is zero ")


# Q 2: Create a loop that prints the first 10 even numbers.\
    
# for i in range(1,11):
#     if i % 2==0:
#         print(i,"Even number")

# Q 3: Implement a program that finds the largest number 
# in a list.

# numbers=[31,13,75,69,59]
# largest=max(numbers)
# print(largest)

# 1 .Create a program that takes a year as input and checks if
# it is a leap year or not.

# year=int(input("Enter a year :"))

# if(year%400==0):
#     print(year,"Leap Year")
# elif (year%100==0):
#     print(year,"NoT a Leap Year")
# elif (year%4==0):
#     print(year,"A Leap year")
# else:
#     print(year,"Not A Leap Year")

#  Given a list of integers, find all the even numbers and
# store them in a new list+

# mylist=[1,2,3,13,22,4,69,70,14,11,16,17,20]
# newlist=[]
# for i in mylist:
#     if i %2==0:
#          newlist.append(i)
# print("even number",newlist)

# .& Write a Python program to check if a given number is a
# prime number+

# primenum=int(input("Enter number :"))

# if primenum > 1:
#     for i in range(2,primenum):
#         if primenum % i ==0:
#             print(primenum,"Not a Prime Number ")
#             break
#     else:
#        print(primenum,"Is A Prime Number")
        

#& Create a program that generates the Fibonacci sequence
# up to a given number of terms+
# n=int(input("Enter a numer :"))
# a,b=0,1
# for i in range(n):
#     print(a,end="")
#     a,b=b,a+b

# -& Given a list of names, print all names starting with the
# letter 'A'+

# names=["Zain","Ali","Shahwaiz","Waqas","Ahmed","Ahmer","Hanzalah","Ammar"]

# for i in names:
#     if i.startswith("A"):
#      print(i)

# & Implement a program that prints the multiplication table
# of a given number+

# table =int(input("Enter a number :"))

# for i in range(1,11):
#     print(table,'*',i,'=',i*table)


# 
# 
# Write a program that calculates the factorial of a given
# number+



# num = int(input("Enter a number: "))

# factorial = 1

# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print("Factorial of", num, "is", factorial)


for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
words = ["python", "ai", "university", "code", "student", "learn"]
count = sum(1 for word in words if len(word) > 5)
print("Number of words with more than 5 characters:", count)

num = int(input("Enter a number: "))

sum_digits = 0
for digit in str(num):
    sum_digits += int(digit)

print("Sum of digits:", sum_digits)
