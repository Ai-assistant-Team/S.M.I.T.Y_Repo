"""
Created on Sat Mar 27 13:08:39 2021

@author: manolispolymeneris
"""

import randfacts #Imports random fun fact generator library

def funFacts():
    
    for i in range(5142): #Runs the list with fun facts
        fact = randfacts.getFact() #Generates a fun fact
        print(fact) #Prints the fun fact
        
        return 0
        
funFacts()
