'''
WAP to check whether both given values point to the same memory location or
not. if it is true print the middle item of the second collection, or else if it is false
print the first item and last item of the first collection along with the memory
address.'''

value1=eval(input('Enter the value1:'))
value2=eval(input('Enter the value2:'))
if  id(value1)==id(value2):
    mid=(len(value2)-1)//2
    print(value1[mid])
else:
    print(f' The first item  {value1[0]}   and  memory address is {id(value1[0])}')
    print(f' last item   {value1[-1]}  and memory address is {id(value1[-1])}  ' )


OR


v1=eval(input('Enter the value1:'))
v2=eval(input('Enter the value2:'))
if id(v1)==id(v2):
    mid=(len(v2)-1)//2
    print(v2[mid])
else:
    print(f' The first item  {value1[0]}   and  memory address is {id(value1[0])}')
    print(f' last item   {value1[-1]}  and memory address is {id(value1[-1])}  ' )
