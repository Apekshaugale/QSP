'''1.wap to check whether the given number is even and greater than 5
num=2'''
'''
num=eval(input('Enter the number : '))
if num%2==0:
    print("The given number is even ")
    if num>5:
        print('The given  number is greater than 5.')
    else:
        print('The given number is less than 5.')
else:
    print('The given number is odd')

'''

'''2.wap to check the number is odd and check if the number is divisible by 7
n=35

'''


# num=eval(input('Enter the number : '))
# if num%2==1:
#     print('The given number is odd .')
#     if num%7==0:
#         print('The number is divsible by 7.')
#     else:
#         print(f'The number {num} is not divsible by 7.')
# else:
#     print(f'The number {num} is even.')


'''5.wap to Book ticket in Book my show

condition:---> first it should ask theaters name then it should display the movie available
                          then it has to display ticket price and in the end ticket should be booked'''
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
 