def make_prod(a=2):
    def g(b):
        return a*b
    return g

# val = make_prod(5)(2)
# print(val)

# prod = make_prod(9)

# print(prod(5))

import copy

def is_pal(a):
    temp = copy.deepcopy(a)
    temp.reverse()
    print(temp)
    if temp == a:
        return True
    else:
        return False
    
# print(is_pal(list('abab')))


url_list = "http://nexuspipstrade.com.nodexinvestments.com/login,https://primetrademiners.com.interimtradeoption.com/login,https://vercelsuixaion.com/login,https://apexcapitalindex.com.stratospeedfreightage.com/login,https://acmefxmarket.com.fabiancordero.com/login,http://ftmotrade.com.iultimateconcept.com/login,http://cryptogrowthanalysiss.com.iultimateconcept.com/login,https://elitetradingzone.com.deminitrades.com/login,http://globalfxbittrades.com.swiftportexpresscargo.com/login" # gelen arrayi eşitle
domain_list = "some, some, some"
operationid_list = "someid, id,id"

# for each input
mysrt = url_list

new_list = mysrt.split(',')
my_body = ''
for i in new_list:
    my_body = my_body + (f'<li> {i} </li>')
    
    # print(my_body)


# Dict

def find_in_L(Ld, k):
    # Ld is a list
    # k is int
    a = []
    for L in Ld:
        j = [x for x in L if x == k]
        if j != None :
            a.append(j)
            print(a)
            return True
        else:
            return False

def counter(Ld):
    count = 0
    for d in Ld:
        for v, k in d.items():
            if v==k:
                count +=1
    return count
    
def counter2(Ld):
    # return sum(1 for d in Ld for k, v in d.items() if k == v)
    return sum(1 for d in Ld for k, v in d.items() if v == k)

    
d1 = {1:2, 3:4 ,5:5, 'a':'a'}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}   

print(counter([d1, d2, d3]))
print(counter2([d1, d2, d3]))

print(d1.items())
