n = int(input())
var = n % 2
if var != 0:
    print("Weird")
if var == 0:
    if 2<n<5:
        print("Not Weird");
    if 6<=n<=20 :
        print("Weird");
    if n>20 :
        print ("Not Weird");