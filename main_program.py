
'''Project 1 : Snake Water Gun Game

We all have played snake, water gun game in our childhood. If you havenʼt,
google the rules of this game and write a python program capable of playing
this game with the user.'''

'''
snake=1
water=2
gun=3
'''

import random
 
computer=random.choice([1,2,3])
you_str=input('Enter your choice :')
youdict={'s':1, 'w':2, 'g':3}
reverse_dict={1:'snake', 2:'water', 3:'gun'}
you= youdict[you_str]
print(f'you chose {reverse_dict[you]}\n computer chose {reverse_dict[computer]}')

if(computer==you):
    print("Its a draw")

else:
    if(computer==1 and you==2): 
        print("you lose")
    elif(computer==1 and you==3):
        print("you win")

    elif(computer==2 and you==1): 
        print("you win")
    elif(computer==2 and you==3):
        print("you lose")

    elif(computer==3 and you==1):
        print("you lose")
    elif(computer==3 and you==2):
        print("you win")

    else:
        print('Something went worng')
