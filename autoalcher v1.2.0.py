##autolicker test
import pyautogui
import numpy as np
import time
import datetime

count = 0

for i in [10,9,8,7,6,5,4,3,2,1]:
    print("starting in "+ str(i))
    time.sleep(1)

print("click it up!")

def breaktime():
#this guy determines if it should take a break
    breakroller = np.random.randint(0,450)
    hibernation_time = (np.random.randint(10,140)) #breaktime random time between 10-140 seconds
    if breakroller == 1:
        print("breakroller was " + str(breakroller)+ ". hibernating for "+ str(hibernation_time)+ " seconds")
        time.sleep(hibernation_time)
        
    else:
        print("breakroller was "+ str(breakroller)+ ". I would have hibernated for "+ str(hibernation_time) + " seconds.")

def dublclick():
    #needs to click twice within an average of ~3.02 seconds, each click separated by an average of .53 seconds
    wait1 = np.random.normal(loc=2.49,scale=.24)
    wait2 = np.random.normal(loc=.53, scale=.08)
    totalwait = wait1 + wait2
    time.sleep(wait1)
    pyautogui.click()
    time.sleep(wait2)
    pyautogui.click()
    
    #this guy tracks how many times its clicked
    print(" double clicked "+ str(wait1) +" and " + str(wait2) + " seconds wait. " + "total wait = " + str(totalwait))
    
    
def fuckup(): #simulates the player losing the count and clicking wildly a few times
    if np.random.randint(0,97) == 1: #triggered 1 out of every 97 cycles
        print("let's fuck it up!")
        for i in range(np.random.randint(2,6)): #click i many times (2-6), waiting avg .87 (norm dist) seconds between clicks
            time.sleep(np.random.normal(.87,.12))
            pyautogui.click()
            

for i in range(7000): #this determines the number of alchs to do
    dublclick()
    breaktime()
    fuckup()
    print("the count is "+ str(i))

with open('C:\\Users\\username\\Documents\\Personal\Projects\\Visual Studio Code 4.12.22\\Alchbot\\donezo.txt', 'w') as f:
    f.write("it appears not to have crashed. closed at "+ str(datetime.datetime.now()))