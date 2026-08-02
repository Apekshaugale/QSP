'''#1.WAP to check whether a number is positive or negative.
#If Positive print positive message or else print Negative Number.
num=eval(input('Enter the number : '))
if num>0:
    print(f"The given number '{num}' is positive.")
else:
    print(f"The given number '{num}' is negative.")

#2.WAP to check whether a number is even or odd.
#If even, print message an even or else print message as odd.
num=eval(input('Enter the number : '))
if num%2==0:
    print(f"The given number '{num}' is even.")
else:
    print(f"The given number '{num}' is odd.")


#3.Write a program to check whether a given number is greater than 10 or not.
#if it is greater than 10 print message as greater or else print that number with not a greater than.
num=eval(input('Enter the number : '))
if num>10:
    print(f"The given number '{num}' is greater than 10.")
else:
    print(f"The given number '{num}' is not greater than 10.")


#4.WAP to check whether the given two input numbers are divisible by 3 and 5.
#If it is divisible, print “Good Morning”, if it is not divisible print “Good Evening”
num1=eval(input('Enter the number1 : '))
num2=eval(input('Enter the number2 : '))
if num1%3==0 and num2%5==0:
    print("Good Morning")
else:
    print("Good Evening")

#4.WAP to accept two integers and check whether those two values are equal or not.
#If equal, multiply to value or else to display the quotation value.
num1=eval(input('Enter the number1 : '))
num2=eval(input('Enter the number2 : '))
if num1==num2:
    print(num1*num2)
else:
    print(' quotation of number =',num1/num2)


#5.WAP to find the largest of two numbers.
num1=eval(input('Enter the number1 : '))
num2=eval(input('Enter the number2 : '))
if num1>num2:
    print(f'The number "{num1}" is larger than "{num2}"')
else:
    print(f'The number "{num2}" is larger than "{num1}"')

 

#6.WAP to the given number integer, if n is greater than 21,
#print the absolute difference between n and 21 otherwise print twice the absolute difference.
num=eval(input('Enter the number : '))
if num>21:
    print(num-21)
else:
    print((num-21)*2)

    
#7.WAP to find the smallest of two numbers
num1=eval(input('Enter the number1 : '))
num2=eval(input('Enter the number2 : '))
if num1<num2:
    print(f'The number "{num1}" is smallest ')
else:
    print(f'The number "{num2}" is smallesr ')


#8.WAP to check whether the given number is divisible by 3 or not if yes,
#print the number or else print the cube of the numbers
num=eval(input('Enter the number : '))
if num%3==0:
    print(num)
else:
    print(num**3)

    

#9.WAP to check whether the given input is divisible by 3 and 5.
#If yes print the actual number or else print string of that number
num=eval(input('Enter the number : '))
if num%3==0 and num%5==0:
    print(num)
else:
    print(str(num))
    print(type(str(num)))

    
#10.WAP to check whether the given number lies between 1 to 19, if it is true square
#that number or else false cube that number and display the number.
num = eval(input('Enter the number: '))
if 1 <= num <= 19:
    print(f'The square of {num} is ',num ** 2)
else:
    print(f'The cube of {num} is {num ** 3}.')

   
#11.WAP to check whether the student has passed or failed. If the student got morethan 40 marks,
#print ‘PASS’ along with those marks, if it is not printed ‘FAIL’ along with those marks
marks=eval(input('Enter the marks : '))
if marks>=40:
    print(f'PASS with {marks} marks')
else:
    print(f'FAIL with by {40-marks} marks')
 
#12.WAP to check whether a given value is even and in range of 47 to 58 and not in 0 or odd.
#if condition is True, to perform display the ascii character. or else to
#perform floor division with 5 and display it.
num = eval(input('Enter the number: '))
if num&1==0 and 47<=num<=58 :
    print(chr(num))
else:
    print(num//5)

    
#13.WAP to check whether a given value is less than 125 and in between 47 to 125 or not.
#if condition is True, to perform store the given value as key and value as a
#  character into the dict or else to append the value in list and display it.
a={}
b=[]
value = eval(input('Enter the value: '))
if value<125 and 47<=value<=125:
    a.update({value:(chr(value))})
    print(a)        
else:
    b.append(value)
    print(b)

    
#14.WAP to check whether a given character is in the alphabet or not. if alphabet,
#display the alphabet with character or else display the not alphabet with character.
char=eval(input('Enter the character : '))
if char.isalpha():
    print(f'Alphabet with character: {char}')
else:
    print('Not alphabet with character :{char}')

    
#15.WAP to check whether a given character is uppercase or other character.
#ifuppercase, display the uppercase with character or else display the other character with character.
char=eval(input('Enter the character : '))
if char.isupper():
    print(f'Uppercase with character: {char}')
else:
    print(f'Other character with character: {char}')


#16.WAP to check whether a given character is lowercase or other character.
#if lowercase, display the lowercase with character or else display the other character with character.
char=eval(input('Enter the character : '))
if char.islower():
    print(f'Lowercase with character: {char}')
else:
    print(f'Other character with character: {char}')
    


#17.WAP to check whether a given character is uppercase or other character.
#if uppercase, convert to lowercase .or else display the ascii number.
char=eval(input('Enter the character : '))
if char.isupper():
    print(f'Lowercase character  :',char.lower())
else:
    print(f'character with ASCII: {ord(char)}')


#18.WAP to check whether the given character is in lowercase or uppercase.
#If it is in lowercase, convert it into uppercase, or else it is in uppercase and convert it into lowercase.
#Display the value.
char=eval(input('Enter the character : '))
if char.islower():
    print(f' character in upper  :',char.upper())
else:
    print(f'character in lower : ',char.lower())

    
#19.WAP to check whether the given string of the first character is a special symbol or not.
#If a special symbol, to extract and display the middle character or else to reverse the string
#and display the half of the string.
string=eval(input('Enter the string : '))
if string[0] in '@#$%^&*?|}{^@!~':
    print(string[len(string)//2])
else:
    a=string[::-1]
    print(a[:len(a)//2])



#20.WAP to check whether the input character is a vowel or not. If it is vowel print
#‘VOWEL’ along with that character, if it is not just print ‘CONSONANT’.
string=eval(input('Enter the character: '))
if string in 'aeiouAEIOU':
    print(f'The given String contains vowels is "{string}" ')
else:
    print(f'The given String "{string}" is consonant ')



#21.WAP to check whether a given character is a vowel or consonant. if vowel, to print the next
#character of a given character or else print previous characters
string=eval(input('Enter the character: '))
if string in 'aeiouAEIOU':
    print(f'The given String contains vowels is "{string}" and next character is ',chr(ord(string) + 1))
else:
    print(f'The given String "{string}" is consonant  and previous character is',chr(ord(string) - 1))

#22.WAP to check whether a given string of first character is alphabet or not
#if the alphabet prints, reverse the string or else print the middle character.

#23.WAP to check whether a given string is less than 3 characters, to print the entire
#string otherwise to print after third positions to the remaining string.
string=eval(input('Enter the string: '))
if len(string)<=3:
    print(string)
else:
    print(string[3::])


    
#24.WAP to check whether a given length of the string is even or not. if even, to
#append the new string called "bye" or else print the first and last characters.
s=eval(input('Enter the string: '))
if len(s)%2==0:
    print(s+ ' '+'bye')
else:
    print( f'The first character is "{s[0]}" and the last character is "{s[-1]}"')


#24WAP to check whether a given length of the string is odd or not. if odd, to append
#the new string("Haii") from the starting of the given string, or else to avoid the
#starting character and ending character of the given string and to display the remaining characters.
s=eval(input('Enter the string: '))
if len(s)%2!=0:
     print('Haii'+s)
else:
    print(s[1:-1:])

    

#25.WAP to check whether the last of the given string is a special character or not, if
#the special character prints reverse the string except the last character or else to
#check if the length of the string is odd or not, if odd to extract the middle
#character to the end of the string.
string=eval(input('Enter the string: '))
if string[-1] in '@#!$%^&*(){}':
    print(string[:-1][::-1])
else:
    len(string)%2!=0
    print(string[len(string)//2:] + string[:len(string)//2])

 OR 
s=eval(input('Enter the string: '))
if  not s[-1].isalnum() :
    rev=s[::-1]
    print(rev)
    print(rev[-2::-1])
else:
  if len(a)%2==1:
    mid=(len(a)-1)//2
 print(mid)
print(a[mid]) #vn[collectiondata]


#26.WAP to check whether the given value is present inside the given collection or
#not.if value is present, display the value is available or else the value is not present.
value=eval(input('Enter the value :'))
if value in 'gjhkdkjh23849':
    print('value is available ')
else:
    print('value is not present.')
    

#27.WAP whether a given string, if string length is more than 2, then it displays a new
#string with the first and last characters switched, otherwise the display the 3
#copies of given string.
s=eval(input('Enter the string: '))
if len(s)>2:
    print()
else:
    print(s*3)

    
#28.WAP to check whether a given value is a list and first and last values should be
#integer if condition is satisfied first value is True division by 3 and perform the
#bitwise not for last value and those result values are stored in same positions in
#given list or else, to perform length of the collection power by 2 and display
#value.
value=eval(input('Enter the value :'))
if value[0]==[] and type(value)==int:
    value%3 and
   

#29.WAP to check whether a given value is a string or not and length of the value
#should be more than 7, if condition is satisfied to append the new string in the
#middle of the given string or else to perform the replications with 3 and display the result.
a=eval(input('Enter the value : '))
if type(a)==str and len(a)>7:
    print()
else:
    print(a*3)
     

#30.WAP to check if the given string of first and second character should be sequence
#or not. if the sequence prints the first, second and last two characters, or else the
#first half string is reversed and the remaining half string should be normal and
#display it.


#31WAP to check whether a given key is present in the dict or not. if key is present:
#display the value or else add key and new value inside the dict
a={3:'df',4:'rrewe',5:'dft'}
d=eval(input('Enter the key : '))
if d in a :
    print(a[d])
else:
    a[7]='cat'
    print(a)



#32.WAP to check whether a given collection is set or not. if set, append the new
#value, or else eliminate the duplicate values in collection. final results should be
#set type.
a=eval(input('Enter the data'))
if type(a)==set:
    a.add('GHEE')
    print(a)
else:
    print(set(a))

#33.WAP to read the age of a candidate and determine whether it is eligible for
#his/her own vote or not.it eligible print age and eligible messages or else print
#not eligible.
age=eval(input('Enter the age : '))
if age>=18 :
    print(f'You age is "{age}" then you are eligible for vote')
else:
    print('Not eligible')

#34WAP to check whether a given value is even and in between 65 to 90 and not in
#0 or odd. if condition is True, to perform display the ascii character or else to
#perform floor division with 5 and display it.
value=eval(input('Enter the value  : '))
if   value%2==0 and 65<=value<=90 :
    print(chr(value))
else:
    print(value//5)

   
#35.WAP to check whether the given string is palindrome or not if it is a palindrome
#string palindrome along with the string if it is not a palindrome print not
#palindrome
string=eval(input('Enter the string :'))
if string==string[::-1]:
    print(f'The given "{string}" is palindrome and output is"{string[::-1]}".')
else:
    print('The given string is not palindrome.')

    
#36.WAP to check whether a given number is palindrome or not. If palindrome,
#display the given value as a palindrome or else not a palindrome.
num=eval(input('Enter the number :'))
if num==num%10:
    print(f'The given "{num}" is palindrome and output is"{num[::-1]}".')
else:
    print('The given string is not palindrome.')

'''
#37.WAP to check length of both string collections are equal or not. if both are equal
#print the concat the two strings and display, or else if any one of the collection
#not equal print both the collections with lengths
    
