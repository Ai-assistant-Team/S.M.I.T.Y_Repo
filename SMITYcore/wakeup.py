#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

import speech_recognition as sr
from speechToText import listenForCommand


WAKEUP_WORDS_LIST = ['smity', 'smitty']


def waitForWakeup():
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
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

                for WAKEUP_WORD in WAKEUP_WORDS_LIST:
                    if WAKEUP_WORD in userInput:  # userInput.count(WAKEUP_WORD) > 0:
                        listenForCommand()
                        break
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass
        except:
            pass