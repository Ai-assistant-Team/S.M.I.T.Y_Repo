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
    try:
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        myScreenshot.save(file_path)
    except:
        return 1
    return 0

