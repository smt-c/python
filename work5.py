

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    def calc(query_name):
        scores = [marks for name, marks in student_marks.items() if name == query_name]
        print(scores)
        total_sc = sum(scores[0])
        divider = int(len(scores[0])) or 3
        return total_sc / divider

    

    sol = calc(query_name)
    print(round(sol,2))
    print(f"{sol:.2f}") 

    
"""
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""