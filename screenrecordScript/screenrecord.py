# importing the required packages
import pyautogui
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def screenRecord():
  
    
        # Specify resolution
        resolution = (1920, 1080)
  
        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*'XVID')
  
        # Specify name of Output file
        root = tk.Tk() 
        root.withdraw()
        filename = filedialog.asksaveasfilename(defaultextension='.mp4')
        #if the user doesnt give a file name the record ends
        if(not filename):
                return 1
  
        # Specify frames rate. We can choose any 
        # value and experiment with it
        fps = 20.0
  
  
      # Creating a VideoWriter object
        out = cv2.VideoWriter(filename, codec, fps, resolution)
  
      # Create an Empty window
        cv2.namedWindow('Live', cv2.WINDOW_NORMAL)
  
      # Resize this window
        cv2.resizeWindow('Live', 480, 270)

    
        while True:
            # Take screenshot using PyAutoGUI
            img = pyautogui.screenshot()
  
            # Convert the screenshot to a numpy array
            frame = np.array(img)
  
            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
            # Write it to the output file
            out.write(frame)
      
            # Optional: Display the recording screen
            cv2.imshow('Live', frame)
            
    
            # Stop recording when we press 'q'
            if (cv2.waitKey(1) & 0xFF == ord('q')) or cv2.getWindowProperty('Live', cv2.WINDOW_NORMAL) == -1:
                break
                
              
        # Release the Video writer
        out.release()
  
        # Destroy all windows
        cv2.destroyAllWindows()
        
        return 0


