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
        return 0
    except:
        return 1
    
  
  
  def testCaseOne()
      screenshot()
    
    testCaseOne()
