#wop to check given number is even.
#wap to check if the given number is even or odd.
'''
#wap to check username and passward are atchinf or not by using user input.
if user=="pyhton" and passward=="py"
'''
'''
#wop to check the given number is even print quotient and reaminder else make it is a square.
num=eval(input('enter the number :'))
if num%2==0:
    print('quotient =',num//2)
    print('reaminder',num%2)

else:
    print(num**2)

    
   ''' '''
#wap to check the given dict len is even print as it is else add one  key and value pair make it as a even.
#s=eval(input('enter the dictionary:'))#taking user input
s={3:4,4:5,5:6}
if len(s)%2==0:
    print(s)
else:
    s[200]='ghi'#without using inbuild fuction
    print(s)


s={3:4,4:5,5:6}
if len(s)%2==0:
    print(s)
else:
    s.update({'ghi':44})#with using inbuild fuction
    print(s)
'''

#wap to check if given no is odd print as it is if it is even convert negative.
num=eval(input('enter the number :'))
if num%2!=1:
    print(num)
else:
    print(-(num))
