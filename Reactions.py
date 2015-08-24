# -*- coding: utf-8 -*-
import time
import random


print ("Let's measure your reaction time.")
print ("Do you want to play?")
vec = []

while True:
    global play
    play = input("y/n? :")
    if play == 'y':
        print ("Press the return key when prompted")
        break
    elif play == 'n':
        print ("Goodbye!")
        break
    else:
        print ("Please enter y or n")

while play == 'y':
    print ("Press return when you are ready.")
    ready = input(">")
    delay = random.uniform(0,3)
    time.sleep(delay)
    print ("Ready, go!")
    start = time.time()
    reaction = input(">")
    end = time.time()
    speed = end - start
    vec.append(speed)
    print ("Your reaction time is ", speed, " seconds.")
    print ("Do you want to play again?")
    again = input("y/n? :")
    if again == 'y':
        play = 'y'
    else:
        print ("Thanks for playing")
        break


print ("Your average reaction time is ", sum(vec)/len(vec), " seconds.")

time.sleep(2)
       
exit()   
    
    