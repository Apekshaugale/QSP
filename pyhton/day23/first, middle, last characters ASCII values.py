''' WAP to check whether a given string collection is more than ten, and the first +
last character of the ascii values should be divisible by 5, if condition is satisfied
print first, middle, last characters ASCII values or else print the string three
times.
'''

s=eval(input('Enter the string:'))   

if  len(s)>10 and ord(s[0])+ord(s[-1])%5:
    print('first character : ',ord(s[0]))
    print('middle character :',ord(s[(len(s)-1)//2]))
    print('last character :',ord(s[-1]))
else:
    print(s*3)

OR

s=eval(input('Enter the string:'))    
a=(s[0])
print(a)
b=(s[-1])
print(b) 
if  len(s)>10 and ord(a)+ord(b)%5:
    print('first character : ',ord(s[0]))
    mid=(len(s)-1)//2
    print('middle character :',ord(s[mid]))
    print('last character :',ord(s[-1]))
else:
    print(s*3)
