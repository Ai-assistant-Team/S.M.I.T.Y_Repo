"""
Created on We May 5 18:03:12 2021
@author: manolispolymeneris
"""

def testCaseOne():
    import randfacts #Imports random fun fact generator library
    
    for i in range(5142): #Runs the list with fun facts
        fact = randfacts.getFact() #Generates a fun fact
        print(fact) #Prints the fun fact
        
        request = "Yes" #Sets request to "Yes"
        
        if (request!="Yes" and request!="No"): #Checks if answer isn't "Yes" or "No"
            print("Invalid Answer") #Prints that the answer is not valid
            break
        #end of if
        if (request=="No"): #Checks if user wants another fun fact
            break
        #end of if
    #end of for
        
testCaseOne()

def testCaseTwo():
    import randfacts #Imports random fun fact generator library
    
    for i in range(5142): #Runs the list with fun facts
        fact = randfacts.getFact() #Generates a fun fact
        print(fact) #Prints the fun fact
        
        request = "No" #Sets request to "No"
        
        if (request!="Yes" and request!="No"): #Checks if answer isn't "Yes" or "No"
            print("Invalid Answer") #Prints that the answer is not valid
            break
        #end of if
        if (request=="No"): #Checks if user wants another fun fact
            break
        #end of if
    #end of for
        
testCaseTwo()
