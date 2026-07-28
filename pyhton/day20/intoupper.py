#17.If the given string length is odd, convert it into lowercase.
a=str(input('Enter the string :'))
if (len(a)%2)==1:
    print(f'The length of string {a} is odd.')
    print(f'The lowercase output of {a} is ',a.lower())


a=str(input('Enter the string :'))
if (len(a)&1)==1:
    print(f'The length of string {a} is odd.')
    print(f'The lowercase output of {a} is ',a.lower())


a=str(input('Enter the string :'))
if len(a)%2!=0:
    print(f'The length of string {a} is odd.')
    print(f'The lowercase output of {a} is ',a.lower())
