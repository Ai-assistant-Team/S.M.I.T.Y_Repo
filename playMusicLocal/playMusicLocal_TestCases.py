# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:31:40 2021

@author: nickk
"""

import playMusicLocal

def testCase1():
  playMusicLocal("T.N.T", "C://users/exaple/music") #Correct example
  
def testCase2():
  try:
    playMusicLocal("C://users/exaple/music") #Only path
  except:
    print("Error")
    
def testCase3():
  try:
    playMusicLocal("T.N.T") #Only Name
  except:
    print("Error")
    
def testCase4():
  try:
    playMusicLocal() #No input
  except:
    print("Error")



