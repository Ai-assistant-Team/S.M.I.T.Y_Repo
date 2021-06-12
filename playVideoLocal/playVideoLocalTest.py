# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:51:09 2021

@author: nickk
"""

def test():
    from playVideoLocal import playVideoLocal
    import os #Required to see the contents of a txt file
    import sys #Required to stop the script
    
    vName = input("Insert video name: ")
    
    pathfileW = open("pathfileV.txt", "a+")
    
    if(os.stat("pathfileV.txt").st_size == 0): #if txt is empty prompt the user to select a search location
        import tkinter as tk
        from tkinter.filedialog import askdirectory
        window = tk.Tk()
        path = askdirectory(title='Select Video Folder')
        window.withdraw()
        pathfileW.write(path)
    else: #else read the location from the txt
        pathfileR = open("pathfileV.txt", "r")
        path = pathfileR.readline()
        print(path)
        pathfileR.close()
        
    
    pathfileW.close()
    playVideoLocal(vName, path) #Play the audio file with the given name in thee given location
    sys.exit()
    
test()