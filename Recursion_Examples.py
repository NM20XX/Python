#Using recursion

#1. Fibonacci series

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1)+ fib(n-2))

num = int(input("Enter the limit:\n"))
for i in range(num):
    print(fib(i))
    
     
    
#############################################################
 
#2. Sum of natural numbers using recursion

def sum(n):
    if n == 1:
        return n
    else:
        return(n + sum(n-1))

num = int(input("Enter the limit:\n"))
print(sum(num))


#############################################################

#Factorial using recursion

def fact(n):
    if n == 1:
        return n
    else:
        return(n * fact(n-1))

num = int(input("Enter the number:\n"))

if num == 0:
    print("factorial of 0 is 1")
elif num < 0:
    print("factorial not applicable for negative numbers")
else:
    print("factorial of {} is {}".format(num,fact(num)))

