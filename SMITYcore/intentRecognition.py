#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#


import createDictFromFiles


KEYWORDS_DICT = createDictFromFiles.create('Keywords', ',')


def most_common_element(lst):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
    return max(set(lst), key=lst.count)
# end of most_common_element


def intentRecognition(userInput, keywordsDict=KEYWORDS_DICT):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    try:
        print(KEYWORDS_DICT)
        # if userInput is a keyword by itself, then return the key that matches that keyword
        for key, value in keywordsDict.items():
            if userInput in value:
                return key

        # searches for each word individually, adds the key/keys that match that keyword
        # on a list and then returns the key that appears the most in that list
        userWordsList = userInput.split()
        keywordsFound = []
        for key, value in keywordsDict.items():
            for word in userWordsList:
                if word in value:
                    keywordsFound.append(key)

            for keyword in value:
                if keyword in userInput:
                    keywordsFound.append(key)

        print(keywordsFound)
        return most_common_element(keywordsFound)

    except ValueError as e:
        return 7
# end of intentRecognition


def writtenCommandFromGUI(command):
    intentRecognition(command)
# end of writtenCommandFromGUI
