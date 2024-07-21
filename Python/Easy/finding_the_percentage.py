if __name__ == '__main__':
    def get_average_marks(student_marks, query_name):
        result = 0.00
        if query_name in student_marks:
            sum_marks = sum(student_marks[query_name])
            if sum_marks != 0:
                result = round(sum_marks / len(student_marks[query_name]), 2)
        return result
            
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = get_average_marks(student_marks, query_name)
    print(f"{result:.2f}")