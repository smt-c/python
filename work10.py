# def mult(a,b):
#     if b == 1:
#         return a
#     else:
#         return a + mult(a, b-1)
    
# print(mult(5, 4))

# def power(a,p):
#     if p < 0 :
#         p = -p
#         return(1/power(a,p))
#     elif p == 0 :
#         return 1
#     elif p == 0:
#         return a
#     else:
#         return a * mult(a, p-1)
    
# print(power(5, 0))

def flatter(L):
    if len(L) ==1:
        return L[0]
    else:
        return L[0] + flatter(L[1:])
    
# print(flatter([[2,3],[12]]))


def is_in_list(L,e):
    """
    L is a list whose elements are lists containing ints
    """
    my_list = flatter(L)
    if e in my_list:
        return True
    else:
        return False
    
print(is_in_list([[1,2],[3,4],[5,7,6]], 4))

for i in range(1, 16):
    # if i % 3 == 0 and i % 5 == 0:
    if i % 3 and 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
