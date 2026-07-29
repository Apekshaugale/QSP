#88. Write a program to check if a credit card number is 16 digits and contains only digits. (e.g., cc = '1234567812345678')#if len(cc)==16 and cc.isdigit:
card=eval(input('Enter the credit card number : '))
if len(card)==16 and card.isdigit():
    print('The given card number is correct.')
