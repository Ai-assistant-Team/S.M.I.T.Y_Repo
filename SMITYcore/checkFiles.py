#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

from SMITY.definePATH import PATH_TO_SETTINGS, PATH_TO_GUI
from searchExeProgram import lookFor
import os


def initializeFiles():
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    settingsFile = os.path.join(PATH_TO_SETTINGS, 'settings.txt')
    websitesFile = os.path.join(PATH_TO_SETTINGS, 'users_urls.txt')
    programsFile = os.path.join(PATH_TO_SETTINGS, 'program_locations.txt')
    userProgramsFile = os.path.join(PATH_TO_SETTINGS, 'users_programs.txt')
    locationsFile = os.path.join(PATH_TO_GUI, 'Calendar', 'locations_of_today.txt')

    try:
        if not (os.path.isfile(settingsFile)):
            if createSettingsFile(settingsFile) != 0:
                raise Exception

        if not (os.path.isfile(websitesFile)):
            if createLinks2Sites(websitesFile) != 0:
                raise Exception

        if not (os.path.isfile(userProgramsFile)):
            if createLinks2usersPrograms(userProgramsFile) != 0:
                raise Exception

        if not (os.path.isfile(programsFile)):
            if createLinks2Programs(programsFile) != 0:
                raise Exception

        if not (os.path.isfile(locationsFile)):
            if createLocationsOfToday(locationsFile) != 0:
                raise Exception

        return 0
    except FileNotFoundError as e:
        return 3
    except Exception:
        return 19

# end of initializeFiles


def createSettingsFile(settingsFile):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    try:
        with open(settingsFile, 'w') as file:
            file.write('S.M.I.T.Y.Gender : female\n')
            file.write('Username : User\n')
            file.write('Voice control : 1\n')
            file.write('Speak key : 1\n')
            file.write('Voice wake up : 1\n')
            file.write('Spotify username : Spotify_Username\n')
            file.write('Music path : ' + os.path.expanduser('~\\Music') + '\n')
        return 0
    except FileNotFoundError as e:
        return 3
    except:
        return 9

# end of createSettingsFile


def createLinks2usersPrograms(userProgramsFile):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    try:
        with open(userProgramsFile, 'w') as file:
            for i in range(10):
                file.write('ADD PROGRAM\n')
                file.write('LOCATION\n')
        return 0
    except FileNotFoundError as e:
        return 3
    except:
        return 9
# end of createLinks2usersPrograms


def createLinks2Sites(websitesFile):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    try:
        with open(websitesFile, 'w') as file:
            for i in range(10):
                file.write('ADD WEBSITE\n')
                file.write('ADD URl\n')
        return 0
    except FileNotFoundError as e:
        return 3
    except:
        return 9
# end of createLinks2Sites


def createLinks2Programs(programsFile):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # Dictionary in which
    #   Key -> Name of executable
    #   Value -> Name that the user sees
    dictOfPrograms = {
        'EXCEL.exe': 'Excel',
        'WINWORD.exe': 'Word',
        'MSACCESS.exe': 'Access',
        'POWERPNT.exe': 'Power Point',
        'Spotify.exe': 'Spotify',
        'Messenger.exe': 'Messenger',
        'calc.exe': 'Calculator',
        'notepad.exe': 'Notepad'
    }
    resultsDict = {}     # here the results (names and links) are going to be stored
    try:
        for exe, name in dictOfPrograms.items():
            result = lookFor(exe)
            if type(result) is int:
                # if type(result) is int, it means that either the program was not found, or there was an error.
                # Either way, the value in the results dictionary for that element is 'NOT FOUND'
                resultsDict[name] = 'NOT FOUND'
            elif type(result) is str:
                resultsDict[name] = result
    except UnicodeDecodeError:
        counter = len(resultsDict)
        for exe, name in dictOfPrograms.items():
            if counter > 0:
                counter -= 1
                continue
            resultsDict[name] = 'NOT FOUND'


    try:
        with open(programsFile, 'w') as file:
            for name, link in resultsDict.items():
                file.write(name + '\n')
                file.write(link + '\n')

        return 0
    except FileNotFoundError as e:
        return 3
    except:
        return 9
# end of createLinks2Programs


def createLocationsOfToday(locationsFile):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    try:
        with open(locationsFile, 'w') as file:
            file.write('relx = 0.0435, rely = 0.104     relx = 0.1735, rely = 0.104    relx = 0.304, rely = 0.104   relx = 0.434, rely = 0.104   relx = 0.5645, rely = 0.104   relx = 0.695, rely = 0.104   relx = 0.8246, rely = 0.104\n')
            file.write('relx = 0.0435, rely = 0.255     relx = 0.1735, rely = 0.255    relx = 0.304, rely = 0.255   relx = 0.434, rely = 0.255   relx = 0.5645, rely = 0.255   relx = 0.695, rely = 0.255   relx = 0.8246, rely = 0.255\n')
            file.write('relx = 0.0435, rely = 0.4065     relx = 0.1735, rely = 0.4065    relx = 0.304, rely = 0.4065   relx = 0.434, rely = 0.4065   relx = 0.5645, rely = 0.4065   relx = 0.695, rely = 0.4065   relx = 0.8246, rely = 0.4065\n')
            file.write('relx = 0.0435, rely = 0.557     relx = 0.1735, rely = 0.557    relx = 0.304, rely = 0.557   relx = 0.434, rely = 0.557   relx = 0.5645, rely = 0.557   relx = 0.695, rely = 0.557   relx = 0.8246, rely = 0.557\n')
            file.write('relx = 0.0435, rely = 0.7094     relx = 0.1735, rely = 0.7094    relx = 0.304, rely = 0.7094   relx = 0.434, rely = 0.7094   relx = 0.5645, rely = 0.7094   relx = 0.695, rely = 0.7094   relx = 0.8246, rely = 0.7094\n')
            file.write('relx = 0.0435, rely = 0.8599     relx = 0.1735, rely = 0.8599    relx = 0.304, rely = 0.8599   relx = 0.434, rely = 0.8599   relx = 0.5645, rely = 0.8599   relx = 0.695, rely = 0.8599   relx = 0.8246, rely = 0.8599')
    except FileNotFoundError as e:
        return 3
    except:
        return 9
# end of createLocationsOfToday

