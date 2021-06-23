# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

from SMITY.definePATH import MY_OUTPUT
# import SMITY.SMITY_GUI.gui3

# Add file that contains whatever is printed on the text area for GUI


# Function
def print2gui(*objects, sep=' ', end='\n', filename=MY_OUTPUT):
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    ## Due to problems with GUI, GUI is not used in this version of S.M.I.T.Y.
    ## The name of the function remains "print2gui" because in future versions
    ##   GUI will be used, and because a change that big may hurt the code.

    # TO BE USED WITH GUI ONLY
    # --------------------------
    # with open(filename, 'a') as file:
        
    #     print(*objects, sep=sep, end=end, file=file)
        
    # # The following is called to update the GUI output
    # SMITY.SMITY_GUI.gui3.update_output_from_outside()
    # --------------------------

    print(*objects)
