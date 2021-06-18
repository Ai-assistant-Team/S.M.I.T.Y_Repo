#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

from SMITY.definePATH import MY_OUTPUT
from SMITY.SMITY_GUI.gui3 import get_command_update

# Add file that contains whatever is printed on the text area for GUI


# Function
def print2gui(*objects, sep=' ', end='n', file=MY_OUTPUT):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # Use the same attributes as python's print, changing only the output file.
    # Link used : https://python-reference.readthedocs.io/en/latest/docs/functions/print.html
    print(*objects, sep=sep, end=end, file=file)
    get_command_update()

