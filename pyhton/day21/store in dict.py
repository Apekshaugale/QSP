#23.Check whether the length of the string is even using only len().
s=str(input("Enter the string : "))
if len(s)%2==0:
    print()



#66.wop to check where a charchet is alphabet
a=eval(input("enter character"))
d={}
if a.isalpha():
    d[a]=ord(a)
    print(d)
