# 1. Write a program to create a dictionary of english words with values as their urdu
# translation. Provide user with an option to look it up!
words = {
    'help': 'madad',
    'shoes': 'chappal',
    'class': 'jamat',
    'chair': 'kursi'
}

word = input('Enter the word: ')

if word in words:
    print('The translation of this word is:', words[word])
else:
    print('This word is not included in dictionary')

# 2. Write a program to input eight numbers from the user and display all the unique numbers
(once).
s=set()

n1=int(input('enter the number 1 :'))
s.add(n1)

n2=int(input('enter the number 2 :'))
s.add(n2)

n3=int(input('enter the number 3 :'))
s.add(n3)

n4=int(input('enter the number 4 :'))
s.add(n4)

n5=int(input('enter the number 5 :'))
s.add(n5)

n6=int(input('enter the number 6 :'))
s.add(n6)

n7=int(input('enter the number 7 :'))
s.add(n7)

n8=int(input('enter the number 8 :'))
s.add(n8)

print(s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s={18,'18'}
print(s,type(s))

Yes,we have a set with 18 (int) and '18' (str) as a value in it

# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(s,len(s))


# 5.What is the type of 's'?
s= {}
print(s,(type(s)))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.
d={}
n=input('Enter the name :')
l=input('Enter the lang :')
d.update({n:l})

n=input('Enter the name :')
l=input('Enter the lang :')
d.update({n:l})

n=input('Enter the name :')
l=input('Enter the lang :')
d.update({n:l})

n=input('Enter the name :')
l=input('Enter the lang :')
d.update({n:l})

print(d)

# 7. If the names of 2 friends are same what will happen to the program in problem 6?
if the names of 2 friends are same  in the program in problem 6 then the language enter 
later is add to dictionary and previous is skip due to update command.


# # 8. If languages of 2 friends are same; what will happen to the program in problem 6?
if the languages of 2 friends are same  in the program in problem 6 then the language enter 
later is also add to dictionary and previous is not skip .

# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
no we Can not change

