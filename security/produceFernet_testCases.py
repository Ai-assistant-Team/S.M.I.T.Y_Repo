# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 06:54:36 2021

@author: Θόδωρος
"""

from produceFernet import produceFernet

def test():
    
    import time   # to use the sleep function
    
    print('1 : ')
    testCase1()
    time.sleep(1)
    
    print('2 : ')
    testCase2()
    time.sleep(1)
    
    print('3 : ')
    testCase3()
    time.sleep(1)
    
    print('4 : ')
    testCase4()
    time.sleep(1)
    
    print('5 : ')
    testCase5()
    time.sleep(1)
    
    print('6 : ')
    testCase6()
    time.sleep(1)
    
    print('7 : ')
    testCase7()
    time.sleep(1)
    
    print('8 : ')
    testCase8()
    time.sleep(1)
    
    print('9 : ')
    testCase9()
    time.sleep(1)
    
    print('10 : ')
    testCase10()
    time.sleep(1)
    
    print('11 : ')
    testCase11()
    time.sleep(1)
    
    print('12 : ')
    testCase12()

#end of test


def testCase1():
    
    try:
        aKey = 'password'
        prime5dig = 86729
        f = produceFernet(aKey, prime5dig)
        
        if f is not None :
            print('pass!\n')
    
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
        
#end of testCase1

def testCase2():
    
    try:
        aKey = ''
        prime5dig = 84673
        f = produceFernet(aKey, prime5dig)
        
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
        
#end of testCase2

def testCase3():
   
    try:
        aKey = 'PASSWORD'
        prime5dig = 56543
        f = produceFernet(aKey, prime5dig)
    
    
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase3

def testCase4():
    
    try:
        aKey = 'PASSWORDpassword'
        prime5dig = 57641
        f = produceFernet(aKey, prime5dig)
        
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase5

def testCase5():
    
    try:
        aKey = 'PASSWORDpassword123'
        prime5dig = 88463
        f = produceFernet(aKey, prime5dig)
    
    
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase5

def testCase6():
    
    try:
        aKey = 'PASSWORDpassword123!@#$%^&*'
        prime5dig = 98129
        f = produceFernet(aKey, prime5dig)
        
        
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase6

def testCase7():
    
    try:
        aKey = 'PASSWORDpassword123!@#$%^&*()_-'
        prime5dig = 27943
        f = produceFernet(aKey, prime5dig)
        
        
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase7

def testCase8():
    
    try:
        aKey = 'PASSWORDpassword123!@#$%^&*'
        prime5dig = 0
        f = produceFernet(aKey, prime5dig)
    
    
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase8

def testCase9():
    
    try:
        aKey = 'PASSWORDpassword123!@#$%^&*'
        prime5dig = 13
        f = produceFernet(aKey, prime5dig)
    
    
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase9

def testCase10():
    
    try:
        aKey = 'PASSWORDpassword123!@#$%^&*'
        prime5dig = 21957700000
        f = produceFernet(aKey, prime5dig)
    
    
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase10

def testCase11():
    # not a possibility, since the main program will pass the correct type of data (and every script is only called by the main program)
    # should fail due to the fact that the function uses attribute 'to_bytes' and 'str' object doesn't have one.
    try:
        aKey = 'PASSWORDpassword123!@#$%^&*'
        prime5dig = '21957700000'
        f = produceFernet(aKey, prime5dig)
    
    
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase11

def testCase12():
    # not a possibility, since the main program will pass the correct type of data (and every script is only called by the main program)
    # should fail due to the fact that the function uses attribute 'encode' and 'int' object doesn't have one.
    try:
        aKey = 16634
        prime5dig = 79159
        f = produceFernet(aKey, prime5dig)
    
    
        if f is not None :
            print('pass!\n')
            
            
    except Exception as e:
        print('fail!\n')
        print(e)
        print('\n')
    
#end of testCase12


# Execution 

test()
