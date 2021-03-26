
#This function is used to lock the device
def lockScrn():
    import ctypes
    
    ctypes.windll.user32.LockWorkStation()
        
lockScrn()
    
