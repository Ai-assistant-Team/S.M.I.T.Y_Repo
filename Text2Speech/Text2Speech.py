"""
Created on Sat May 8 
@author: Δημήτρης Σούμπασης
"""

import os
import pyttsx3

text = 'hello world'  #Here you write what you want to hear
engine = pyttsx3.init()

def t2s(text):

    engine.say(text)
    engine.runAndWait() 

t2s(text)