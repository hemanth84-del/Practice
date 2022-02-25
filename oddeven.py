def main():
    num=int(input('enter the number->'))
    is_oddeven(num)

def is_oddeven(num):
    if num % 2 == 0:
        print(f'{num=} is even')
    else:
        print(f'{num=} is odd')
main()