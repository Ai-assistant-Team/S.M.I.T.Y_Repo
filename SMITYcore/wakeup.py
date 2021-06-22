# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

import speech_recognition as sr
#from SMITY.SMITYcore.speechToText import listenForCommand
import SMITY.SMITYcore.speechToText


WAKEUP_WORDS_LIST = ['smity', 'smitty']


def waitForWakeup():
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    # # Uses Google's Speech Recognition Model

    while 1:
        try:
            # obtain audio from the microphone
            r = sr.Recognizer()

            with sr.Microphone() as source:
                audio = r.listen(source)

            # try to recognize what is being said
            try:
                userInput = r.recognize_google(audio)
                userInput = userInput.lower()

                # if user said a word from the WAKEUP_WORDS_LIST
                for WAKEUP_WORD in WAKEUP_WORDS_LIST:
                    if WAKEUP_WORD in userInput:
                        # activate
                        SMITY.SMITYcore.speechToText.listenForCommand()
                        break
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass
        except:
            pass
