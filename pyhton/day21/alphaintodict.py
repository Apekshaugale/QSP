#66.wap to check whether a character is in the alphabet or not,if it is alphabet, store the value inside
#a dict(key as a character and value as a ascii value)
character=eval(input('Enter the character : '))
x={}
if character.isalpha():
    print(f'The given character "{character}" is in alphabet.')
    x[character]=ord(character)
    print(x)
