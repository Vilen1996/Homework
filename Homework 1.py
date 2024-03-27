# 1. Basics of Lambda: Create a lambda function that multiplies any number by 10.

# x = int(input('Enter a number'))
# multiplie = lambda a: a*10
# print(multiplie(x))

#####################################################

# 2. Using Map: Given a list of integers, use map() to double each number in the list.

# arr = [1,2,3,4,5]
# double = list(map(lambda a: a*2, arr))
# print(double)

#####################################################

# 3. Using Filter: Given a list of numbers, use filter() to extract all the even numbers.

# arr = list(range(1,10))
# even = list(filter(lambda a: a % 2 == 0, arr))
# print(even)

#####################################################

# 4. Using Reduce: Use reduce() to find the product of all numbers in a given list.

# from functools import reduce
#
# arr = [1, 2, 3, 4]
# product = reduce((lambda x, y: x * y), arr)
# print(product)

#####################################################

# 5. Custom Function: Write a function named is_prime that determines if a number
# is prime. Use this function with filter() to extract prime numbers from a list.

# def is_prime(a):
#     for i in range(2, a//2):
#         if a % i == 0:
#             return False
#     return True
#
#
# x = list(filter(is_prime,[5, 6, 7, 8, 9, 10, 11]))
# print(x)

#####################################################

# 6  Combining Map & Filter: Given a list of numbers, first filter out the even
# numbers and then square them using map()


# numbers = [1,2,3,4,5,6,7,8,9]
# x = list(
#     map(lambda x: x**2,
#     filter(lambda y: y % 2 == 0, numbers))
# )
# print(x)

#####################################################

# 7 Write a python function to create a simple Calculator.

# def calculate(a,b,c):
#     if '+' == b:
#         return int(a) + int(c)
#     elif '-' == b:
#         return int(a) - int(c)
#     elif '*' == b:
#         return int(a) * int(c)
#     elif '/' == b:
#         return int(a) / int(c)
#
# x,y,z = input('Enter what you want to do ').split( )
#
# print(calculate(x,y,z))

#####################################################

# 8. Write a python function to find max of two numbers.

# def maximum(a,b):
#     return max(a,b)
#
# print(maximum(7,8))

#####################################################

#  9. Write a python function to sum all numbers from given list.

# def sum_of_digits(arr):
#     return sum(arr)
#
# print(sum_of_digits([1,2,3]))


#####################################################

#  10. Write a python function to multiply all numbers from given list.

# def multiple(arr):
#     sum = 1
#     for i in range(len(arr)):
#         sum *= arr[i]
#     return sum
#
# print(multiple([1,2,3,4]))

#####################################################
# 11. You are given a program that takes all 3 passengers ages as inputs and inserts

# i = 1
# while i <= 4:
#     x = int(input(f'Enter {i} passanger`s age '))
#     if x < 16:
#         print('Too young!')
#         break
#     else:
#         print("Get ready!")
#     i += 1

import random

class MagicFight:
    def __init__(self, magic_words: list):
        self.magic_words = magic_words

    def check(self) -> str:
        """It will return the Lord Voldemort’s three random magic words.
        And if you have 2 and more corresponding words
        it will say ‘’You win’ otherwise it will say ‘’You lose’.
        """
        lst = []
        voldemort = ['Avada Kedavra', 'Crucio', 'Imperio']
        for i in range(3):
            lst.append(voldemort[random.randint(0, 2)])
        core = 0
        core_vol = 0
        for i in range(3):
            if self.magic_words[i] == lst[i]:
                core += 1
                core_vol -= 1
            else:
                core -= 1
                core_vol += 1
        print(f'Harry Potter: {core}')
        print(f'Lord Voldemord: {core_vol}')
        print(lst)
        print(self.magic_words)
        return 'You Win' if core >= 1 else 'You Lose'


a = MagicFight(list(input('Write your magic ').split(',')))
print(a.check())
