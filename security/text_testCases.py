# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 07:36:49 2021

@author: Θόδωρος
"""

from text import textSecurity

from programStateCodes import MESSAGES

def test():
    testCase1()
    print('\n-----\n')
    testCase2()
    print('\n-----\n')
    testCase3()
    print('\n-----\n')
    testCase4()
    print('\n-----\n')
    testCase5()                                                             # throws error because of the conversion to binary in produceFernet 
    print('\n-----\n')
    testCase6()                                                             # throws error because an integer doesn't have the attribute 'encode', used in encryption

#end of test


def testCase1():
    res = textSecurity().encrypt('secret', 'pass')
    
    if type(res) == int :
        
        print(MESSAGES[res])
        
    else :
        
        print('Encryption Result 1 : ', res)
    
        print('\nOriginal : ', textSecurity().decrypt(res, 'pass'))
    
#end of testCase1

def testCase2():
    res = textSecurity().encrypt('secret', 'pass')
    
    if type(res) == int :
        
        print(MESSAGES[res])
        
    else :
        print('Encryption Result 2 : ', res)
        
        print('\nOriginal : ', textSecurity().decrypt(res, 'wrongPass'))
    
#end of testCase2

def testCase3():
    res = textSecurity().encrypt('secret', '')
    
    if type(res) == int :
        
        print(MESSAGES[res])
        
    else :
        print('Encryption Result 3 : ', res)
        
        print('\nOriginal : ', textSecurity().decrypt(res, ''))
    
#end of testCase3

def testCase4():
    res = textSecurity().encrypt('', 'pass')
    
    if type(res) == int :
        
        print(MESSAGES[res])
        
    else :
        print('Encryption Result 4 : ', res)
        
        print('\nOriginal : ', textSecurity().decrypt(res, 'pass'))
    
#end of testCase4


def testCase5():
   
    # not a possibility, since the main program will pass the correct type of data (and every script is only called by the main program)
    # should return an ERROR due to the fact that the function uses attribute 'to_bytes' and 'str' object doesn't have one.
    res = textSecurity().encrypt('', 1)
   
    if type(res) == int :
        
        print(MESSAGES[res])
        
    else :
        print('Encryption Result 5 : ', res)
        
        print('\nOriginal : ', textSecurity().decrypt(res, 1))
    
#end of testCase5


def testCase6():
    
    # not a possibility, since the main program will pass the correct type of data (and every script is only called by the main program)
    # should return an ERROR due to the fact that the function uses attribute 'encode' and 'int' object doesn't have one. 
    res = textSecurity().encrypt(1, '')
   
    if type(res) == int :
        
        print(MESSAGES[res])
        
    else :
        print('Encryption Result 6 : ', res)
        
        print('\nOriginal : ', textSecurity().decrypt(res, ''))
    
#end of testCase6

# Execution

test()
