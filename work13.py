"""
function practice
"""
from ast import Pass


# def is_even(i):
#     return i % 2 == 0

# print(is_even(2))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# print(is_prime(62))

def is_palindrome(s):
    if s == s[::-1]:
        return s
    else:
        pass


my_list = ["racecar", "hello", "madam", "level", "rotor", "deed"]
for i in my_list:
    new_list = []
    elem = is_palindrome(i)
    if elem is not None: 
        new_list.append(elem)
    else: 
        pass
    print(new_list)

