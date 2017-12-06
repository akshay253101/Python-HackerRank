def print_formatted(number):
    for i in range(1,number+1):print(str(i).rjust(len(format(number,'b')),' ')+str(format(i,'o')).rjust(len(format(number,'b'))+1,' ')+str(format(i,'X')).rjust(len(format(number,'b'))+1,' ')+str(format(i,'b')).rjust(len(format(number,'b'))+1,' '))
	

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
	