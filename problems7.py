# 1. Write a program to print multiplication table of a given number using for loop

t=int(input('Enter the number for table :'))

i=0
for i in range(i,11):
    print(f"{t}X{i}={t*i}")

# 2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Mahad", "Mustafa", "Ahad","Sarim"]

for name in l:
    if(name.startswith('M')):
        print(f'God bless you {name}')
 
# 3. Attempt problem 1 using while loop.
t=int(input('Enter the number for table :'))

i=1
while(i<11):
    print(f"{t}X{i}={t*i}")
    i+=1
 
# 4. Write a program to find whether a given number is prime or not.
a=int(input('Enter the number :'))

for i in range(2,a):
    if(a%2==0):
        print("The number is not prime")

    else:
        print("The number is prime")
        
# 5. Write a program to find the sum of first n natural numbers using while loop.
n=int(input("Enter the number :"))

i=1
sum=0
while(i<=n):
    sum+=i
    i+=1

print(sum)
 
# 6. Write a program to calculate the factorial of a given number using for loop.
n=int(input('enter the number:'))

product=1

for i in range(1, n+1):
    product = product * i

print(f'the factorial of {n} is {product}')
 
# # 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3
n=int(input("Enter the number : "))

for i in range(1 ,n+1):
    print(' '* (n-i) ,end="")
    print('*'*(2*i-1),end="")

print('')

# 8. Write a program to print the following star pattern: 
# *
# **
# *** for n = 3
n=int(input("Enter the number :"))

for i in range(1, n+1):
    print(" "*(n-1),end="")
    print("*"*(i),end="")

print('')


# 9. Write a program to print the following star pattern.
# * * *
# *   *
# * * *
n=int(input("Enter the number :"))

for i in range(1, n+1):
    if(i==1 or n==i):
        print("*" *n,end="")
    
    else:
        print("*", end="")
        print(" " *(n-2),end="")
        print("*" ,end="")
    print("")

# 10. Write a program to print multiplication table of n using for loops in reversed order
t=int(input('Enter the number for table :'))

i=0
for i in range(i,10):
    print(f"{t}X{10-i}={t*(10-i)}")