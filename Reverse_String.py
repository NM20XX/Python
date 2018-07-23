#Reverse a String - Enter a string and the program will reverse it and print it out.

def rev_str(s):
        
    str_iter = iter(s)
    rev_str = ''
    i = len(s)
    
    for i in range(len(s)):
        rev_str = rev_str + s[-i-1]        
    print rev_str

"""

Another way:
numbers = 'Nila'
string = ''
for i in range(len(numbers)-1,-1,-1):
    string += numbers[i]
print string 

"""

def get_input():
    s = raw_input("Enter a string: ")
    return s

if __name__ == '__main__':
    s = get_input()
    rev_str(s)
        
        