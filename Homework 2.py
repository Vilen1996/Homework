# 1. Create a python program which will say which number used more.
# my_list = [1, 3, 4, 5, 1, 2, 3, 1] output:  number 1 - 3 times

# my_list = [1, 3, 4, 5, 1, 2, 3, 3, 3, 1]
# final_number = my_list[0]
# for i in my_list:
#     if my_list.count(i) > my_list.count(final_number):
#         final_number = i
#
# print(f'Number {final_number} - {my_list.count(final_number)} times')

#################################################################

# 2 Write a Python program to sum all the items in a list. use list comprehension

# my_list = [1,2,3,4,5,6,7,8,9]
# Sum = 0
# for i in my_list:
#     Sum += i
#
# print(Sum)

#################################################################

# 3. Write a Python program to get the largest text from a list.

# my_list = ['Karapetyan', 'Sargsyan', 'Hovhannisyan', 'Ter-Mamikonyan', 'israyelyan']
# largest_text = my_list[0]
# for i in my_list:
#     if len(i) > len(largest_text):
#         largest_text = i
#
# print(largest_text)

#################################################################

# 4 Write a Python program that have two lists and returns True if they have at least one common member.

# def common(arr1: list, arr2: list):
#     for i in arr1:
#         if i in arr2:
#             return True
#     else: return False
#
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,1]
# print(common(list1, list2))

#################################################################

# 5 Write a Python program to Sort Words in Alphabetic Order

# def sort_word(arr: list):
#
#     new_list = [arr[0]]
#
#     for i in arr:
#         for f in range(len(new_list)):
#             if i in new_list:
#                 continue
#             if i > new_list[f] and i < new_list[f + 1]:
#                 new_list.insert(f+1, i)
#             elif i > new_list[-1]:
#                 new_list.append(i)
#             elif i < new_list[f]:
#                 new_list.insert(f, i)
#     return new_list
#
#
# my_list = ['j', 'g', 't', 'a', 'b', 'c', 'f', 'd', 'h', 'o', 'e']
#
# print(sort_word(my_list))

#################################################################

# 6 Write a Python program that creates a generator function that generates all
# prime numbers between two given numbers.

# arr = (12, 66)
#
# def is_prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     else:
#         return True
#
#
# gen = [i for i in range(arr[0], arr[1]) if is_prime(i)]
# print(gen)

#################################################################

# 7 Create python program which will check if your password is strong or no. if Len
# your password is great than 8 and if your password have 2 numbers and 2 of the
# following special characters ('!', '@', '#', '$', '%', '&', '*')
# Sample Input:    Python@$World11
# Sample Output:   Strong

# def strong_password(text: str):
#     if len(text) > 8:
#         count_num = 0
#         count_sym = 0
#         for i in text:
#             if i.isdigit():
#                 count_num += 1
#             if i in ('!', '@', '#', '$', '%', '&', '*'):
#                 count_sym += 1
#         if count_num > 1 and count_sym > 1:
#                 return 'Strong'
#         else:
#             return 'Weak'
#     return 'Weak'
#
#
# print(strong_password(input('Write a new password ')))

#################################################################

# 8. Create python program where you want to find id in link if link have id print id.

# def link_id(text: str):
#     arr = []
#     for i in range(len(text)-1, -1, -1):
#         if text[i] == '=':
#             arr.reverse()
#             return ''.join(arr)
#         arr.append(text[i])
#
#
# print(link_id('https://www.youtube.com/watch?v=Bkl1zoKfbM0'))

#################################################################

# 9 Write a Python program that implements a decorator to validate function arguments
# based on a given condition.

# def decorator_func(basic):
#     def wrapper():
#         print('The name of the function is ' + basic.__name__)
#         return basic()
#     return wrapper
#
# @decorator_func
# def game():
#     print('Game has started')
#
# game()

#################################################################

# 10. Write a Python program that implements a decorator to validate function arguments length.

# def decorator_func(basic):
#     def wrapper(*args):
#         for i in range(basic.__code__.co_argcount):
#             print(len(basic.__code__.co_varnames[i]))
#         return basic(*args)
#     return wrapper
#
# @decorator_func
# def game(arr, binary):
#     print('Game has started')
#
# game('a','b')
