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

def phone_number_receive(number):

    a = ''.join(list(filter(lambda i: i.isdigit(), number)))
    if len(a) == 8:
        return '+374' + a + ' Correct phone number'
    elif len(a) == 9 and a[0] == '0':
        return '+374' + a[1::] + ' Correct phone number'
    else:
        a = '+' + a
        if a.startswith('+374') and len(a) == 12:
            return a + ' Correct phone number'
        else:
            return ValueError('Invalid phone number')


b = phone_number_receive(input('Write your phone number -  ').strip())
print(b)
