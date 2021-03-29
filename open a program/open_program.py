import webbrowser
import subprocess
import os


from program import Program

def open_program(program):
    # if the type of the program is .exe
    if program.program_type == "exe":
        try:
            #go to the program.locatino and start the executable file t
            subprocess.Popen(program.location)
        except:
            #if ther is a problem send an error message
            print("Problem opening " + program.name)
    # if the type of the program is web_site       
    elif program.program_type == "web_site":
        #open the last used browewr and go to the url that is in the program.location
        webbrowser.open_new_tab(p.location)
    # if none of te above send a message
    else:
       print("There is a problem")

#installation of programs, adding the to the list of Programs
def create_programs(listOfPrograms):
    notepad = Program("notepad","exe",'C:\\Windows\\System32\\notepad.exe')
    listOfPrograms.append(notepad)
    calculator = Program("calculator","exe", 'C:\\Windows\\System32\\calc.exe')
    listOfPrograms.append(calculator)
    google = Program("google","web_site","https://www.google.com")
    listOfPrograms.append(google)
    facebook = Program("facebook","web_site","https://www.facebook.com")
    listOfPrograms.append(facebook)
    messenger = Program("messenger","exe", 'C:\\Users\\NektariosP\\AppData\\Local\\Programs\\Messenger\\Messenger.exe')
    listOfPrograms.append(messenger)

#Test  
def test(listOfPrograms):
    create_programs(listOfPrograms)
    answer = input("What do you want to open?")
    found = False
    for x in listOfPrograms:
        if x.name == answer:
            found = True
            open_program(x)
    if found == False:
        print("Program Not found")



listOfPrograms = []
test(listOfPrograms)
