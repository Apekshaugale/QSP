#14.If the given number is odd, store it in a list.
a=eval(input('Enter the number:'))
if a%2==1:
    print(f'The given number {a} is odd.')
    b=[]
    b.append(a)
    print(b)

a=eval(input('Enter the number:'))
if a%2==1:
    print(f'The given number {a} is odd.')
    b=[a]
    print(b)
