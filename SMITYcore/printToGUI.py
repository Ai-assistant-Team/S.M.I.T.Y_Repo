#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

from SMITY.definePATH import MY_OUTPUT
# from SMITY.SMITY_GUI.gui3 import get_command_update         # despite the error, it should work. When the GUI runs, it will create a global variable, that references <get_command_update>
import SMITY.SMITY_GUI.gui3

# Add file that contains whatever is printed on the text area for GUI


# Function
def print2gui(*objects, sep=' ', end='n', filename=MY_OUTPUT):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # Use the same attributes as python's print, changing only the output file.
    # Link used : https://python-reference.readthedocs.io/en/latest/docs/functions/print.html
    with open(filename, 'a') as file:
        print(*objects, sep=sep, end=end, file=file)
    # The following is called to update the GUI output
    # get_command_update()                                  TODO delete this (no need for it anymore)
    SMITY.SMITY_GUI.gui3.main().get_command_update()
