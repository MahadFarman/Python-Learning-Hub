# Practice Set

# 1. Create a class “Programmer” for storing information of
# few programmers working at Microsoft.
# class programmer:
#     company="Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name= name
#         self.salary= salary
#         self.pin= pin

# p1=programmer("Mahad", 130000, 1234)
# print(p1.name, p1.salary, p1.pin)

# p2=programmer("ahad", 140000, 98605)
# print(p2.name, p2.salary, p2.pin)

# 2. Write a class “Calculator” capable of finding square, cube 
# and square root of a number.
# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#             print(f"The square of this no. is {self.n * self.n}")

#     def cube(self):
#             print(f"The cube of this no. is {self.n * self.n * self.n}")

#     def squareroot(self):
#             print(f"The squareroot of this no. is {self.n**1/2}")

# a=int(input("Enter the number :"))

# cal=Calculator(a)

# cal.square()
# cal.cube()
# cal.squareroot()

# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
# ‘object.a = 0ʼ. Does this change the class attribute?
# class demo:
#     a=4 # Class attribute

# o=demo()

# print(o.a) # Accessing the class attribute through the object

# o.a=0  # Creates an instance attribute; class attribute is not changed

# print(o.a) # Instance attribute → 0
    
# print(demo.a) # Class attribute remains unchanged → 4

# 4. Add a static method in problem 2, to greet the user with hello.
# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#             print(f"The square of this no. is {self.n * self.n}")

#     def cube(self):
#             print(f"The cube of this no. is {self.n * self.n * self.n}")

#     def squareroot(self):
#             print(f"The squareroot of this no. is {self.n**1/2}")


#     @staticmethod
#     def greet():
#         print('Hello user')

# a=int(input("Enter the number :"))

# cal=Calculator(a)

# cal.greet()
# cal.square()
# cal.cube()
# cal.squareroot()

# 5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Pakistani Railways.
from random import randint

class Train:
    def __init__(self, Train_no, seats):
        self.Train_no= Train_no
        self.seats= seats
    
    def book(self, fro, to):
        if self.seats > 0:
            self.seats -=1
        print(f"Ticket is booked in Train_no : {self.Train_no} from {fro} to {to}")
    
    def get_status(self):
        print(f"Train No: {Train_no} has {self.seats} seats avaible")
    
    def fare(self, fro, to):
        fare= randint(200,2000)
        print(f"Ticket from {fro} to {to} is Rs: {fare}")
Train_no=int(input("Enter your Ticket_no :"))
seats=int(input("Enter your seat_no :"))
fro=input("Enter starting station :")
to=input("Enter your destination :")

t=Train(Train_no, seats)

t.book(fro,to)
t.get_status()
t.fare(fro, to)

    



# 6. Can you change the self-parameter inside a class to something else (say “harry”)? Try
# changing self to “slf” or “mahad” and see the effects.
# class employee:
#     company="GETZ_PHARMA"
#     def __init__(slf, name, salary, position):
#         slf.name= name
#         slf.salary=salary
#         slf.position=position

# a=employee("mahad", 123999, 'data analyist')
# print(a.name, a.salary, a.position)

# class employee:
#     company="SAMSUNG"
#     def __init__(MAHAD, name, salary, position):
#         MAHAD.name= name
#         MAHAD.salary=salary
#         MAHAD.position=position

# a=employee("mahad", 123999, 'data analyist')
# print(a.name, a.salary, a.position)



