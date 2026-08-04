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


