"""
Created on We May 5 18:07:19 2021
@author: manolispolymeneris
"""

def testCaseOne():
    import pyjokes #Imports random joke generator library
    
    for i in range(9, 105): #Runs the list with jokes
        joke = pyjokes.get_joke() #Generates a joke
        print(joke) #Prints the joke
        
        request = "Yes" #Sets request to "Yes"
        
        if (request!="Yes" and request!="No"): #Checks if answer isn't "Yes" or "No"
            print("Invalid Answer") #Prints that the answer is not valid
            break
        #end of if
        if (request=="No"): #Checks if user wants another joke
            break
        #end of if
    #end of for
        
testCaseOne()

def testCaseTwo():
    import pyjokes #Imports random joke generator library
    
    for i in range(9, 105): #Runs the list with jokes
        joke = pyjokes.get_joke() #Generates a joke
        print(joke) #Prints the joke
        
        request = "No" #Sets request to "No"
        
        if (request!="Yes" and request!="No"): #Checks if answer isn't "Yes" or "No"
            print("Invalid Answer") #Prints that the answer is not valid
            break
        #end of if
        if (request=="No"): #Checks if user wants another joke
            break
        #end of if
    #end of for
        
testCaseTwo()
