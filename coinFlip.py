'''
Created on Mar 7, 2020

@author: ITAUser
'''
import random
keepPlaying = True
while(keepPlaying):
    print("Test your luck! Press 's' to begin.")
    user = 's'
    while (user == 's'): 
        Toss = random.randint(0,1)
        userinput = input ("To quit: ")
        if ("q" ==userinput):
            keepPlaying = False
                
        elif Toss ==0:
            print("Heads!")
        else:
            print("Tails!")
            
    
    