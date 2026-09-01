# 1. Write a program using functions to find greatest of three numbers.
a1=int(input("enter the number 1 :"))
a2=int(input("enter the number 2 :"))
a3=int(input("enter the number 3 :"))

def greatest(a1,a2,a3):
    if(a1>a2 and a1>a3):
        return 'a1 is greatest'
    
    elif(a2>a1 and a2>a3):
        return 'a2 is greatest'

    else:
        return('a3 is greatest')

print (greatest(a1,a2,a3))


# 2. Write a python program using fuction to convert Fahrenheit to celsius.
t=int(input("Enter the temperature : "))
  
def f_to_c(t):
    return 5*(t-32)/9

c=f_to_c(t)
print(f"{round(c,3)} degree celsius")

# 3. Write a recursive function to calculate the sum of first n natural numbers.
n=int(input("Enter the number : ")) 

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(n))

# 4. Write a python function to print first n lines of the following pattern.
# ***
# **  for n = 3
# *

n=int(input("enter the number :"))

def patren(n):
    if(n==0):
        return ''
    print('*'*n)
    pattern(n-1)
pattern(n)


# 5. Write a python function which converts inches to cms.
inches=int(input("enter the inches :"))

def inch_to_cm(inches):
    return inches*2.54

print(inch_to_cm(inches))

# 6. Write a python function to remove a given word from a list and strip it at the same time.

l=['harry', 'mahad',' farman', 'affan', 'azkia']

def rem(l, word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

print(rem(l, 'an'))

# 7. Write a python function to print multiplication table of a given number.
n=int(input("enter the table :"))

def table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
table(n)

