
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
