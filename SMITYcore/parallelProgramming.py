#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

# ------------------------------
# For Parallel Programming
# ------------------------------
import multiprocessing
from SMITY.SMITYcore.printToGUI import print2gui
from SMITY.SMITYcore.errorHandling import handleError


def communicateWithRunningFunctions(conn):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    ##
    ## function to print the messages received from running job.
    ## This function is not meant to be imported by another script.
    ## It is used directly from <call_function_wCommunication>
    ##
    while 1:
        msg = conn.recv()
        if type(msg) == str:
            print2gui("{}".format(msg))
        elif type(msg) == int:
            handleError(msg)
        else:
            return 1
# end of communicateWithRunningFunctions


def call_function_wCommunication(function2beCalled, *functionsArgs):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    parent_conn, child_conn = multiprocessing.Pipe()

    # if the function2beCalled doesn't sleep after sending a message, add the following code after each send :
    # from time import sleep
    # sleep(0.0000000000001)
    # so that the receiver gets its turn to receive the messages and do what he has got to do with them
    p_function = multiprocessing.Process(target=function2beCalled, args=(parent_conn, *functionsArgs))
    receiver = multiprocessing.Process(target=communicateWithRunningFunctions, args=(child_conn,))

    receiver.start()
    p_function.start()

    p_function.join()
    receiver.join()


def call_function(function2beCalled, *functionsArgs):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # if the function2beCalled doesn't sleep after sending a message, add the following code after each send :
    # from time import sleep
    # sleep(0.0000000000001)
    # so that the receiver gets its turn to receive the messages and do what he has got to do with them
    p_function = multiprocessing.Process(target=function2beCalled, args=(*functionsArgs,))

    p_function.start()
    p_function.join()

# ------------------------------
# End <For Parallel Programming>
# ------------------------------
