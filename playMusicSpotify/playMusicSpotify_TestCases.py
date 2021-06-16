# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:40:03 2021

@author: nickk
"""

from playMusicSpotify import *

def testCase1():
    songbyTitle('Toxicity', 'System of a down')

def testCase2():
    songbyTitle('Toxicity', None)
    
def testCase3():
    songsbyArtist('Nirvana')
    
def testCase4():
    playAlbumOrPlaylist('album', 'Trench')
    
def testCase5():
    playAlbumOrPlaylist('playlist', 'just rock')
    
def testCase6():
    repeatControl('track')
    
def testCase7():
    repeatControl('context')
    
def testCase8():
    repeatControl('off')
    
def testCase9():
    shuffleControl('True')
    
def testCase10():
    shuffleControl('False')
    
def testCase11():
    playlistCreate('', 'Playlist1', 'True', 'False', 'A description')
    
def testCase12():
    playlistCreate('', 'Playlist2', 'False', 'False', 'Second Description')
    
def testCase13():
    saveTracks('what a beautiful world')
    
def testCase14():
    saveTracks('what a beautiful world','welcome to the black parade')
    
def testCase15():
    ID = searchForId('Back in black','track')
    print(ID)
    
def testCase16():
    ID = searchForId('AC/DC','artist')
    print(ID)
    
def testCase17():
    ID = searchForId('track:Run boy run artist:woodkid','track')
    print(ID)
    
testCase2()
    
    