def merge_the_tools(string, k):
    l=[]
    for i in range(0,len(string),k):
        l.append(string[i:k+i])
    for i in range(0,len(l)):
        s=""
        for j in range(0,k):
            if not l[i][j] in s:
                s=s+l[i][j]
        print(s)    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)