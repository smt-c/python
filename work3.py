# from typing import List

# myArr = [0,17, 2, 5, 3, 4, 7, 9, 15, 45, 6, 17, 74, 13, 22, 60, 8, 34, 53, 21, 10, 12, 20, 23, 31, 29]

# class Solution:
#     def summer(self, nums: List[int], target: int):
#         # Remove duplicates while preserving order
#         uniqueArr = list(set(nums))
#         unique_list = list(dict.fromkeys(nums))
#         unique_ = sorted(nums)
#         print(uniqueArr)
#         print(unique_)
#         print(unique_list)
        
#         h = {}
#         fin = set()

#         for i, num in enumerate(uniqueArr):
#             h[num] = i  # store number and its index
#         print(h)

#         for i, num in enumerate(uniqueArr):
#             pair = target - num
#             if pair in h and h[pair] >= i:
#                 fin.add((i, h[pair]))   # store index pairs

#         return fin

# # Example usage
# sol = Solution()
# print(sol.summer(myArr, 17))  


"""
1:
enumerate(uniqueArr) gives you both the index (i) and the value (num).

h[num] = i saves each number as a key in the dictionary, with its index as the value.

2:
For each number num, you calculate the other number (pair) needed to reach target.
Example: if target = 10 and num = 7, then pair = 3.

if pair in h: checks if that "other number" exists in the dictionary.

h[pair] != i: makes sure you don’t accidentally use the same element twice.

If found, return the indices (i, h[pair]).
"""


# class Solution:
#     def finder(self, arr: list[int], key:int):
#         fix_arr = list(set(arr))

#         h= {}
#         my_list = set()

#         for i, element in enumerate(fix_arr):
#             h[element] = i

#         print(h)
#         for i, element in enumerate(fix_arr):
#             target = key - element
#             if target in h and h[target] != i:
#                  my_list.add((min(i, h[target]), max(i, h[target])))
                    
        
#         return my_list
    
# sol = Solution()
# print(sol.finder(myArr, 17))


a = 1
b = 1.0
c = "1"
d = ("1")
e = ["1"]
f = {"1"}

for var in (a,b,c,d,e,f):
    print(type(var))

nums = range(12)
list = [num**2 for num in nums if num <10]
print(list)

listme = ['xy','abcd',7,'4.0']
res = (len(x) for x in listme if type(x)==str)
print(res)