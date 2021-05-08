
#This function is used to lock the device
def lockScrn():
    import ctypes
    
    ctypes.windll.user32.LockWorkStation()
        
#This fnction is used to lock the device after a number of seconds speciafied by the user
def lockScrnTimer(t): 
    import time
    
    while(t>0):
        time.sleep(1)
        t = int(t)-1;
    
    lockScrn()
