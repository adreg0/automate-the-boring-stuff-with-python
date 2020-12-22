def collatz(number):
    if (number%2==0):
        return(number//2)
    else: 
        return(3*number+1)


try:
    number=int(input("Number:"))
except ValueError:
    number=int(input("Input must be an integer"))
while(number!=1):
    number=collatz(number)
    print(number)