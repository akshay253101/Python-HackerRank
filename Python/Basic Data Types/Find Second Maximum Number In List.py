n = int(input())
arr = list (map(int, input().split()))
d = max(arr)
for i in range (0,n):
    if d == max(arr) :
        arr.remove(max(arr))
print(max(arr))