'''
WAp to check wheteher the middle value in a list is str or not
ls=eval(input('Enter the  list : '))
if len(ls)%2==1:
    if type(ls[len(ls)//2])==str:
        print('The middle is string.')
    else:
        print('The middl value is not string')
else:
    print('The lenght is even and no middle value. ')
    '''



'''
WAP to check whether the character is vowel or not 
char=eval(input('Enter the caharcter : '))
if char.isalpha():
    if char in 'aeiouAEIOU':
           print('The given charcter is vowels .')
    else:
        print(char,'-->is vowles .')
else:
    print(char,' is not alphabet.')


    '''
'''
WAP to check whether the last value in list is palindrome or not and start with vowel or not
ls=eval(input('Enter the list : '))
if ls[-1]==ls[-1][::-1]:
    if ls[-1][0] in 'aeiouAEIOU':
        print(ls[-1],'is a palindrome and start with vowels .')
    else:
        print(ls[-1],'is a palindrome ans start with consonant .')
else:
    print('last value/element is not a palindrome.')

    '''

'''
WAP to check pin and username are same.

un='Apeksha'
pw=123%35
username=eval(input('Enter the username : '))
password=eval(input('Enter the password'))
if username==un:
    if password==pw:
        print('Login Successful...')
    else:
        print('Invaild Password.')
else:
    print('User not found')

        '''

'''
find greteset of four number'''
num1:input('Enter the number 1 : ')
num2:input('Enter the number 2: ')
num3:input('Enter the number 3 : ')
num4:input('Enter the number 4: ')
'''
if num1>=num2 and num1>=num3 and num1>=num4:
    print(f'{num1} is greatest number ')
    if num2>=num1 and num2>=num3 and num2>=num4:
        print(f'{num2} is greatest number ')
        if num3>=num1 and num3>=num2 and num3>=num4:
            print(f'{num3} is greatest number ')
            if num4>=num1 and num4>=num2 and num4>=num3:
                print(f'{num4} is greatest number ')
            else:
               print(f'{num4} is not  greatest number ')
        else:
               print(f'{num3} is not  greatest number ')
    else:
               print(f'{num2} is not  greatest number ')
else:
               print(f'{num1} is not  greatest number ')
        '''



               
