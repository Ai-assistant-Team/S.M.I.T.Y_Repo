
#This function is used to restart the device
def lockScrn():
    import ctypes
    
    ctypes.windll.user32.LockWorkStation()
        
lockScrn()
    