#LIST AND TUPLES

# Q 1: Given a list of numbers, find the sum and average using
# built-in functions.

# list=[1,2,3,4,5,6,7,8,9,10]
# sum_of_list=sum(list)
# avge_of_list=sum_of_list/len(list)
# print("sum of list",sum_of_list)
# print("Average of list ",avge_of_list)

# Q 2: Create a list of fruits and add a new fruit to the list.

# fruits=["apple","banana","orange","mango"]
# addfruits=fruits.append("cherry")
# print(fruits)
# Q 3: Access elements in a tuple using indexing.
# mytupple=("apple","banana","orange")
# print(mytupple[0])
# print(mytupple[1])
# print(mytupple[2])


#  Given two lists of numbers, concatenate them into a
# single list)

# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# list3=list1+list2
# print(list3)

#  Write a program that finds the largest and smallest
# elements in a list)

# list=[1,5,7,9,15,3,4]
# largest=max(list)
# samllest=min(list)
# print("LARGEST :",largest)
# print("SMALLEST : ",samllest)


# Implement a function that takes a list of numbers and
# returns a new list with the squared values)
# def squared_list(list):
#     return[x**2 for x in list]
# print(squared_list([1,2,3,4,5,6,7,8,9,10]))


# Create a program that finds the common elements
# between two lists and stores them in a new list)



# def common_list(list1,list2):
#     return [num for num in list1 if num in list2]

# print(common_list([1,2,3,4,5],[4,5,6,7,8]))

# % Given a list of words, find the word with the maximum
# length and its length)
# Given a list of words, find the word with the maximum length and its length

# words = ["apple", "banana", "watermelon", "grapes", "kiwi"]

# longest_word = max(words, key=len)

# print("Longest word:", longest_word)
# print("Length:", len(longest_word))


#  Write a Python program to count the occurrences of each
# element in a given list)
# from collections import Counter

# numbers = [1, 2, 2, 3, 4, 4, 4, 5]

# count = Counter(numbers)

# print(count)

#  Given a list of names, remove all duplicate names and
# print the unique names)
# names=["Alice","Bob","Charlie","Alice","Bob"]
# unique_names=list(set(names))
# print(unique_names)

# Create a function that takes a list of strings and returns
# the list sorted by the length of the strings)
# def sorted_by_length(strings):
#     return sorted(strings,key=len)
# print(sorted_by_length(["apple","banana","kiwi","orange"]))


# Write a program that checks if a given list is sorted in
# ascending order)
# def is_sorted_ascending(lst):
#     return lst == sorted(lst)

# print(is_sorted_ascending([1, 2, 3, 4, 5]))
# print(is_sorted_ascending([5, 4, 3, 2, 1]))

# Implement a function that takes two lists and returns their
# union (all unique elements from both lists).
def union_lists(list1, list2):
    return list(set(list1) | set(list2))

print(union_lists([1, 2, 3], [3, 4, 5]))