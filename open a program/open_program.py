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
        webbrowser.open_new_tab(program.location)
    # if none of te above send a message
    else:
       print("There is a problem")

#installation of programs
def create_programs():
    notepad = Program("notepad","exe",'C:\\Windows\\System32\\notepad.exe')
    calculator = Program("calculator","exe", 'C:\\Windows\\System32\\calc.exe')
    google = Program("google","web_site","https://www.google.com")

#Test  
def test():
    create_programs():
    open_program(notepad)
    open_program(calculator)
    open_program(google)

test()