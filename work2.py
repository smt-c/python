from collections import defaultdict, Counter



# # groups = lambda :{month : '', amount: 0}

# pairs = [
#          {"month": "12", "amount": 2000, },
#          {"month": "11", "amount": 440, },
#          {"month": "11", "amount": 4400, },
#          {"month": "11", "amount": 440, },
#          {"month": "12", "amount": 600, },
#          {"month": "10", "amount": 400, },
#          {"month": "10", "amount": 4030, },
#          {"month": "10", "amount": 4200, },
#          {"month": "9", "amount": 400, },
#          {"month": "9", "amount": 3050, },
#         ]

# groups = defaultdict(list)
# groups2 = defaultdict(int)
# for i in pairs:
#     amount = i["amount"]
#     month = i["month"]
#     groups[month].append(amount)
#     groups2[month] += (amount) 

# print(dict(groups))
# print(dict(groups2))

# arr = [1,3,4,6,7,9,2,8,10, 11,12,5]
# n = len(arr)
# k = 4
# print(n, sorted(arr), k)

# def my_function(n, arr, k):
#     n, arr, k = n, arr, k
#     my_arr = sorted(arr)
#     num = my_arr[-k]
#     print(num)
#     return num

# my_function(n, arr, k)


# word = input("wright text:")
# char = input("choose a letter:")
# # word = "örnekKelime"
# res = ''
# d = {}
# d2 = {}
# str3 = word[::-1]

# w_word = word.lower()

# for c in w_word:
#     d[c] = d.get(c, 0) + 1

# for c, cnt in d.items():
#     if cnt > 1:
#         res += (c)


# for c in w_word:
#     d2[c] = d2.get(c, 0) +1

# d = d2.get(char,0)

# print(d2)
# print(d)
# print(str3)


s = "banana"
d = Counter(s)

most_freq_char = str(d.most_common(1)[0][0])
print(most_freq_char)

print(d)
print(d['a'])       # 3 → count of 'a'
print(d.most_common())  # [('a', 3), ('n', 2), ('b', 1)]




