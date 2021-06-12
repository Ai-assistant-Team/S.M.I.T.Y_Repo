# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 06:56:49 2021

@author: Θόδωρος
"""

from googleMapsDirections import googleMapsDirections


def test():
    #made by Οικονομίδης Θεόδωρος
    import time                      # to use sleep() function
    
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
    time.sleep(1)
    print(testCase7())
    time.sleep(1)
    print(testCase8())
    time.sleep(1)
    print(testCase9())
    

def testCase1():
    #made by Οικονομίδης Θεόδωρος
    
    # Should open empty google maps directions page
    # Tests the case that no parameters are passed
    return googleMapsDirections()
    
#end of testCase1

def testCase2():
    #made by Οικονομίδης Θεόδωρος
    
    # Should open google maps directions page with <origin> filled
    # Tests the case that only one parameter is given a value
    return googleMapsDirections('New York')
    
#end of testCase2

def testCase3():
    #made by Οικονομίδης Θεόδωρος
    
    # Should open google maps directions page with <origin> and <destination> filled
    # Tests the case that two parameters are given a value
    return googleMapsDirections('New York', 'Miami')
    
#end of testCase3

def testCase4():
    #made by Οικονομίδης Θεόδωρος
    
    # Should open google maps directions page with <origin>, <destination> and <travelmode> filled
    # Test the case that three parameters are given a value. 
    # Also tests the value 'walking' of the thirds parameter (one of the 5 currently available)
    return googleMapsDirections('New York', 'Miami', 'walking')
        
#end of testCase4

def testCase5():
    #made by Οικονομίδης Θεόδωρος
  
    # Should fill <origin> with current location (since an empty string is passed)
    # Tests the value 'driving' of the thirds parameter (one of the 5 currently available)
    return googleMapsDirections('', '8ball club, Thessaloniki', 'driving')
    
#end of testCase5

def testCase6():
    #made by Οικονομίδης Θεόδωρος
  
    # Tests the value 'bicycling' of the thirds parameter (one of the 5 currently available)
    return googleMapsDirections('DaVinci, Athens', 'Hard Rock Cafe, Athens', 'bicycling')
    
#end of testCase6

def testCase7():
    #made by Οικονομίδης Θεόδωρος
  
    # Tests the value 'bicycling' of the thirds parameter (one of the 5 currently available)
    return googleMapsDirections('DierenPark Amersfoort, Barchman Wuytierslaan 224, 3819 AC Amersfoort', 'Κρατικό Μουσείο της Ολλανδίας, Museumstraat 1, 1071 XX Amsterdam', 'bicycling')
    
#end of testCase7

def testCase8():
    #made by Οικονομίδης Θεόδωρος
  
    # Tests the value 'transit' of the thirds parameter (one of the 5 currently available)
    return googleMapsDirections('8ball club, Thessaloniki', 'Pagoseto, Thessaloniki', 'transit')
    
#end of testCase8

def testCase9():
    #made by Οικονομίδης Θεόδωρος
    
    # Should have the exact same result as testCase1
    # Tests the case where empty strings are given as values to all parameters
    return googleMapsDirections('', '', '')
    
#end of testCase9


## Execution

test()