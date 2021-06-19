# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:51:09 2021

@author: nickk
"""

def test():
    from playVideoLocal import playVideoLocal
    import os #Required to see the contents of a txt file
    import sys #Required to stop the script
    
    vname = input('Insert video name: ')
    filename = 'pathfilev.txt'
    pathfilew = open(filename, 'a+')
    
    if(os.stat(filename).st_size == 0): #if txt is empty prompt the user to select a search location
        import tkinter as tk
        from tkinter.filedialog import askdirectory
        window = tk.Tk()
        path = askdirectory(title='Select Video Folder')
        window.withdraw()
        pathfilew.write(path)
    else: #else read the location from the txt
        pathfiler = open(filename, 'r')
        path = pathfiler.readline()
        print(path)
        pathfiler.close()
        
    
    pathfilew.close()
    playVideoLocal(vname, path) #Play the audio file with the given name in thee given location
    sys.exit()
    
test()