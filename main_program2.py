
'''Project 1 : Rock,Paper,Scissors  game

We all have played Rock,Paper,Scissors  game in our childhood. If you havenʼt,
google the rules of this game and write a python program capable of playing
this game with the user.'''

'''
Rock=1
Paper=2
Scissors =3

'''
import random

computer=random.choice([1,2,3])
you_str=input('Enter your choice :')
youdict={'r':1,'p':2,'s':3}
reverse_dict={1:'Rock', 2:'Paper', 3:'Scissors '}
you=youdict[you_str]

print(f'You chose {reverse_dict[you]}\nComputer chose {reverse_dict[computer]}')

if(computer==you):
    print('its a draw')

else:
    if(computer==1 and you==2):
        print('you win')
    elif(computer==1 and you==3):
        print('you lose')

    elif(computer==2 and you==1):
        print('you lose')
    elif(computer==2 and you==3):
        print('you win')

    elif(computer==3 and you==1):
        print('you win')     
    elif(computer==3 and you==2):
        print('you lose')

    else:
        print('something went worng')      