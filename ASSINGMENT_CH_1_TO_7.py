# Assingment Questions

 # 1. Write a Python program to print 'Hello, World!' on the screen.
a='Hello,World!'
print(a)

# # 2. Write a Python program to accept two numbers from the user and display their sum.
a1=int(input('Enter the number 1:'))
a2=int(input('Enter the number 2:'))

b=(a1+a2)
print(b)

# # 3. Write a Python program to check whether a number entered by the user is even or odd.
n=int(input('Enter the number:'))
if(n%2)==0:
    print('The number is even')

else:
    print('The number is odd')

# # 4. Write a Python program to find the largest among three user-entered numbers.
a1=int(input('Enter the number 1:'))
a2=int(input('Enter the number 2:'))
a3=int(input('Enter the number 3:'))

print('largest =',max(a1,a2,a3))

# # 5. Write a Python program to display the multiplication table of a user-entered number.
n=int(input('Enter the number:'))

for i in range(1,11):
    print(f'{n}X{i}={n*i}')

# # 6. Write a Python program to count the number of vowels in a string entered by the user.
a=input('enter the string:')
count=0
for n in a.lower():
    if n in 'aeiou' :
        count+=1
        print('vowels=',count)

# # 7. Write a Python program to reverse a string entered by the user.
s=input('Enter string:')
print(s[ : :-1])

# # 8. Write a Python program to print all numbers between 1 and 100 that are divisible by 5.
i=()

for i in range(1,101):
    if(i%5==0):
        print(i)
