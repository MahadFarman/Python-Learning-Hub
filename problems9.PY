# 1. Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
# contains the word ‘twinkleʼ.
f=open("poems.txt")
content=f.read()

if("twinkle" in content):
    print("The word twinkle is present")

else:
    print("The word twinkle is not present")

f.close()

# 2. The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
# Hi-score. You need to write a program to update the Hi-score whenever the game()
# function breaks the Hi-score.
import random

def game():
    print("you are playing a game")
    score=random.randint(1,100)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore !=""):
            hiscore= int(hiscore)
        else:
            hiscore= 0
        print(f"your score is {score}")
        if(score>hiscore):
            with open("hiscore.txt","w") as f:
                f.write(str(score))
        return score 
game()       
    

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old.
def generateTable(n):
    table=""
    for i in range(1,11):
        table+= f"{n}x{i}={n*i}\n" 

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)

# 4. A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.
word='donkey'

with open("file.txt") as f:
    content= f.read()

newcontent= content.replace( word, '#####')

with open("file.txt", 'w') as f:
    f.write(newcontent)

# 5. Repeat program 4 for a list of such words to be censoredFILE.
words=['donkey','good','animal']

with open("file.txt") as f:
    content= f.read()

for word in words:
   content= content.replace(word, "#"* len(word))

with open("file.txt", 'w') as f:
    f.write(content)

# 6. Write a program to make a copy of a text file “this.txt”.
with open("file.txt") as f:
    content=f.read()

with open("copy.txt","w") as f:
    f.write(content)

# 7. Write a program to find out whether a file is identical and matches the content of another
with open("file.txt") as f:
    content1=f.read()

with open("copy.txt") as f:
    content2=f.read()

if(content1 == content2):
    print("yes, these files are identical ")
else:
    print("no, these files are not identical ")

# 8. Write a program to wipe out the content of a file using python.
with open("emptyfile.txt","w") as f:
    content=f.write("")

