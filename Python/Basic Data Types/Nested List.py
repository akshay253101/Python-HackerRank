students,j,flag = [],0,0
for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
students.sort(key = lambda x:(x[1],x[0]))

for i in range(len(students)):
    if students[0][1] < students[i][1] and flag == 0:
        j = i
        flag = 1
    if students[j][1] == students[i][1] and flag == 1:
         print(students[i][0])
           