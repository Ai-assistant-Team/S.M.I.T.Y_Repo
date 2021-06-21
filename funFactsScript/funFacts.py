"""
Created on Sat Mar 27 13:08:39 2021

@author: manolispolymeneris
"""


def funFacts():
    
    try:
        import randfacts #Imports random fun fact generator library
        for i in range(5142): #Runs the list with fun facts
            fact = randfacts.getFact() #Generates a fun fact
            return fact #Returns and prints the fun fact
    
    except:
        return 1 #Undefined error
