"""
LOOPS
"""

mysum = 0 

for i in range(6):
    
    if i%2 == 0:
        mysum += 1

print(mysum)

# mylist = list(range(-4,11,2))
# mylist2 = [x for x in range(-4,11,2)]
# print(mylist)
# print(mylist2)

line = "aeiouöü"
s= []


line2 = "Cumartesi günü Joe size gelecek. Joe için bir hazırlık yapın."

input1 = input("Replace name: ")
input2 = input("New name: ")  
   
count = line2.count(input1)
line2 = line2.replace(input1, input2)

print(line2)
print(f"{count} replacement(s) made.")

