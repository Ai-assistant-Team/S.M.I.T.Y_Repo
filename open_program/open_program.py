import subprocess
from SMITY.open_program.program import Program
import pathlib
from SMITY.urlHandling.openUrls import openUrl
from SMITY.definePATH import RESOURCES_PATH
import os


def open_program(program_name):
    listOfPrograms = []
    listOfwebsites = []

    location = RESOURCES_PATH + '\\Settings\\program_locations.txt'
    execution = load(listOfPrograms, location)
    if execution == 1:
        return 1
    location = RESOURCES_PATH + '\\Settings\\users_urls.txt'
    execution = load(listOfwebsites, location)
    if execution == 1:
        return 1
    else:
        found = 'N'
        for program in listOfPrograms:
            if program.name == program_name:
                found = 'Y'
                if program.location == 'NOT FOUND':
                    return 3
                try:
                    # go to the program.locatino and start the executable file t
                    subprocess.Popen(program.location)
                except:
                    # if ther is a problem send an error message
                    return 3

        if found == "N":
            for website in listOfwebsites:
                if website.name == program_name:
                    found = 'Y'
                    b = openUrl(website.location)
                    if b == 14:
                        return 14
                    # open the last used browewr and go to the url that is in the program.location
        if found == 'N':
            return 1
        if found == 'Y':
            return 0


# installation of programs, adding the to the list of Programs

def load(list, txt_location):
    try:
        location = RESOURCES_PATH + '\\Settings\\program_locations.txt'
        f = open(location, "r")
        while 5 > 4:
            name = f.readline()
            name = name.replace('\n', '')
            if not name:
                break
            program_location = f.readline()
            program_location = program_location.replace('\n', '')
            list.append(Program(name, program_location))
        f.close()
        return 0
    except:
        return 1
