
'''4.wap to validate facebook username and password
condition is:---> username-->"python"  and password="python masters"'''
'''
FBusername=eval(input('Enter the user name :'))
if FBusername=='python':
    print('User name is vaild .')

    password=eval(input('Enter the password : '))
    if  password=='Python masters':
        print('Password is matched')
    else:
        print('Password is not matched .')
else:
    print('User not found.')
'''

'''string-->lower to upper,upper to lower,swapcase,capitalize.
'''
'''
string=eval(input('Enter the string : '))
if isinstance(string,str):
    print('The given data type is string')
    option=eval(input('Enter the option(1,2,3,4)'))

    if option==1:
        
        print(string.upper())
    elif option==2:
        print(string.lower())
    elif option==3:
        print(string.swapcase())
    elif option==4:
        print(string.capitalize())
    else:
        print('Enter the valid option')
else:
    print('The given data type is not string.')
'''

'''5.wap to Book ticket in Book my show

condition:---> first it should ask theaters name then it should display the movie available
                          then it has to display ticket price and in the end ticket should be booked
theater =['Miraj','PVR','Lakxmi','Cinipole']
user=eval(input('Enter the theater name : '))
 if user in theater :
    print(f'User is selected the  "{user}" theater name.')
    movies=['RRR','KGF','Animal']

    user1=eval(input('Enter the movie name : '))
    if user1 in movies:
         print(f' here {user} is selected the theater and {user1} selected the movie')

         TPrice=[1000,2000,3000,4000]
         amout=eval(input('Enter the amount : '))
         if amount==TPrice[0]:
             print(f'Here user is {user} selected the theater name nand user1 is selelcted the movie and total ticket price is {amount}')
         elif amount==TPrice[1]:
            print(f'Here user is {user} selected the theater name nand user1 is selelcted the movie and total ticket price is {amount}')
         elif amount==TPrice[2]:
            print(f'Here user is {user} selected the theater name nand user1 is selelcted the movie and total ticket price is {amount}')
         elif amount==TPrice[3]:
            print(f'Here user is {user} selected the theater name nand user1 is selelcted the movie and total ticket price is {amount}')
         else:
          print('The ticket price is too low .')
    else:
       print('Wrong movie selected .')
else:
    print('Wrong theater selected ..')
'''
'''6.wap to find middle element is even or odd
s=[3,4,6,7,9,1,5]'''
'''
s=[3,4,6,7,9,1,5]
mid=len(s)//2
if type(s)==list :
    print('Given data type is list .')
    print(s[mid])
    if s[mid]%2==0:
        print('The given middle element is even .')
    else:
        print('The given middle element is odd. ')
else:
    print('The given data is not list')

    '''

'''7.wap to purchase a phone from the shopping app
apps=[“flipkart”,”amazon”]
categories=[“electronics”,”mobile”,”fashion”,”furnitures”]

apps=['flipkart','amazon']
print('Available apps are : ',apps)
user=eval(input('Enter the app name : '))
if user in apps:
    print(f'User selected the app name is {user}')
    categories=['electronics','mobile','fashion','furnitures']
    print('Categories : ')
    print('electronics')
    print('mobile')
    print('fashion')
    print('furnitures')
    c_gories=eval(input('Select the categories : '))
    if c_gories==categories[0]:
        print(f'User select the category : {c_gories} ')
        print(' Electronic does not contains the mobile select vaild category')
    elif  c_gories==categories[1]:
        print(f'User select the category : {c_gories} ')
        mobile=eval(input('Enter the mobile name : '))
        print(f'Added to cart {mobile}  mobile  .')
    elif  c_gories==categories[2]:
        print(f'User select the category : {c_gories} ')
        print(' fashion does not contains the mobile select vaild category')
    elif  c_gories==categories[3]:
        print(f'User select the category : {c_gories} ')
        print(' furnitures does not contains the mobile select vaild category')
    else:
      print('Invalid category ')
else:
    print('App is not available')
        
    '''
'''8.wap to give 10% off only who is purchasing in credit card and
min 3 product should purchase and each product price should be more than 500'''
p1=eval(input ('Enter the product 1:'))
r1=int(input('Enter the price of product 1 Rs:'))
p2=eval(input ('Enter the product 2:'))
r2=int(input('Enter the price of product 2 Rs:'))
p3=eval(input ('Enter the product 3:'))
r3=int(input('Enter the price of product 3 Rs:'))
'''p4=eval(input ('Enter the product 4:'))
r4=int(input('Enter the price of product 4  Rs:'))'''
product=p1,p2,p3
rupees=r1,r2,r3
print('Selected product are  : ',product)
print('Selected product  price are  : ',rupees)
payment=str(input('Enter the payment option :'))
if payment=='credit card':
    print('You are eligible for 10 % off ...')
    if len(product)>=3:
        print('Your minimun order is  3.')
        if r1>500 and r2>500 and r3>500:
            print('Your each product price is greater than 500 .')
            discount=((r1+r2+r3)*10)/100
            total_price=r1+r2+r3
            price=total_price-discount
            print('total_price of product is :',total_price)
            print('10% discount  :',discount)
            print('total_price of product  after 10%  of discount  :',price)
        else:
            print('You are  not eligible  for 10 % off  because your each product price is greater than 500 .')
    else:
        print('You are  not eligible for 10 % off because your minimun order  is less than 3.')
else:
    print('You are not eligible for 10 % off  because you selected different payment mode ..')


