
# 1. Write a python class to find max, min  num and and sum in your list:

# class MaxCheck:
#
#     def __init__(self, arr):
#         self.arr = arr
#
#     def check(self):
#
#         self.arr.sort()
#         print(f'Maximum number in list - {self.arr[-1]}')
#         print(f'Minimum number in list - {self.arr[0]}')
#
#     def sum_of_numbers(self):
#
#         sum = 0
#         for i in self.arr:
#             sum += i
#         print(sum)
#
# M = MaxCheck([1,2,4,5,8,48,4,84,8485,15,184,84,84])
# M.check()
# M.sum_of_numbers()

#########################################################

# 2. Write a python class to find two highest values in your dict:

# class TwoHighest:
#     arr = []
#     def __init__(self,d):
#         self.d = d
#     def figure_out(self):
#         for i in self.d.values():
#             self.arr.append(i)
#         self.arr.sort()
#         print(self.arr[-1],self.arr[-2])
# a = TwoHighest({'t': 45, 'a': 1, 'b': 2, 'c': 4, 'r': 9, 'p': 485})
# a.figure_out()

#########################################################

# 3. Write a python class where your child class takes all
# methods in parent class and print them.

# class Parent:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def biggest_number(self):
#         print(max([self.a, self.b, self.c]))
#
#     def sum_of_numbers(self):
#         print(sum([self.a, self.b, self.c]))
#
#     def sum_of_digits(self):
#         p = (str(self.a) + str(self.b) + str(self.c))
#         h = list(map(lambda x: int(x), p))
#         print(sum(h))
#
# class Child(Parent):
#
#     def __init__(self, a, b, c):
#         super().__init__(a, b, c)
#
# d = Child(45, 78, 98)
# d.biggest_number()
# d.sum_of_numbers()
# d.sum_of_digits()

#########################################################

# 4. Write a Python class named Rectangle constructed by
# a length and width and a method which will compute the
# area of a rectangle.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def compute_area(self):
#         print(self.length * self.width)
#
# res = Rectangle(10,20)
# res.compute_area()

#########################################################

# 5. Write a python class where we use polymorphism:

# class Armenia:
#
#     def capital_of(self):
#         print('Yerevan')
#
# class Usa:
#
#     def capital_of(self):
#         print('Washington')
#
#
# a = Armenia()
# b = Usa()
# a.capital_of()
# b.capital_of()

#########################################################

# 6. Create a class Change:You have 3 methods in your class:

# class Change:
#
#     def __init__(self, USD):
#         self.USD = USD
#
#     def convert_to_EURO(self):
#         print(f'USD: {self.USD} = Euro: {self.USD * 0.92}')
#
#     def convert_to_AMD(self):
#         print(f'USD: {self.USD} = AMD: {self.USD * 397.48}')
#
#     def convert_to_RUB(self):
#         print(f'USD: {self.USD} = RUB: {self.USD * 92.30}')
#
# a = Change(455)
# a.convert_to_EURO()
# a.convert_to_AMD()
# a.convert_to_RUB()
