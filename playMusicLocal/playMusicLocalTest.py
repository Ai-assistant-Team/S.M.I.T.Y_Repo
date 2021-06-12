# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:28:45 2021

@author: nickk
"""
def test():
    from playMusicLocal import playMusicLocal
    import os #Required to see the contents of a txt file
    import sys #Required to stop the script
    
    sName = input("Insert song name: ")
    
    pathfileW = open("pathfile.txt", "a+")
    
    if(os.stat("pathfile.txt").st_size == 0): #if txt is empty prompt the user to select a search location
        import tkinter as tk
        from tkinter.filedialog import askdirectory
        window = tk.Tk()
        path = askdirectory(title='Select Music Folder') 
        window.withdraw()
        pathfileW.write(path)
    else: #else read the location from the txt 
        pathfileR = open("pathfile.txt", "r")
        path = pathfileR.readline()
        print(path)
        pathfileR.close()
        
    
    pathfileW.close()
    playMusicLocal(sName, path) #Play the audio file with the given name in thee given location
    sys.exit()
test()