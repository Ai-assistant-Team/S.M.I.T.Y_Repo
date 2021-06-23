# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

from SMITY.definePATH import MY_OUTPUT
# import SMITY.SMITY_GUI.gui3
# from SMITY.SMITY_GUI.gui3 import update_output_from_outside

# Add file that contains whatever is printed on the text area for GUI


# Function
def print2gui(*objects, sep=' ', end='\n', filename=MY_OUTPUT):
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    # Use the same attributes as python's print, changing only the output file.
    # Link used : https://python-reference.readthedocs.io/en/latest/docs/functions/print.html
    
    # with open(filename, 'a') as file:
        
    #     print(*objects, sep=sep, end=end, file=file)
        
    # # The following is called to update the GUI output
    # SMITY.SMITY_GUI.gui3.update_output_from_outside()
    print(*objects)
