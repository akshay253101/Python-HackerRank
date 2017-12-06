def minion_game(string):
    stuart=0
    kevin=0
    for i in range(0,len(string)):
        if string[i] != 'A' and string[i] != 'E' and string[i] != 'I' and string[i] != 'O' and string[i] != 'U':
            stuart=stuart+len(string)-i
        else:
            kevin= kevin+len(string)-i
    if stuart>kevin:
        print("Stuart" +" "+str(stuart))
    elif stuart==kevin:        
        print("Draw")
    else:    
        print("Kevin" +" "+str(kevin))

if __name__ == '__main__':
    s = input()
    minion_game(s)