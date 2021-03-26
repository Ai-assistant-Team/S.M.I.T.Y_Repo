# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:50:47 2021

@author: fotis
"""

#function to count from a number to another. The default number to start counting is 1 but the user can 
#switch it and start counting from another number. He can also choose a speed to count. The default speed
#is "Normal" but he can choose between "Fast" or "Slow".Any other words for speed wont be accepted.

def countTo(to,countFrom=1,speed="Normal"):  #3 variables
    
    import time #library to slow the system in order to count in a specific speed
    
    while(countFrom<=to):      
        if(speed=="Normal"):  #if the speed is set to "Normal" the scrip counts every one second
            print(countFrom)
            time.sleep(1)
            countFrom += 1
        elif(speed=="Slow"): #if the speed is set to "Slow" the scrip counts every two seconds
            print(countFrom)
            time.sleep(2)
            countFrom += 1
        elif(speed=="Fast"): #if the speed is set to "Fast" the scrip counts every three seconds
            print(countFrom)
            time.sleep(0.5)
            countFrom += 1
  
#function to count down from a number to 1. The default number to count down to is 1 but the user can 
#switch it and start counting down to another number. He can also choose a speed to count down. The default speed
#is "Normal" but he can choose between "Fast" or "Slow".Any other words for speed wont be accepted.
            
def countDown(countDownFrom,countDownTo=1,speed="Normal"):
    
    import time  #library to slow the system in order to count  down in a specific speed
    
    while(countDownFrom>=countDownTo):
            if(speed=="Normal"):        #if the speed is set to "Normal" the scrip counts down every one second
                print(countDownFrom)
                time.sleep(1)
                countDownFrom -= 1
            elif(speed=="Slow"):        #if the speed is set to "Slow" the scrip counts down every two seconds
                print(countDownFrom)
                time.sleep(2)
                countDownFrom -= 1
            elif(speed=="Fast"):        ##if the speed is set to "Fast" the scrip counts every three seconds
                print(countDownFrom)
                time.sleep(0.5)
                countDownFrom -= 1
            
            