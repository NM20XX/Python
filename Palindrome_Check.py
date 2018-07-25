#Palindrome check
#A palindrome is a string which is same read forward or backwards.

   
def rev_str(string):
    string = string[::-1]
    return string

s = input("Enter a string :")	

print ("\nThe original string  is : " + s)

s = s.casefold()  
#The casefold() method used for caseless matching, i.e. ignores cases when comparing.
 
r = rev_str(s)
print ("\nThe reversed string is : " + r)

if s == r:
  print("\nIt is a palindrome")
else:
  print("\nIt is not a palindrome")
  

