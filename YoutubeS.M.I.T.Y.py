import speech_recognition as sr         # importing speech_recognition module and giving name
import pyttsx3                          # importing pyttsx3 module
import pywhatkit                        # importing pywhatkit module
import datetime                         # importing datetime module
import wikipedia                        # importing wikipedia module

listener = sr.Recognizer()                      # recognizer to recognize your voice
engine = pyttsx3.init()                         # pyttsx3 is a text-to-speech conversion library in Python
voices = engine.getProperty("voices")           # making a male voice sound female
engine.setProperty("voice", voices[2].id)       # making a male voice sound female


##
## This function is used for machine to speak
##

def talk(text):             # declaring a function and every time we call this she is starting to speak
    engine.say(text)        # causes it to stop for a brief period of time to say the queued text.
    engine.runAndWait()     # end of <talk/Structure>



##
## This function is using your microphone to tell you the time or search on wikipedia for the person you told her
##

def take_command():                                                     # declaring a function
    try:                                                                # incase microphone not work
        with sr.Microphone() as source:                                 # use microphone and give name(source)
            print("Listening...")                                       # printing Listening
            talk("Listening...")                                        # saying she is listening
            voice = listener.listen(source)                             # listen to this source
            command = listener.recognize_google(voice)                  # provides access to the speech recognition service
            command = command.lower()                                   # Python string method lower() returns a copy of the string in which all case-based characters have been lowercased.
            if "smity" in command:                                      # working only if she hears her name(smity)
                command = command.replace("smity", "")                  # replacing word smity with blank
                talk(command)                                           # if "smity" in command she will talk
            elif "time" in command:                                     # saying time only if she hears the word "time"
                time = datetime.datetime.now().strftime("%I:%M %p")     # recognizing time
                print(time)                                             # printing time
                talk("Current time is" + time)                          # saying current time is...
            elif "who is " in command:                                  # giving wikipedia info if she hears the sentence"who is"
                person = command.replace("who is ", "")                 # replacing "who is" with blank
                info = wikipedia.summary(person, 3)                     # recognizing wikipedia info and giving 3 lines answer
                print(info)                                             # printing info
                talk(info)                                              # saying info
    except:                                                             # python will ignore when except happens
        pass
    return command                                                      #end of <take_command/Structure>


##
## This function is searching youtube the video you told her
##


def run_smity():                                            # declaring a function
    command = take_command()                                # taking a command from user
    if "play" in command:                                   # playing only if she hears the word play
        song = command.replace("play", "")                  # replacing the word play with blank
        talk("playing" + song)                              # she says that she is playing and the song name
        pywhatkit.playonyt(song)                            # opening youtube and playing what user said
                                                            # end of <run_smity/Structure>


run_smity()                                                 # running smity