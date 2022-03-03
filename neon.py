import math
print('this code is to check if a number is neon or not')
def main():
    num=int(input("Enter a number:"))
    is_neon(num)

def is_neon(num):
    if num==neon(num):
        print("It is a Neon Number.")
    else:
        print("It is not a Neon Number.")

def neon(num):
    res=0
    count_digits=count_digits(num)
    while num:
        last_digit= num % 10
        res += int(sqr(last_digit,count_digits))
        num=remove_last_digit(num)
    return res
def count_digits(num):
    count=0
    while num:
        count += 1
        num=remove_last_digit(num)
    return count
def remove_last_digit(num):
    return num//10
main()
