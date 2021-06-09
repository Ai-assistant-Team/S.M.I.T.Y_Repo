# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:04:17 2021

@author: Θόδωρος
"""

from file import fileSecurity

from programStateCodes import MESSAGES

from time import sleep                                                 # to use the sleep() function

testFilesDirectory = 'testFiles'
filename = testFilesDirectory + '/' + 'testFile.anything'

def test():    
    
    print('\n-----\n')
    print('Test Case 1 : \n')
    testCase1()
    print('\n-----\n')
    print('Test Case 2 : \n')
    testCase2()
    print('\n-----\n')
    print('Test Case 3 : \n')
    testCase3()
    print('\n-----\n')

    
#end of test

def testCase1():
    
    makeTestFile()
    
    sleep(1.0)
    
    check = fileSecurity().encrypt(filename, 'password')
    
    if check == 0:
        
        print('\nencrypted!')
        print('\nText inside file : \n', readFromFile(filename))
        
        sleep(1.0)
        
        check = fileSecurity().decrypt(filename, 'wrongpassword')
        
        if check == 0:
            print('\ndecrypted!')
            print('\nText inside file : \n', readFromFile(filename))
        
        else:
            print('\n', MESSAGES[check])
        
    else :
        print('\n', MESSAGES[check])

#end of testCase1


def testCase2():
    
    makeTestFile()
    
    sleep(1.0)
    
    check = fileSecurity().encrypt(filename, 'password')
    
    if check == 0:
        
        print('\nencrypted!')
        print('\nText inside file : \n', readFromFile(filename))
        sleep(1.0)
        
        check = fileSecurity().decrypt(filename, 'password')
        
        if check == 0:
            print('\ndecrypted!')
            print('\nText inside file : \n', readFromFile(filename))
            
        else:
            print('\n', MESSAGES[check])
        
    else :
        print('\n', MESSAGES[check])

#end of testCase2


def testCase3():
    
    makeTestFile()
    
    sleep(1.0)
    
    check = fileSecurity().encrypt('fileThatDoesntExist', 'password')
    
    if check == 0:
        
        print('\nencrypted!')
        print('\nText inside file : \n', readFromFile(filename))
        sleep(1.0)
        
        check = fileSecurity().decrypt('fileThatDoesntExist', 'password')
        
        if check == 0:
            print('\ndecrypted!')
            print('\nText inside file : \n', readFromFile(filename))
            
        else:
            print('\n', MESSAGES[check])
        
    else :
        print('\n', MESSAGES[check])

#end of testCase3


def makeTestFile():
    from os import mkdir
    try: 
        mkdir(testFilesDirectory)
    except:
        # The only possible exception is 'FileExistsError'. In this case, nothing needs to be done
        pass
    
    with open(filename, 'w') as file:
        file.write('This is a test text.')
        
    # uncomment the following if you want to confirm that the file is written successfully
    #print('file ready!')
    
#end of makeTestFile
        

def readFromFile(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    return text

#end of readFromFile

# Execution

test()
