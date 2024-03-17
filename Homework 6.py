# 1.Write a recursive function to determine whether
# all digits of the number are odd or not.

# Example 1
#
# def recursive_for_determine(num: str):
#     for i in num:
#         if int(i) % 2 != 0:
#             return recursive_for_determine(num[1::])
#         else:
#             return False
#     return True
#
#
# print(recursive_for_determine(input('Enter your number ')))


# Example 2

# def recursive_for_determine(num):
#     for i in str(num):
#         if len(str(num)) == 1 and int(num) == 0:
#             return True
#         if int(i) % 2 != 0:
#             return recursive_for_determine(num // 10)
#         else:
#             return False
#
#
#
# print(recursive_for_determine(int(input('Enter your number '))))

############################################################################

# 2. Write a python function all even number
# in 10.000 use threading and print time.

# import threading
# import time
#
#
# def even(start, stop):
#     even_numbers = []
#     for i in range(start, stop):
#         if i % 2 == 0:
#             even_numbers.append(i)
#     print(even_numbers)
#
#
# start_time = time.time()
#
# t1 = threading.Thread(target=even, args=(0, 10000))
# t2 = threading.Thread(target=even, args=(3300, 10000))
# t3 = threading.Thread(target=even, args=(6600, 10001))
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
# print(time.time() - start_time)

############################################################################

# 3.Given N number. Write a recursive function
# that should print from 1 to N numbers.


# def recursive(N):
#     if N != 0:
#         recursive(N-1)
#         print(N)
#
# recursive(5)

############################################################################

# 4.Write a python program to find the longest word from the file content.Need
# to use <try-except> block in the file reading process and print time. example:

# import time
#
#
# def find_long_word(file):
#     try:
#         start_time = time.time()
#         with open(file, 'r') as f:
#             text = f.read().split()
#             longest_word = max(text, key=len)
#             print(time.time() - start_time)
#             return longest_word
#     except:
#         print("No File Found")
#
# print(find_long_word('TEXT.txt'))