# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 06:11:56 2021

@author: Θόδωρος
"""

from googleMapsSearch import googleMapsSearch

def test():
    #made by Οικονομίδης Θεόδωρος
    
    import time                      # to use sleep() function
    
    # print is used to view the returned state codes (all should be == 0, if everything works)
    
    print(testCase1())
    time.sleep(1)
    print(testCase2())
    time.sleep(1)
    print(testCase3())
    time.sleep(1)
    print(testCase4())
    time.sleep(1)
    print(testCase5())
    time.sleep(1)
    print(testCase6())
    
    
#end of test
    

def testCase1():
    #made by Οικονομίδης Θεόδωρος

    return googleMapsSearch()                                          # when used without parameters, it should open google maps empty search 
    
#end of testCase1  

def testCase2():
    #made by Οικονομίδης Θεόδωρος

    return googleMapsSearch('')                                        # should have the exact same result as testCase1
    
#end of testCase2

def testCase3():
    #made by Οικονομίδης Θεόδωρος

    return googleMapsSearch('8ball Club, Thessaloniki')
    
#end of testCase3

def testCase4():
    #made by Οικονομίδης Θεόδωρος

    return googleMapsSearch('Πανεπιστήμιο Μακεδονίας')
    
#end of testCase4

def testCase5():
    #made by Οικονομίδης Θεόδωρος

    return googleMapsSearch('546 36')
    
#end of testCase5

def testCase6():
    #made by Οικονομίδης Θεόδωρος

    return googleMapsSearch('40.625183883140934, 22.960135320666556')  # longitude and latitude
    
#end of testCase6


test()