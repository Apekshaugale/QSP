#63.wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)
number=eval(input('Enter the number : '))
if number%5==0 and number%7==0:
  print('The square of given value is',number**2)
