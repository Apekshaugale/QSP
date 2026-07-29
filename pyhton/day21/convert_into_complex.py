#61.wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)
number=eval(input('Enter the number : '))
if number%2==0 and number%6==0:
  print(complex(number))
