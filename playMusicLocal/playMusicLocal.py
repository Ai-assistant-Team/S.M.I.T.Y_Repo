# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:50:33 2021

@author: nickk
"""
def playMusicLocal(songName, songPath): #Given a name and a path plays an audio file on the system defaul player
    try:  
        import os #Required to start the audio file
        import sys #Required to stop the script if audio file is not found

    
        audioTypes = ['.mp3','.m4a','.flac','.wav','.wma','.aac'] #The audio types supported by the script
    
        for i in range(6): 
            result = find(songName+audioTypes[i], songPath) #Searches for the audio file with every one of the above extentions   
            if result != None: #if the audio file is found break the loop
                break   
        
        if (result == None)or(result == 1): #if the audio file is not found return code 2 and stop script
            return 2
            sys.exit()
        
    
        os.startfile(result) #if the audio file is found play it
        return 0
    except:
        return 1
    
def find(fileName, filePath): #Searches for the audio file in a given path and if found returns full path
    try:
        import os
        for root, dirs, files in os.walk(filePath):
            if fileName in files:
                return os.path.join(root, fileName)
    except:
        return 1
    
