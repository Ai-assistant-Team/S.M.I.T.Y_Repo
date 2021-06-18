#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

import speech_recognition as sr
from textToSpeech import Text2Speech
from printToGUI import print2gui
from errorHandling import handleError
from main import recognizeAndAct


def greeting():
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    from random import choice

    list_of_greetings = ['How may I be of service?', 'How may I assist you?', 'What can I do for you?']
    return choice(list_of_greetings)


def listenForCommand():
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # # Uses Google's Speech Recognition Model

    # obtain audio from the microphone
    userInput = listen()
    if type(userInput) == str:
        recognizeAndAct(userInput.lower())
    else:
        return userInput
    # try:
    #     r = sr.Recognizer()
    #
    #     with sr.Microphone() as source:
    #         Text2Speech().speak(greeting())
    #         print2gui('Listening...')
    #
    #         audio = r.listen(source)
    #
    #         try:
    #             userInput = r.recognize_google(audio)
    #             print2gui('User :  ', userInput)
    #
    #         except sr.UnknownValueError:
    #             return 7
    #
    #         except sr.RequestError as e:
    #             print2gui('Error. Could not request results; {0}'.format(e))
    #             return 10
    #
    #     return intentRecognition(userInput.lower())
    #
    # except:
    #     # handleError(1)  # 1 : Did not understand that
    #     return 1


def listen():
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # # Uses Google's Speech Recognition Model

    # obtain audio from the microphone
    try:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            Text2Speech().speak(greeting())
            print2gui('Listening...')

            audio = r.listen(source)

            try:
                userInput = r.recognize_google(audio)
                print2gui('User :  ', userInput)

                return userInput

            except sr.UnknownValueError:
                return handleError(7)  # 7 : Did not understand that

            except sr.RequestError as e:
                print2gui('Error. Could not request results; {0}'.format(e))
                return handleError(10)     # 10 : No Internet Connection

    except:
        return handleError(1)  # 1 : Did not understand that


def callListenFromGUI():
    try:
        check = listenForCommand()
        if type(check) is int:
            handleError(check)
    except:
        Text2Speech().speak('Something Went Wrong.')
