

# import pandas as pd

# s = pd.Series([10, 11, 12])
# result = s.apply(lambda x: x % 2 == 0)
# print(result)

# a = (lambda x: x % 2 == 0)(11)  
# print(a)

# def doit_twice(n, fn):
#     return fn(fn(n))
# fn = lambda x : x**2
# print(doit_twice(3,fn))

# a_tuple = (2,)
# y = list(a_tuple)
# y.append(3,4)
# a_tuple = tuple(y)
# print(type(a_tuple))
# print((a_tuple))

def char_counts(s):
    # return a tuple that counts vovels, consanants
    vowels = set("aeıioöuüAEIİOÖUÜ")
    v_count, c_count = 0, 0
    for i in s:
        if i.isalpha():
            if i in vowels:
                v_count +=1
            else:
                c_count +=1
    return (v_count, c_count)

# sol = char_counts("elveda elenoracığım")
# print(sol)

def sum_and_prod(L):
    # L is list of nr
    # return tuple first = sum of el in L
    # second = prod el in L
    sum = 0
    prod = 1
    for i in L:
        sum += i
        prod *=i

    return (sum, prod)

solu = sum_and_prod([1,2,3,4,5])
# print(solu)

import copy

def remove_all(L, e):
    L2 = L[:]
    a = [x for x in L if x != e]
    return a, L2

L = [1, 2, 2, 2]

print(remove_all(L, 2)[0])  
print(remove_all(L, 2)[1])  


List1 = [2,3,4,5,6,7]
# List1 = [[2,3],[4,5],[6,7]]
List2 = copy.copy(List1)
List3 = copy.deepcopy(List1)
List4 = List1[:]

List1[0] = 92
# List2[0] = 99
# List3[0][0] = 88

print(List1, List2, List3, List4)

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())

#     b = list(integer_list)
#     a =tuple(b)
#     c =hash(a)

# def swap_case(s):
#     a = str(s)
#     c = a.swapcase()
#     return c

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)