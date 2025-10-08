
# if (n%2) == 1 or n%2 == 0 and 6<=n<=20 :
#     print("Weird")

import datetime
import math
# from collections import defaultdict
from datetime import datetime

# dt = '2025-09-09'
# x = datetime(2020, 5, 17)
# our_date = datetime.strptime(dt, '%Y-%m-%d')

# print(x.year)
# print(our_date.strftime(("%W")))

# def myfunc(n):
#   return lambda a : a * n

# lamb = myfunc(11)(2)
# print(lamb)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# array = ["222", "elma", "armut", "limon", "214", "yyy", "veyaa", "kalem"]

# print(type(array))

# array.pop()
# print(array)

# print(array.index("elma"))

# a = "Hello, World!"
# split_array = (a.split(",")) # returns ['Hello', ' World!']
# print(type(split_array))

# price = 159
# # txt = f"The salary is {price:.2f}K dollars annualy"
# txt = "We are the so-called \nWikings\" from the north."
# t = txt.rfind('a')
# end = txt.endswith('.')
# print(end)





# newlist = [x for x in nr if "99" in str(x)]
# fruits.sort()
# print(nr)

# dict = {
#     "type": "car",
#     "model": "320i"
# }
# print(dict)
# dict["color"] = 'blue'
# print(dict)
# dict.update({"color": "red"})
# print(dict)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# for i in range(len(fruits)):
#     fruits[i] += "med"

# print(fruits)

# def my_function(*args, **kwargs):
#   print("The youngest child is ", args)
#   print("The youngest child is " + kwargs["kids"])

# my_function( "Tobias", "Linus", kids="Emil")


# def namef(**kid):
#   print("His last name is " + kid["adı"])

# namef(fname = "Tobias", lname = "Refsnes", adı="Jack")


# def shout(word="yes"):
#     return word.capitalize()+"!"

# print(shout())
# outputs : 'Yes!'

# scream = shout

# print(scream())
# outputs : 'Yes!'


# n = 0  # try changing this to 0, 1, 5, etc.

# if n == 0:
#     fib = []
# elif n == 1:
#     fib = [0]
# else:
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[-1] + fib[-2])

# cubed_fib = list(map(lambda x: x**3, fib))

# print("Fibonacci numbers:", fib)
# print("Cubed Fibonacci numbers:", cubed_fib)


# my

# nr = [99, 12, 1231, 199, 123, 499, 4, 19, 80]
# ipp = 2
# item = 12

# index = nr.index(item) + 1

# boy = len(nr)

# def pageFunc (boy, ipp):
#     return  math.ceil(boy/ipp)
    
# def lastPageFunc (a,b):
#     pageNr = (a/b)
#     lowerPageNr = math.floor(a/b)
#     upperPageNr = pageFunc(a,b)
#     if pageNr> lowerPageNr:
#       sonItem = (pageNr - lowerPageNr) * ipp
#     else:
#       sonItem = ipp
#     return int(sonItem)


# print(pageFunc(index, ipp))
# print(lastPageFunc(boy, ipp))

# def fun(s):
#     # return True if s is a valid email, else return False
#     if type(s) is not str:
#         return False
        
#     m = s.strip()
#     if "@" not in m or "." not in m:
#         return False

#     try:
#         name, domain_parts = m.split("@")
#         domain, ext = domain_parts.split(".")
#     except ValueError:
#         return False

#     allowed_name = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
#     allowed_domain = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
#     allowed_ext = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

#     def isValid(name, domain, ext):
#         if not all(ch in allowed_name for ch in name):
#             return False
#         if not all(ch in allowed_domain for ch in domain):
#             return False
#         if not all(ch in allowed_ext for ch in ext):
#             return False
#         if len(ext) > 3:  
#             return False
#         return True

#     return isValid(name, domain, ext)


# def filter_mail(emails):
#     return list(filter(fun, emails))

# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())

# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)

# allowed_name = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")

# a = "test_of_test"
# b = "domain"
# c = "srap-test"

# def Valid(a,b,c):
#     if not all(x in allowed_name for x in a ):
#         return False
#     if not all(x in allowed_name for x in b ):
#         return False
#     if not all(x in allowed_name for x in c ):
#         return False
#     else:
#         return True

# print(Valid(a,b,c))


# newlist = [x for x in nr if "99" in str(x)]
# print(newlist)

# def calculate_cashflow(transactions):
#     total_inflows = 0
#     total_outflows = 0

#     for t in transactions:
#         t_type = t.get("type")
#         amount = t.get("amount", 0)

#         if t_type == "inflow":
#             total_inflows += amount
#         elif t_type == "outflow":
#             total_outflows += amount
#         else:
#             # Ignore unknown types
#             pass

#     net_cashflow = total_inflows - total_outflows

#     if net_cashflow > 0:
#         status = "positive"
#     elif net_cashflow < 0:
#         status = "negative"
#     else:
#         status = "balanced"

#     return {
#         "total_inflows": total_inflows,
#         "total_outflows": total_outflows,
#         "net_cashflow": net_cashflow,
#         "status": status
#     }


# transactions = [
#     {"type": "inflow", "amount": 10000, "description": "Customer payment"},
#     {"type": "outflow", "amount": 3500, "description": "Supplier invoice"},
#     {"type": "outflow", "amount": 1200, "description": "Office rent"},
#     {"type": "inflow", "amount": 2500, "description": "Service income"},
# ]

# result = calculate_cashflow(transactions)
# print(result)

from collections import defaultdict


transactions = [
    {"type": "inflow", "amount": 1000, "month" : "09", "description": "Payment A", "date": "2025-09-01"},
    {"type": "outflow", "amount": 500, "month" : "09", "description": "Invoice B", "date": "2025-09-01"},
    {"type": "inflow", "amount": 2000, "month" : "10", "description": "Payment C", "date": "2025-10-02"},
    {"type": "outflow", "amount": 2300, "month" : "10", "description": "Payment CA", "date": "2025-10-02"},
    {"type": "outflow", "amount": 800, "month" : "11", "description": "Invoice D", "date": "2025-11-02"},
    {"type": "inflow", "amount": 800, "month" : "11", "description": "Invoice DA", "date": "2025-11-02"},
]


for t in transactions:
    t.setdefault("status","")
    # print(t)

# Group transactions by date
cashflow_by_month= defaultdict(lambda: {"inflow": 0, "outflow": 0})

for t in transactions:
    # Convert string to datetime object
    dt = datetime.strptime(t["date"], "%Y-%m-%d")
    month_key = f"{dt.year}-{dt.month:02d}"  # YYYY-MM format
    month2 = t["month"]
    if t["type"] == "inflow":
        # cashflow_by_month[month_key]["inflow"] += t["amount"]
        cashflow_by_month[month2]["inflow"] += t["amount"]
    elif t["type"] == "outflow":
        # cashflow_by_month[month_key]["outflow"] += t["amount"]
        cashflow_by_month[month2]["outflow"] += t["amount"]

print(cashflow_by_month.items())

# Calculate net cashflow per month
for month, data in cashflow_by_month.items():
    data["net"] = data["inflow"] - data["outflow"]
    data["status"] = "positive" if data["net"] > 0 else ("negative" if data["net"] < 0 else "balanced")

# Print results
for month in sorted(cashflow_by_month):
    print(month, cashflow_by_month[month])

month = "2025-11-02"[:7]
# month2 = t["date"][:7]
print(month)

