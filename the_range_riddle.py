'''
1. The Range Riddle

Objective: The aim of this assignment is to deepen your understanding of Python's 
range() function.

Task 1: Your Mood Today Write a program that prints off different moods for each day 
of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". 
Using the range() function, loop through every day of the week and for each day, 
randomly select a mood from the list and print it. Ensure that your program includes 
the use of the random module to select the mood.

Example Outcome: An example output could be "On Wednesday, you were feeling 
happy." "On Thursday you were feeling sad."
'''
# import the module

import random


# create a list for the days and the moods

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm", "Chill", "Down", "Nonchalant", "Positive",
         "Stoked", "Grateful", "Abundant"]



# use for loop in range, days once thru, print random moods

for day in range(len(days)):   # I had to use range, and the len 
    print(f"Today is {days[day]}, I'm feeling {random.choice(moods)}!")

