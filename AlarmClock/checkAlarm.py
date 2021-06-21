"""
Created on Fri Jun 18
@author: Τάσος Παπαδόπουλος
"""
import datetime
import os
import time
from SMITY.definePATH import PATH_TO_ALARM_CLOCK
file = 'hours.txt'

def checkTime():
    try:
        while True: #running forever
            
            if os.path.exists(os.path.join(PATH_TO_ALARM_CLOCK, file)) : #checks if the file hours.txt exists
                
                if os.stat(os.path.join(PATH_TO_ALARM_CLOCK, file)).st_size > 0 : #checks  if the file hours.txt is empty
                    
                    with open(os.path.join(PATH_TO_ALARM_CLOCK, file), 'r') as f: #if it exists it opens the file

                        a = [a.strip() for a in f]  #formats the content of the txt file to a list of integers that represent the time

                    s = [] #new list

                    for x in a:
                        s.append(int(x) - datetime.datetime.now().hour) #puts each element of list 'a' to list 's' where every element is the result of its self minus the current time

                    minv = 24

                    for x in s:

                        if int(x) < minv and int(x) >= 0: #finds the element that is the lowest and not negative
                            minv = int(x)

                    p = []
                    
                    j = 0
                    
                    k = 0
                    
                    for x in s:

                        if int(x) != 0:
                            p.append(x) #puts all elements into a new list excluding elements that are equal to zero
                            
                            k += 1
                            
                        else:
                            j += 1

                    y = 0

                    for x in p:
                        
                        p[y] = int(x) + datetime.datetime.now().hour #converts each element back to its original state by additive its self and current time
                        
                        y += 1

                    
                    b = 0
                    
                    if (minv == 0): #if there was an element equal to 0 and so is min it means that the ring has to go off
                        
                        wakeup='WAKE UP!'
                        
                        
                        with open(os.path.join(PATH_TO_ALARM_CLOCK,file), 'w') as txt_file: #saving every element from list p to the hours.txt file
                            
                            for line in p:
                                
                                if b == 0:

                                    txt_file.write(str(line))

                                else:

                                    txt_file.write('\n' + ''.join(str(line)))
                                    
                                b += 1
                                
                                if b == (k - j): #the size of the list minus the number of all the elements that where 0
                                    
                                    txt_file.close()
                                    
                                    f.close()
                                    
                                    return wakeup
                                
                                    break

                        txt_file.close()
                        
                    f.close()
                    
                    time.sleep(2)
                else:

                    time.sleep(10) #checks if the file is empty
            else:

                time.sleep(10) #checks if the file exists
            #end of while

    except OSError :
        return 8 #It could not open and read the file


checkTime()
