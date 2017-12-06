if __name__ == '__main__':
    s = input()
    for i in range(0,len(s)):
        if s[i].isalnum():
            result_(s[i].isalnum())
            break
        elif not s[len(s)-1].isalnum() and i == len(s)-1:
            result_(s[i].isalnum())
            
    for i in range(0,len(s)):
        if s[i].isalpha():
            result_(s[i].isalpha())
            break
        elif not s[len(s)-1].isalpha() and i == len(s)-1:
            result_(s[i].isalpha())

    for i in range(0,len(s)):
        if s[i].isdigit():
            result_(s[i].isdigit())
            break
        elif not s[len(s)-1].isdigit() and i == len(s)-1:
            result_(s[i].isdigit())

    for i in range(0,len(s)):
        if s[i].islower():
            result_(s[i].islower())
            break
        elif not s[len(s)-1].islower() and i == len(s)-1:
            result_(s[i].islower())
            
    for i in range(0,len(s)):
        if s[i].isupper():
            result_(s[i].isupper())
            break
        elif not s[len(s)-1].isupper() and i == len(s)-1:
            result_(s[i].isupper())