# 1. Write a python program to display a user entered name followed by Good Afternoon using
input() function.
name=input('Enter your name :')
print(f'Good Afternoon, {name}')

# 2. Write a program to fill in a letter template given below with name and date using input function.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
a=input('Enter the name :')
b=input('Enter the date :')
print(letter.replace('<|Name|>',a).replace('<|Date|>',b))

# 3. Write a program to detect triple space in a string.
a='mahad the   genius'
b=a.find('   ')
print(b)

# 4. Replace the triple space from problem 3 with single spaces.
a='mahad the   genius'
print(a.replace('   ',' '))

# 5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\n\t This python course is nice.\n Thanks!"
print(letter)
