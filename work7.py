if __name__ == '__main__':
    N = int(input())
    arr = []
    
    def func(first):
        arg = first[0]
        index = None
        item = None

        if len(first) == 2:
            item = first[1]
        elif len(first) == 3:
            index = first[1]
            item = first[2]
        
        return (arg, index, item)
    
    for _ in range(N):
        first = input().split()
        arg, inx, item = func(first)

        if arg == "print":
            print(arr)
        else:
            if item is not None:
                if inx is not None:
                    getattr(arr, arg)(int(inx), int(item))
                else:
                    getattr(arr, arg)(int(item))
            else:
                getattr(arr, arg)()

"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""