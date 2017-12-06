N = int(input())
lista = []
for i in range(0,N):
    var=input().split()
    if var[0] == "print":
        print(lista);
    elif var[0] == "sort":
        lista.sort();
    elif var[0] == "insert":
        lista.insert(int(var[1]),int(var[2]));
    elif var[0] == "remove":
        lista.remove(int(var[1]));
    elif var[0] == "append":
        lista.append(int(var[1]));
    elif var[0] == "pop":
        lista.pop();
    elif var[0] == "reverse":
        lista.reverse();
    