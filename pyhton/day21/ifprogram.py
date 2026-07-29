'''#wop to check the given data type is string
a=eval(input('Enetr the data :'))
if type(a)==str:
    print('string data type')

#wop to check given data type is sequence data type or not
x=eval(input("Enter the data type :"))
if type(x)in (str,list,tuple):
    print("the sequrnce data type")

 #or using isinstance()--->syntax:(vn,(datatype1,dt2,dt3))
x=eval(input("Enter the data type :"))
if isinstance(x,(str,list,tuple)):
    print("the sequrnce data type")



#wop to check given word is palindrome ?(by redaing right to left and left to right both meaning and words same.eg:)
x=str(input("Enter the string : ")) #mom use indexing to check .can use eval
if x==x[::-1]:
    print(f'The given word "{x}" is palindrome')




#wop to check given number is palindrom or not
#121(if condition check only three numbers)
x=str(input("Enter the number : ")) 
if x==x[::-1]:
    print(f'The given word "{x}" is palindrome')


   #or
x=eval(input("Enter the number : ")) 
y=str(x)
if x==x[::-1]:
    print(f'The given word "{x}" is palindrome')


#or using // or %
x=eval(input("Enter the number : "))
if (x//100)==(x%10):
    print(f'The given word "{x}" is palindrome')
    #to print first we used // and to used last we use %


#wop to check the givin number is divisible by 2 and 6
num=eval(input("Enter the number : "))
if num%2==0 or num%6==0:
    print(f'The given number "{num}" is divisible by 2 and 6.')

#or
num=eval(input("Enter the number : "))
if (num%2)==0 and (num%6)==0:
    print(f'The given number "{num} is divisible by 2 and 6.')


#
x=[11,12,13,14]
if key in x :
    print("part")


#multiple of 7 then used % sign not *
    if x%7==0:


#elelment is present or not
        if 'n' in 'a'

#check start and end with same character using indexing
#wop to check last character endswith "k"
y="good luck"
if y.endswith('k'):
    print('True')


#wop to check given sentence starts with "g"
'''

#wop to check year is leap or not
y=eval(input("Enter the year : "))
if y%4==0:
     print(f'the given "{y}" year is leap year.')
else:
    print("The given year is not a leap year .")

    
