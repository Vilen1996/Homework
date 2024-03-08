# 1. Write a Python program which will remove all zeros from an IP address.

# ip = '216.008.094.196'
#
# def remove_zeros(text):
#     text = text.split('0')
#     return ''.join(text)
#
# print(remove_zeros(ip))

#################################################################

# 2 Given an list of numbers. Find the maximum element in list.Without use max function.

# arr = [12,214,48483,44,54]
#
# def max_element(list):
#     Max = list[0]
#     for i in range(1, len(list)):
#         if len(str(list[i])) >len(str(Max)):
#             Max = list[i]
#     return Max
#
# print(max_element(arr))

#################################################################

# 3 Write a Python program that validates passwords based on the following criteria:
#  The password must be at least 8 characters long.
#  The password must contain at least one uppercase letter.
#  The password must contain at least one lowercase letter.
#  The password must contain at least one digit (0-9).
#  The password must contain at least one special character (e.g., @, #, $,
# etc.).

# password = 'Thisiswar1$'
#
# def valid_password(text):
#     uppercase = False
#     lowercase = False
#     digit = False
#     character = False
#     if len(text) >= 8:
#         for i in text:
#             if i.isupper():
#                 uppercase = True
#             if i.islower():
#                 lowercase = True
#             if i.isdigit():
#                 digit = True
#             if not i.isalnum():
#                 character = True
#     return uppercase and lowercase and digit and character
#
# print(valid_password(password))

#################################################################

# 4 Write a program that takes in a string as input, counts and outputs the number of vowels.

# text = input('Write a text ')
# count = 0
# vowels = ('o','i','e','a','u')
# for i in text:
#     if i.lower() in vowels:
#         count += 1
# print(count)

#################################################################

# 5 Write a function. Create the list which elements are products between two neighbours.

# arr = list(i for i in input('Write an elements ').split(' '))
# for i in range(len(arr)):
#     if arr[i] == arr[-1]:
#         arr.pop()
#     else:
#         arr[i] = int(arr[i]) * int(arr[i + 1])
# print(arr)

#################################################################

# 6 Given a sentence with missing words and an array of words. Replace all ‘_’ in a sentence with the words from the array.

# text = '_ we have a _ and _ dont know _ to do'
# L = ['Ashot', 'problem', 'we', 'what']
# count = 0
# arr = text.split(' ')
# for i in range(len(arr)):
#     if arr[i] == '_':
#         arr[i] = L[count]
#         count += 1
#
# print(' '.join(arr))

#################################################################

# 7 Given a list of strings. Find the strings with maximum
# and minimum lengths in array. Print the sum of their lengths.
#
# arr = ['Harut' , "Harutunyan", 'Hovhannisyan', 'Ter-Hovsepyan', 'Haykyanc']
# Max = arr[0]
# Min = arr[0]
#
# for i in arr:
#     if i > Max:
#         Max = i
#     if i < Min:
#         Min = i
#
# print(len(Max) + len(Min))

#################################################################

# 8 Given a list of numbers and a number. Find the index
# of a first element which is equal to that number. If there is
# not such a number, that find the index of the first element
# which is the closest to it.
#
# number = 8
# list_to_check = [36, -12, 47, -58, 148, -55, -19, 10]
# if number in list_to_check:
#     print(list_to_check.index(number))
#
# else:
#     number1 = 0
#     min = 1000000000000
#
#     for i in list_to_check:
#         if min > abs(number - i):
#             min = abs(number - i)
#             number1 = i
#
#     print(list_to_check.index(number1))


#################################################################

# 9. Given an dict. Invert it (keys become values and values
# become keys). If there is more than key for that given
# value create an list.Input

# Dict = {'a': 1, 'f': 1, 'b': 2, 'c': 2, 'd': 2}
# Dict_1 = dict()
# for i in Dict.keys():
#     if Dict[i] in Dict_1.keys():
#         arr = list(Dict_1[Dict[i]])
#         arr.append(i)
#         Dict_1[Dict[i]] = arr
#     else:
#         Dict_1.setdefault(Dict[i], i)
# print(Dict_1)

#################################################################

# 10  Define a function which can generate a dictionary
# where the keys are numbers between 1 and N (both
# included) and the values are square of keys. The function
# should print the dict.Example :

# N = 8
# Dict = dict()
# for i in range(1,8+1):
#     Dict.setdefault(i, i ** 2)
# print(Dict)