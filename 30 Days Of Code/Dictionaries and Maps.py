n = int(input())
d = dict(input().split() for i in range(0,n))
while True:
    try:
        key = input()
        if key in d:
            print(key+"="+d[key]);
        elif key not in d:
            print("Not found")
    except EOFError:
        break;