# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

# ------------------------------
# For Parallel Programming
# ------------------------------
import multiprocessing
import SMITY.SMITYcore.textToSpeech
from SMITY.SMITYcore.errorHandling import handleError


def communicateWithRunningFunctions(conn):
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    ##
    ## function to print the messages received from running job.
    ## This function is not meant to be imported by another script.
    ## It is used directly from <call_function_wCommunication>
    ##
    while 1:
        msg = conn.recv()
        if type(msg) == str:
            # SMITY.SMITYcore.printToGUI.print2gui("{}".format(msg))
            SMITY.SMITYcore.textToSpeech.Text2Speech().speak("{}".format(msg))
        elif type(msg) == int:
            handleError(msg)
        else:
            return 1
# end of communicateWithRunningFunctions


def call_function_wCommunication(function2beCalled, *functionsArgs):
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    parent_conn, child_conn = multiprocessing.Pipe()

    p_function = multiprocessing.Process(target=function2beCalled, args=(parent_conn, *functionsArgs))
    receiver = multiprocessing.Process(target=communicateWithRunningFunctions, args=(child_conn,))

    receiver.start()
    p_function.start()

    p_function.join()
    receiver.join()


def call_function(function2beCalled, *functionsArgs):
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    p_function = multiprocessing.Process(target=function2beCalled, args=(*functionsArgs,))

    p_function.start()
    p_function.join()

# ------------------------------
# End <For Parallel Programming>
# ------------------------------
