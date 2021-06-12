# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:41:35 2021

@author: Θόδωρος
"""

from openUrls import openUrl
from programStateCodes import MESSAGES

def test():
    import time              # to use the sleep function
    
    testCase1()
    time.sleep(1)
    testCase2()
    time.sleep(1)
    testCase3()
    time.sleep(1)
    testCase4()
    time.sleep(1)
    testCase5()
    time.sleep(1)
    testCase6()
    
    
def testCase1():
    print('Test Case 1 : \n')
    check = openUrl()  
    print(MESSAGES[check])
#end of testCase1

def testCase2():
    print('Test Case 2 : \n')
    check = openUrl('')
    print(MESSAGES[check])
#end of testCase2

def testCase3():
    print('Test Case 3 : \n')
    check = openUrl('www.uom.gr')
    print(MESSAGES[check])
#end of testCase3

def testCase4():
    print('Test Case 4 : \n')
    check = openUrl('google.com')
    print(MESSAGES[check])
#end of testCase4

def testCase5():
    print('Test Case 5 : \n')
    check = openUrl('testsearch')
    print(MESSAGES[check])
#end of testCase5

def testCase6():
    print('Test Case 6 : \n')
    check = openUrl('test search')
    print(MESSAGES[check])
#end of testCase6

test()
