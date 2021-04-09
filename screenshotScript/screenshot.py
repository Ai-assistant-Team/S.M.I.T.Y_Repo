# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:56:35 2021

@author: fotis
"""

#function that takes screenshot

def screenshot():
    
    #import the needed libraries    
    import pyautogui 
    import tkinter as tk
    from tkinter import filedialog
    
    root = tk.Tk()
    
    #taking the screenshot
    myScreenshot = pyautogui.screenshot()
    
    root.withdraw()
    
    #chooses the location to store the screenshot and the name
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)
    root.mainloop()
    
