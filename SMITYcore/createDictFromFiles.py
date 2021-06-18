#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

# Creates a dictionary with key = filename and value = listOfContents

import os

# Constants

SPLIT_AT = ','  # ','
DIRPATH = '.'  # 'Keywords'


def create(dirpath=DIRPATH, split_at=SPLIT_AT):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    dictionary = {}

    for file in os.listdir(dirpath):
        with open(os.path.join(dirpath, file)) as f:
            key = os.path.basename(f.name).split('.')[0]  # f.name.split('.')[0]
            values = f.read().split(split_at)
            # add to dictionary
            dictionary[key] = values

    return dictionary
