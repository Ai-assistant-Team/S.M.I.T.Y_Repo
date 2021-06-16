# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:25:09 2021

@author: nickk
"""

import playVideoLocal

def testCase1():
  playVideoLocal("Smells like teen spirit", "C://users/exaple/videos") #Correct example

def testCase2():
  try:
    playVideoLocal("C://users/exaple/video") #Only path
  except:
    print("Error")
    
def testCase3():
  try:
    playVideoLocal("Smells like teen spirit") #Only Name
  except:
    print("Error")
    
 def testCase4():
  try:
    playVideoLocal() #No input
  except:
    print("Error")
