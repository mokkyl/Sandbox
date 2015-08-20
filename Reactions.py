# -*- coding: utf-8 -*-
import time
import random


print "Let's measure your reaction time."
print "Do you want to play?"


while True:
    global play
    play = raw_input("y/n? :")
    if play == 'y':
        print "Press the return key when prompted"
        break
    elif play == 'n':
        print "Goodbye!"
        break
    else:
        print "Please enter y or n"

while play == 'y':
    print "Press return when you are ready."
    ready = raw_input(">")
    delay = random.uniform(0,3)
    time.sleep(delay)
    print "Ready, go!"
    start = time.time()
    reaction = raw_input(">")
    end = time.time()
    speed = end - start
    print "Your reaction time is ", speed, " seconds."
    print "Do you want to play again?"
    again = raw_input("y/n? :")
    if again == 'y':
        play = 'y'
    else:
        print "Thanks for playing"
        break
 

time.sleep(2)
       
exit()   
    
    