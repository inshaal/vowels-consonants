#To find the number of vowels and consonants in the string
s=raw_input("Enter String : ")
v,x=0,0
for i in range (0,len(s)):
    if s[i] in ['a','e','i','o','u']:
        v=v+1
    else:
        x=x+1
print "The total no. of vowels are: ",v
print "Consonants are: ",x
print "                                         -by Ins"
