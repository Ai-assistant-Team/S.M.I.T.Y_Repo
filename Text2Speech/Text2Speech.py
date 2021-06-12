<<<<<<< HEAD
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

=======
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

>>>>>>> 2d0c9e829aaeb0a0b78aa6fa26a69f95b3db7c56
t2s(text)