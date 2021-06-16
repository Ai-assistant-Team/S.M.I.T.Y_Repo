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

def testCaseOne():
    translateText('dog','hr')

def testCaseTwo():
    translateText(0,0)

def testCaseThree():
    translateText('dog','english')

def testCaseFour():
    translateText('dog',0)

def testCaseFive():
    translateText(0,'el')
