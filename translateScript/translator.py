#import the needed libraries
from googletrans import Translator

#function that translates a given text to the given language
def translateText():

    #Gives the text and the langugage to translate to
    textToTranslate = input('Give text to translate: ')
    lang = input('Choose language: ')

    try:
        #Google Translate ajax API implementation class
        translator = Translator()
    
        #Translate text from source language to destination language
        translated = translator.translate(textToTranslate,dest=lang)
    except:
        return print('Wrong input.')
    #Show the translated text on screen
    return print(translated.text)


