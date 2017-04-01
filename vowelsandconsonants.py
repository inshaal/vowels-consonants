#To find the number of vowels and consonants present in the string provided by the user.
s=raw_input("Enter String : ")
d=len(s)
v=0
x=0
for i in range (0,d):
    if s[i] in ['a','e','i','o','u']:
        v=v+1
    else:
        x=x+1
print "The total no. of vowels are: ",v
print "Consonants are: ",x
