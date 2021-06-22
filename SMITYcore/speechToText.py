# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

import speech_recognition as sr
from SMITY.SMITYcore.textToSpeech import Text2Speech
from SMITY.SMITYcore.printToGUI import print2gui
from SMITY.SMITYcore.errorHandling import handleError


def greeting():
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    from random import choice

    list_of_greetings = ['How may I be of service?', 'How may I assist you?', 'What can I do for you?']

    return choice(list_of_greetings)
# end of greeting


def listenForCommand():
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    from SMITY.SMITYcore.takeAction import recognizeAndAct

    # takes the user's input (returned as a string)
    userInput = listen()

    if type(userInput) == str:
        # forwards that input to the recognizeAndAct function, in order to determine what action did the user request.
        recognizeAndAct(userInput.lower())
    else:
        # If type(userInput) is not str, then listen() returned an error code.
        # This code is handled from inside listen(), so there is nothing more to do, except to return the code
        #   and let the calling function know what went wrong.
        return userInput
# end of listenForCommand


def listen():
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    ## Listens for the user's input and returns it as a string

    ## Uses Google's Speech Recognition Model

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
        return handleError(1)  # 1 : Something Went Wrong (General Error)
# end of listen


def callListenFromGUI():
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    # This function is called from GUI, when the user clicks on the <Microphone Button>, and has no return statement.
    try:
        check = listenForCommand()
        if type(check) is int:
            handleError(check)

    except:
        Text2Speech().speak('Something Went Wrong.')
# end of callListenFromGUI
