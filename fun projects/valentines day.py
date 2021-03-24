while True:
    n=10
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end='')
        for j in range(i+1):
            print("* ",end="")
        for j in range(2*(n-i-1)):
            print(' ',end='')
        for j in range(i+1):
            print("* ",end="")
        print()
    for i in range(20,0,-1):
        for j in range(20-i):
            print(' ',end='')
        for j in range(i,0,-1):
            print('* ',end='')
        print()