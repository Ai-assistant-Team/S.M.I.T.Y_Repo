# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:08:39 2021

@author: manolispolymeneris
"""

def jokes():
    import pyjokes #Imports random joke generator library
    
    for i in range(298): #Runs the list with jokes
        joke = pyjokes.get_joke() #Generates a joke
        print(joke) #Prints the joke
        
        request = input("Do you want to see another Joke? Yes/No: ") #Asks user if we wants another joke
        
        if (request!="Yes" and request!="No"): #Checks if answer isn't "Yes" or "No"
            print("Invalid Answer") #Prints that the answer is not valid
            break
        #end of if
        if (request=="No"): #Checks if user wants another joke
            break
        #end of if
    #end of for
        
jokes()