"""
Created on Sat Mar 27 13:08:39 2021

@author: manolispolymeneris
"""

import pyjokes #Imports random joke generator library

def jokes():

    try:
        for i in range(9, 105): #Runs the list with jokes
            joke = pyjokes.get_joke() #Generates a joke
            return joke #Returns and prints the joke
        
    except:
        return 1 #Undefined error
