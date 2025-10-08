import heapq

# arr = range(12)

# second_highest = heapq.nlargest(2, set(arr))[-3] 
# print(second_highest)

# #find 3 largest nr

# list_a = [2, 7, 1, 8, 3, 5, 6]

# list3 = []

# list3 = heapq.nlargest(3,list_a)
# print(list3)

# h = []
# heapq.heappush(h, (5, 'write code'))
# heapq.heappush(h, (7, 'release product'))
# heapq.heappush(h, (1, 'write spec'))
# heapq.heappush(h, (3, 'create tests'))
# heapq.heappop(h)

# print(h)

if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score
    print(students)
    # get the 2 smallest *unique* scores
    unique_scores = set(students.values())
    two_smallest = heapq.nsmallest(2, unique_scores)

    if len(two_smallest) < 2:
        print("Not enough unique scores")
    else:
        second_lowest = two_smallest[1]   # 2nd smallest
        print(second_lowest)

        # collect names with that score
        result = [name for name, score in students.items() if score == second_lowest]

        # print sorted names
        for name in sorted(result):
            print(name)


