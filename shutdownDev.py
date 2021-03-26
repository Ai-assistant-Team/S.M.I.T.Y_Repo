 
#This function is used to shut down the device
def shutdownDev():
    import os
    
    os.system("shutdown /s /t 1") #This method is used to shut down the device.
                                  #/s is for shut down and /t is a timer so that the system shuts down after 1 sec.
    