#Reverse a String 2 ways
----------------------------------------------------------------------
       
#1. Reverse a string using loop

def rev_str(s):        
  str = ''
    
  for i in range(len(s)):
    str = str + s[-i-1]        
  return str
  
s = input("Enter a string :")	

print ("\nThe original string  is : " + s)
 
print ("\nThe reversed string is : " + rev_str(s))

------------------------------------------------------------------------- 

#2. Reverse a string using slice syntax

def rev_str(string):
    string = string[::-1]
    return string

s = input("Enter a string :")	

print ("\nThe original string  is : " + s)
 
print ("\nThe reversed string is : " + rev_str(s))
        