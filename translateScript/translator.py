#import the needed libraries
from googletrans import Translator

#function that translates a given text to the given language
def translateText(textToTranslate,lang):

    try:
        #Google Translate ajax API implementation class
        translator = Translator()
    
        #Translate text from source language to destination language
        translated = translator.translate(textToTranslate,dest=lang)
   
        #Show the translated text on screen
        return print(translated.text)
    except:
        return 1
