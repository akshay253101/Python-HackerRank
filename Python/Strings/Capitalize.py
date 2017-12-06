def capitalize(string):
    l = string.split(" ")
    for i in range(0,len(l)):
        l[i]=l[i].capitalize();
    d = " ".join(map(str,l))
    return d

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)