# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

from SMITY.SMITYcore.initialization import init
from SMITY.SMITYcore.wakeup import waitForWakeup
from SMITY.SMITYcore.parallelProgramming import call_function
# from time import sleep


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

    import SMITY.SMITY_GUI.gui3

    call_function(SMITY.SMITY_GUI.gui3.main())
    # sleep(0.00000000001)

    # ------------------------------

    # ------------------------------
    # Listen For Wakeup Word
    # ------------------------------

    ## Start a parallel process that
    ## waits to hear the word 'SMITY'.
    ## When it does, it spawns a new
    ## speech2text to hear the request

    call_function(waitForWakeup)
    # sleep(0.00000000001)

    # ------------------------------
