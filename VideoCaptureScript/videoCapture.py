from ecapture import ecapture as ec

def videocap() :
    
    try:
        ec.vidcapture(0,'Video','Demo.avi','q')
    
    except IOError:
        return 12
    except:
        return 1
   
#The vidcapture function takes four arguments:

#Camera index(first connected webcam will be of index 0. The next webcam will be of index 1)

#Window name (It can be a variable or a string)

#Save name (It can be a variable or a string. If you don't wish to save the video, type False)

#Exit key (The key you press to stop recording the video. It can be ("q", "x", "a" or any other letter))


