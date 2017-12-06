n=int(input())
for i in range(0,n):
    s=input()
    l=[]
    r=[]
    for j in range(0,len(s)):
        if j%2==0:
            l.extend(s[j])
        else:
            r.extend(s[j])
    print(("").join(map(str,l)) +" "+ ("").join(map(str,r)))