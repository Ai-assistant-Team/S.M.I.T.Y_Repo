# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:08:39 2021

@author: manolispolymeneris
"""

def funFacts():
    import randfacts #Imports random fun fact generator library
    
    for i in range(5142): #Runs the list with fun facts
        fact = randfacts.getFact() #Generates a fun fact
        print(fact) #Prints the fun fact
        
        request = input("Do you want to see another Fun Fact? Yes/No: ") #Asks user if we wants another fun fact
        
        if (request!="Yes" and request!="No"): #Checks if answer isn't "Yes" or "No"
            print("Invalid Answer") #Prints that the answer is not valid
            break
        #end of if
        if (request=="No"): #Checks if user wants another fun fact
            break
        #end of if
    #end of for
        
funFacts()
