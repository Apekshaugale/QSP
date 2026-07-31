
'''1WAP to check whether the first item of these two lists is either integer or not.
If it is an integer, concatenate these two lists or else print the memory
address of these two lists.'''
'''
list1=[10,20,30,40]
list2=[20,30,40,24]
'''
'''list1=eval(input ('Enter the list1 : '))
list2=eval(input ('Enter the list2 : '))
if  type(list1[0])==int and type(list2[0])==int:
if isinstance(list1[0],int) and isinstance(list2[0],int):
    print(list1+list2)
else:
    print(id(list1))
    print(id(list2))

'''
'''
#2.Ravi would like to buy a new cello or red pen. The cost of the pen should be 10.
#If the pen is available in the shop, he will buy the pen. If it is not there he will
#come out of the shop.
pen_available=eval(input('Enter  yes/no :  '))
pen_price=eval(input('enter the amount : '))
if pen_available=='yes' and pen_price==10:
    print('Ravi will but a pen ')
else:
    print('Ravi will come out of the shop ')
'''

'''3.WAP to perform addition and subtraction operation by using list collection if the
first and middle data items number are even performing addition operation, or
else performing subtraction.'''
'''
a=[10,20,30,40,50,60,70]
low=0
high=len(a)-1
first_element=a[low]   #varname[position]
print(first_element)
mid_element=(low+high)//2  #postion low and position low 
print(mid_element)  #3 o  utput as a position
print(a[mid_element])
if first_element%2==0 and  a[mid_element]%2==0  :
    print(first_element+a[mid_element)
else:
    print(first_element-[mid_element)
'''
          
'''WAP to check whether the given string of the first character is a special symbol
or not. If a special symbol, to extract and display the middle character or else to
reverse the string and display the half of the string'''
'''
a=eval(input('enter the input'))
mid=(len(a)-1)//2
if not a[0].isalnum():
    print(mid,a[mid])  #mid=collection[position]
else:
    rev = a[::-1]
    print(rev[0:mid+1:1])
'''
'''
#27.WAP whether a given string, if string length is more than 2, then it displays a new
#string with the first and last characters switched, otherwise the display the 3
#copies of given string.
#s=eval(input('Enter the string: '))
s='pyhton'
if len(s)>2:
    print(s[-1]+s[1:-1:1]+a[0])  #a[1:5:1]
else:
    print(s*3)
'''

'''
