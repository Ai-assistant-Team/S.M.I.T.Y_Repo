
#This function is used to restart the device
def restartDev():
    import os 
    
    os.system("shutdown /r /t 1")#This method is used to shut down the device.
                                  #/r is for restart and /t is a timer so that the system shuts down after 1 sec.
        
restartDev()