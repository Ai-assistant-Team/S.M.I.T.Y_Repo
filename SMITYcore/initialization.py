# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

# Sources : https://www.programiz.com/python-programming/user-defined-exception

## This script runs at the very beginning of the program, and initializes some

from SMITY.News.ClearTheTxtOfLinks import create_txt_with_links, clear_the_txt_of_links
from SMITY.SMITYcore.createPATH import create
from SMITY.SMITYcore.checkFiles import initializeFiles


class ResourcesPathCouldNotBeCreated(Exception):
    pass


class FilesCouldNotInitialize(Exception):
    pass


class News_Not_Initialized_Correctly(Exception):
    pass


def init():
    ## ------------------------------------------------------
    ## created by Theodore Economides
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
    try:
        if create_txt_with_links() == 0:
            if clear_the_txt_of_links() != 0:
                raise News_Not_Initialized_Correctly
        else:
            raise News_Not_Initialized_Correctly

    except News_Not_Initialized_Correctly:
        # Not a fatal error. If this happens, it means the "news functions" will not work.
        pass
