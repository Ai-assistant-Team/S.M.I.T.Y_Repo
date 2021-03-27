"""
Created on Mon Mar 22 06:25:31 2021
@author: Δημήτρης
"""

import os
t2s("Hello World")  #inside the () you add what the program will say



def t2s(text):       #text to speech function 
    #This function here takes the value of [text] and it creates a .mp3 file of the computer reading it in english
    #after that it opens the file and plays it.

    from gtts import gTTS  #In order to communicate with google's text to speech
    tts = gTTS(text, lang='en')
    tts.save("AI.mp3")    
    os.startfile("AI.mp3")       #end of text to speech

