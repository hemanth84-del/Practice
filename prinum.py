#print('this is to print 1st 10 prime number')
#def read(meg):
 #   return int(input(msg))
#def main():
 #   prime(read('enter the number'))
#def prime(num):
 #   for i in range(2,num):
  #      if (num%i)==0:
   #         print(num)
#main()
#print()
        

lower=int(input("Enter lower range:"))
upper=int(input("Enter upper range:"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)