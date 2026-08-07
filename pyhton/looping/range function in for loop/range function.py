'''WAP to print numbers from 5 to 25 in steps of 5 using range().
for i in range(5,26,5):
    print(i,end=' ')
'''

'''WAP to accept a number n from the user and print all numbers from 1 to n using a for loop.
n=eval(input('Enter the numbre : ') )
for a in range(1,n+1):
    print(a,end=' ')
'''

'''WAP to print the multiplication table of a given number using a for loop.
n=eval(input('Enter the numbre : ') )
for a in range(1,11):
    print(a*n,end=' ')

'''

'''WAP to calculate the sum of numbers from 1 to n using a for loop.
b=0
n=eval(input('Enter the numbre : ') )
for a in range(1,n):
    b=b+a
    print(b,end=' ')
'''


'''WAP to calculate the sum of all even numbers from 1 to n using a for loop.
b=0
n=eval(input('Enter the numbre : ') )
for a in range(1,n):
    if a%2==0:
         
         print(a,end=' ')
         b=b+a
print()
print(f'sum of all even numbers from 1 to {n} is ',b)'''

'''WAP to find the factorial of a given number using a for loop.
n=eval(input('Enter the input : '))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)
'''

''' WAP to traverse a string and print each character on a new line using a for loop.  

n=str(input('Enter the input : '))
for i in n:
  print(i)

  '''

'''WAP to count the number of vowels in a given string using a for loop.
count=0
n=str(input('Enter the input : '))
for i in n:
    if i in 'aeiouAEIOU':
       count=count+1 
print(count)
'''

'''WAP to count the number of uppercase and lowercase letters in a string using a for loop.
upper=0
lower=0
n=str(input('Enter the input : '))
for i in n:
    if i.isupper():
       upper=upper+1
    elif i.islower():
       lower=lower+1
print('number of uppercase ',upper)
print('number of lowercase ',lower)
'''


'''WAP to reverse a string using a for loop (without using slicing).
s=str(input('Enter the input : '))

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")

    '''
'''WAP to count how many times a particular character appears in a string using a for loop.'''
s=str(input('Enter the input : '))
a=eval(input('Enter the input : '))
count=0
for b in s:
    if s in b
    
else:
    print("Not a Palindrome")
