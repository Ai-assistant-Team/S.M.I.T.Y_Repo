# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Wed Mar 31 17:46:42 2021

@author: fotis
"""
#function that translates a given text to the given language
def translateText(textToTranslate = input('Give text to translate: '),lang = input('Choose language: ')):
    
    #import the needed libraries
    from googletrans import Translator
    
    #Google Translate ajax API implementation class
    translator = Translator()
    
    #Translate text from source language to destination language
    translated = translator.translate(textToTranslate,dest=lang)
    
    #Show the translated text on screen
    print(translated.text)

