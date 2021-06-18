#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

# Sources : https://www.programiz.com/python-programming/user-defined-exception

## This script runs at the very beginning of the program, and initializes some

from SMITY.News.ClearTheTxtOfLinks import create_txt_with_links, clear_the_txt_of_links
from SMITY.definePATH import RESOURCES_PATH
from createPATH import create
from errorHandling import handleError, MESSAGES
from checkFiles import initializeFiles


class ResourcesPathCouldNotBeCreated(Exception):
    pass


class FilesCouldNotInitialize(Exception):
    pass


def init():
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # creating file PATH
    try:
        # crucial for the app to function. If this fails, the program should not be able to start.
        create()
    except:
        raise ResourcesPathCouldNotBeCreated('The File Structure Needed Could Not Be Created.')

    # creating the needed files (if they do not exist)
    try:
        # crucial for the app to function. If this fails, the program should not be able to start.
        initializeFiles()
    except:
        raise FilesCouldNotInitialize('The Files Needed In Order For The App To Run Properly Could Not Be Initialized')

    # initializing News Script
    if create_txt_with_links() == 0:
        clear_the_txt_of_links()


init()
