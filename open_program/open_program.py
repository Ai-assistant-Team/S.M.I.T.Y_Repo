import webbrowser
import subprocess
from program import Program
import pathlib

def open_program(program_name):
    listOfPrograms =[]
    listOfwebsites =[]
    execution = 0
    execution = load(listOfPrograms,"\\program_locations.txt")
    execution = load(listOfwebsites,"\\users_urls.txt")
    if execution == 1:
        return 10
    else:
        found = 'N'
        for program in listOfPrograms:
            if program.name == program_name:
                print(program.name)
                found = 'Y'
                # if the type of the program is .exe
                try:
                    #go to the program.locatino and start the executable file t
                    subprocess.Popen(program.location)
                except:
                    #if ther is a problem send an error message
                    return 3
        
        if found == "N":
            for website in listOfwebsites:
                if website.name == program_name:
                    print(website.name)
                    found = 'Y'
                    try:
                        webbrowser.open_new_tab(website.location)
                    except:
                        return 14
                    #open the last used browewr and go to the url that is in the program.location
        if found == 'N':
            return 1


#installation of programs, adding the to the list of Programs

def load(list,txt_location):
    try:
        location = pathlib.Path(__file__).parent.absolute()
        f = open("%s%s"%(location,txt_location), "r")
        while 5>4:
            name = f.readline()
            name = name.replace('\n','')
            if not name:
                break
            program_location = f.readline()
            program_location = program_location.replace('\n','')
            list.append(Program(name,program_location))
        f.close()
        return 0
    except:
        return 1
