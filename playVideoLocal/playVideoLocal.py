# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:58:13 2021

@author: nickk
"""

def playVideoLocal(videoName, videoPath): #Given a name and a path plays a video file on the system defaul player
    try:
        import os #Required to start the video file
        import sys #Required to stop the script if video file is not found

    
        videoTypes = [".m4v",".mp4",".mov",".asf",".avi",".wmv",".m2ts",".3g2",".3gp2",".3gpp"] #The video types supported by the script
    
        for i in range(6):
            result = find(videoName+videoTypes[i], videoPath) #Searches for the video file with every one of the above extentions
            if result != None: #if the video file is found break the loop
                break
        
        if result == None: #if the video file is not found return code 2 and stop script
            return 2
            sys.exit()
        
    
        os.startfile(result) #if the video file is found play it
        return 0
    except:
        return 1
    
def find(fileName, filePath): #Searches for the video file in a given path and if found returns full path
    import os
    for root, dirs, files in os.walk(filePath):
        if fileName in files:
            return os.path.join(root, fileName)
    