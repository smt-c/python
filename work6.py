# Enter your code here. Read input from STDIN. Print output to STDOUT
# SOLUTION 1 mine
# if __name__ == "__main__":
#     M = int(input())
#     sets = []
#     for i in range(1):
#         line = input().split()
#         m_set = set(map(int, line))
#         sets.append(m_set)
        

#     N = int(input())
#     setsc = []
#     for i in range(1):
#         line = input().split()
#         n_set = set(map(int, line))
#         setsc.append(n_set)
        
#     united_list = m_set.union(n_set)
#     intersect_list = m_set.intersection(n_set)
    
    
#     for i in intersect_list:
#         united_list.discard(i)
#     for j in sorted(united_list):
#         print(j)

# SOLUTION 2 GPT

if __name__ == "__main__":
    M = int(input())
    m_set = set(map(int, input().split()))

    N = int(input())
    n_set = set(map(int, input().split()))

    # Symmetric difference
    result = m_set ^ n_set

    # Print sorted
    for x in sorted(result):
        print(x)

"""
4
2 4 5 9
4
2 4 11 12
"""