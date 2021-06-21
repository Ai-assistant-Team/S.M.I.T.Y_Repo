#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

from SMITY.SMITYcore.printToGUI import print2gui
from SMITY.SMITYcore.textToSpeech import Text2Speech

MESSAGES = {
    0: 'The operation was executed successfully.',
    1: 'Operation Failed. Something Went Wrong.',  # General Error
    2: 'You Do Not Have The Necessary Permissions To Do That.',
    3: 'I Could Not Find The File.',
    4: 'I Could Not Find The Application.',
    5: 'You Have To Be Connected To This Service In Order To Use It.',
    6: 'Language Not Supported Yet.',
    7: 'I Did Not Understand That.',
    8: 'Something Went Wrong While Trying To Read File.',
    9: 'Something Went Wrong While Trying To Write To File.',
    10: 'You Are Not Connected To The Internet.',
    11: 'There Is Not Enough Space In The Device.',
    12: 'No Input Device Found.',
    13: 'No Output Device Found.',
    14: 'Something Went Wrong While Trying To Open The Link You Requested.',
    15: 'Something Went Wrong With The Encryption.',
    16: 'Something Went Wrong With The Decryption.',
    17: 'The Password Given Was Invalid.',
    18: 'Operation Timed Out.',
    19: 'Initialization Failed.'
}


def handleError(code):
    if code in [10, 12, 13]:
        # errors to be communicated only by written word
        print2gui(MESSAGES[code])
    else:
        # errors to be communicated like any other answer from S.M.I.T.Y.
        Text2Speech().speak(MESSAGES[code])

    return code
