def fib_iter(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print(f"Res: ", end=' ')
        print('0',a,b,end=' ')
        for i in range(n-3):
            temp = a + b
            b=a
            a= temp
            print(temp,end=' ')
        print()
        return b
fib_iter(10)