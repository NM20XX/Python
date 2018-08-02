#Problem 1
#Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
#Then capitalize every vowel in this new string (a, e, i, o, u) 	

def letter_replace(str): 

    from string import ascii_letters

    replace_str=''
    for c in str:
     if c in ascii_letters:
        replace_str = replace_str + ascii_letters[(ascii_letters.index(c)+1)%len(ascii_letters)] #modulo to roll around to the beginning of the string as that will return 0
     else:
        replace_str = replace_str + c
    
    
    vowel = ['A','E','I','O','U','a','e','i','o','u']
    for i in replace_str:
        if i in vowel:
            replace_str = replace_str.replace(i,i.upper())
            
        
    return replace_str
    
#call
letter_replace(input())  


#--------------------------------------------------------------------------------------------------

#Problem 2
#capitalize the first letter of each word. 
#Words will be separated by only one space. 

def capitalize(str):
  word = []
  for w in str.split():
   word.append(w.title())
  return ' '.join(word)

#call  
capitalize(input())