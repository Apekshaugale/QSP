#67.wap to check whether a character is in uppercase or not,
#if uppercase, convert to lowercase and store the value inside the dictionary
#(character as key and ascii as value) take user input
character=eval(input('Enter the character : '))
dictionary={}
if character.isupper():
    print(f'The given character "{character}"  in lowercase = ',character.lower())
    dictionary[character]=ord(character)
    print(dictionary)
