# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number
###########################################################################

#To determine if a number in prime or not
num = int(input("Enter the number\n"))

if num <= 1:
    print(str(num) + " is not a prime number")
else:
    for i in range(2,num):
        if num%i == 0:
            print(str(num) + " is not a prime number")
            break
    else:
        print(str(num) + " is a prime number")
	
	
###########################################################################

#To print all prime numbers in an interval:

lower_limit = int(input("Enter the lower limit\n"))
upper_limit = int(input("Enter the upper limit\n"))

prime_list = []

for i in range(lower_limit, upper_limit+1):
    for num in range(2, i):
        if i % num == 0:
            break
    else:
        if i > 1:
            prime_list.append(i)

print(prime_list)




