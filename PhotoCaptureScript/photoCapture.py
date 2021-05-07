from ecapture import ecapture as ec
#import the parts of the ecapture that are needed

def capturing():

    ec.capture(0,"robo camera","img.jpg")

#The capture function takes three arguments:

#Camera index(first connected webcam will be of index 0. The next webcam will be of index 1)

#Window name (It can be a variable or a string. If you don't wish to see the window, type False)

#Save name (It can be a variable or a string. If you don't wish to save the image, type False)

capturing()

