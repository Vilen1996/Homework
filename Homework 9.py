# with decorator
#
#
# def decorator(func):
#     def inner(*args,**kwargs):
#         a = ''.join(list(filter(lambda i: i.isdigit(), func(*args, **kwargs))))
#         if len(a) == 8:
#             return func('+374' + a)
#         elif len(a) == 9 and a[0] == '0':
#             return func('+374' + a[1::])
#         else:
#             a = '+' + a
#             if a.startswith('+374') and len(a) == 12:
#                 return func(a)
#             else:
#                 return ValueError('Invalid phone number')
#     return inner
#
# @decorator
# def phone_number_receive(number):
#     return number
#
#
# b = phone_number_receive(input('Write your phone number -  ').strip())
# print(b)


# without decorator

# def phone_number_receive(number):

#     a = ''.join(list(filter(lambda i: i.isdigit(), number)))
#     if len(a) == 8:
#         return '+374' + a + ' Correct phone number'
#     elif len(a) == 9 and a[0] == '0':
#         return '+374' + a[1::] + ' Correct phone number'
#     else:
#         a = '+' + a
#         if a.startswith('+374') and len(a) == 12:
#             return a + ' Correct phone number'
#         else:
#             return ValueError('Invalid phone number')


# b = phone_number_receive(input('Write your phone number -  ').strip())
# print(b)

# Extra task

def extra_task(numbers, target):
    if not 2 <= len(numbers) <= 3 * 104:
        raise ValueError('Wrong numbers input')
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if not -1000 <= numbers[i] <= 1000:
                raise ValueError('Wrong numbers input')
            elif not -1000 <= target <= 1000:
                raise ValueError('Wrong numbers input')
            elif numbers[i] + numbers[j] == target:
                return [i+1, j+1]


arr_of_nums = [2, 7, 11, 15]
print(extra_task(arr_of_nums, -1))
