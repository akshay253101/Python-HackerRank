n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
marks = student_marks[query_name]
percentage = round((marks[0] + marks[1] + marks[2])/3,2)
print("{0:.2f}".format(percentage))