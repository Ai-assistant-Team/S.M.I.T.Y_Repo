# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

# Creates a dictionary with key = filename and value = listOfContents

import os
from SMITY.definePATH import PATH_TO_KEYWORDS


# Constants

SPLIT_AT = ','  # ','
DIRPATH = PATH_TO_KEYWORDS


def create(dirpath=DIRPATH, split_at=SPLIT_AT):
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    dictionary = {}

    for file in os.listdir(dirpath):
        with open(os.path.join(dirpath, file), encoding='utf8') as f:
            key = os.path.basename(f.name).split('.')[0]  # f.name.split('.')[0]
            values = f.read().split(split_at)
            # add to dictionary
            dictionary[key] = values

    return dictionary
