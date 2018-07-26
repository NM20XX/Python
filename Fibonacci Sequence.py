# Method 1:Fibonacci Sequence using generator

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fib(n):
    x = 0
    y = 1
    for i in range(n): 
        yield x 
        x,y = y,x+y


def get_input():
    term = int(input("Enter term in the Fibonacci sequence: "))
    return term

for n in fib(get_input()):
    print(n)
		
	
--------------------------------------------------------------------

# Method 2:

def get_input():
    term = int(input("Enter term in the Fibonacci sequence: "))
    return term

x = 0
y = 1
cnt = 0

# check if the input is valid
while True: 
  input_term = get_input()
  if input_term <= 0:
    print("Enter a positive value")
    continue
  else:
    break

print("Fibonacci sequence upto",input_term,":")
while cnt < input_term:
  if input_term == 1: 
    print(x)
  else:
    print(x,end=', ')
    # assign values
    x,y = y,x+y
  cnt += 1
























