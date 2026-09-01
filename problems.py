# # 1. Write a program to print Twinkle twinkle 
# little star poem in python.
print(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

# 3. Install an external module and use it to 
import pyttsx3
engine = pyttsx3.init()
engine.say("mahad the genius ")
engine.runAndWait()

# Write a python program to print the contents of a directory
#  using the os module. 
import os
path = r'C:\Users\fisba\Desktop\PYTHON COURSE'
contents = os.listdir(path)
print("Contents of the directory:")
for item in contents:
    print(item)


# 5. Label the program written in problem 4 with comments.
# mahad the genius