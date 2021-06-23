# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

from SMITY.SMITYcore.initialization import init
from SMITY.SMITYcore.wakeup import waitForWakeup
from SMITY.SMITYcore.parallelProgramming import call_function

if __name__ == '__main__':

    # ------------------------------
    # Initialize App
    # ------------------------------

    try:
        
        init()
        
    except:
        
        # if initialization fails, then GUI doesn't work, so errorHandling can't be used
        # and the user is notified from the standard output.
        print('Initialization Failed.')
        exit(1)

    # ------------------------------
    
    # ------------------------------
    # Initialize GUI
    # ------------------------------

    # Problem with GUI, not used

    # ------------------------------

    # ------------------------------
    # Listen For Wakeup Word
    # ------------------------------

    ## Start a parallel process that
    ## waits to hear the word 'SMITY'.
    ## When it does, it spawns a new
    ## speech2text to hear the request

    p = call_function(waitForWakeup)


    # ------------------------------
