#64.wap to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5
#,if satisfied, display the ascii characters (take user input)
value=eval(input('Enter the value : '))
if (value>45 and value<200) and (value%4==0 and value%5==0):
    print(f'The ASCII character of given value "{value}" is ',chr(value))
