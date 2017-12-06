def print_rangoli(size):
    a = 96 + size
    n=size
    l,r,d = [],[],[]
    for i in range(a,96,-1):
        l.append(chr(i))
        if i==a:
            r.append('')
        else:
            r.append('-'+chr(i+1))
        d.append(('-'.join(map(str,l))+''.join(map(str,r[::-1]))).center(4*n-3,'-'))
        print(('-'.join(map(str,l))+''.join(map(str,r[::-1]))).center(4*n-3,'-'))
        size = size-1
    for i in range(len(d)-2,-1,-1):
        print(d[i])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)