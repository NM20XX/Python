# To find factorial of any number
# Factorial of 0 is 1
# Not applicable for negative numbers

number = int(input("Enter the number:\n"))

fact = 1

if number < 0:
    print("\nFactorial of negative number is not possible")
    exit()
elif number == 0:
    fact = 1
else:
    for i in range(1, number+1):
        fact = fact * i

print("\nThe factorial of {} is {}".format(number,fact))




