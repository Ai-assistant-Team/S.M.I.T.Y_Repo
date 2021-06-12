# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:24:19 2021

@author: nickk
"""
from playMusicSpotify import *

def playMusicSpotifyTest():
    
    print("Welcome to the spotify script!\nWhat do you want to do?\n---------------------------------")
    while(True):
        choice = input("1.Modify Playback(Resume, Pause, Add to queue, Skip to next track, Skip to previous track, Seek in track, Enable/Disable Reapeat, Enable/Disable Shuffle, Change the volume)\n2.Search and Play a track\n3.Search and Play an episode\n4.Play tracks from an artist\n5.Play a show\n6.Play album or playlist\n7.Modify playlist(Create, Add tracks, Remove tracks, Follow, Unfollow)\n8.Modify Library(Save/Remove tracks, Save/Remove albums, Save/Remove shows, Artist/User Follow/Unfollow)\nPRESS ANY OTHER KEY TO QUIT\nInput: ")
        if(int(choice) == 1):
            
            choice2 = input("      1.Resume\n      2.Pause\n      3.Add to queue\n      4.Next track\n      5.Previous track\n      6.Seek\n      7.Repeat\n      8.Shuffle\n      9.Volume contol\nInput:")
            if(int(choice2) == 1):
                resumePlayback()
            elif(int(choice2) == 2):
                pausePlayback()
            elif(int(choice2) == 3):
                itemName = input("Enter song name: ")
                addToQueue(itemName)
            elif(int(choice2) == 4):
                playNext()
            elif(int(choice2) == 5):
                playPrev()
            elif(int(choice2) == 6):
                whereTo = input("Skip where?: ")
                seek(whereTo)
            elif(int(choice2) == 7):
                flag = input("track/context/off: ")
                repeatControl(flag)
            elif(int(choice2) == 8):
                flag = input("True/False: ")
                shuffleControl(flag)
            elif(int(choice2) == 9):
                howMuch = input("How much: ")
                volumeControl(howMuch)
        elif(int(choice) == 2):
            songName = input("Enter song name: ")
            choice2 = input("Do you know the artist (yes/no): ")
            if(choice2 == "yes"):
                songArtist = input("Enter artist name: ")
                songbyTitle(songName, songArtist)
            else:
                songbyTitle(songName, None)
        elif(int(choice) == 3):
            epName = input("Enter episode name: ")
            playEpisode(epName)
        elif(int(choice)  == 4):
            artistName = input("Enter artist name: ")
            songsbyArtist(artistName)
        elif(int(choice)  == 5):
            showName = input("Enter show name: ")
            playShow(showName)
        elif(int(choice)  == 6):
            itemName = input("Enter album/playlist name: ")
            itemType = input("Enter item type(album/playlist): ")
            playAlbumOrPlaylist(itemType, itemName)
        elif(int(choice)  == 7):
            choice2 = input("      1.Create\n      2.Add track\n      3.Remove tracks\n      4.Follow\n      5.Unfollow\nInput:")
            if(int(choice2) == 1):
                playlistName = input("Enter playlist name: ")
                isPublic = input("Is it public?(True/False): ")
                isCollab = input("Is it collab?(True/False): ")
                description = input("Enter description: ")
                playlistCreate(username, playlistName, isPublic, isCollab, description)
            elif(int(choice2) == 2):
                playlistName = input("Enter playlist name: ")
                trackNameList = []
                while(True):
                    trackName = input("Enter track name: ")
                    trackNameList.append(trackName)
                    flag = input("Add another?(yes/no): ")
                    if(flag == "no"):
                        break
                playlistAddTracks(username, playlistName, trackNameList, None)
            elif(int(choice2) == 3):
                playlistName = input("Enter playlist name: ")
                trackNameList = []
                while(True):
                    trackName = input("Enter track name: ")
                    trackNameList.append(trackName)
                    flag = input("Add another?(yes/no): ")
                    if(flag == "no"):
                        break
                playlistRemoveTracks(playlistName, trackNameList)
            elif(int(choice2) == 4):
                playlistName = input("Enter playlist name: ")
                playlistFollow(playlistName)
            elif(int(choice2) == 5):
                playlistName = input("Enter playlist name: ")
                playlistUnfollow(playlistName)
        elif(int(choice) == 8):
            choice2 = input("      1.Save/Remove tracks\n      2.Save/Remove albums\n      3.Save/Remove shows\n      4.Artist/User Follow/Unfollow\nInput:")
            if(int(choice2) == 1):
                choice3 = input("            1.Save\n            2.Remove\nInput: ")
                if(int(choice3) == 1):
                    trackNameList = []
                    while(True):
                        trackName = input("Enter track name: ")
                        trackNameList.append(trackName)
                        flag = input("Add another?(yes/no): ")
                        if(flag == "no"):
                            break
                    saveTracks(trackNameList)
                elif(int(choice3) == 2):
                    trackNameList = []
                    while(True):
                        trackName = input("Enter track name: ")
                        trackNameList.append(trackName)
                        flag = input("Add another?(yes/no): ")
                        if(flag == "no"):
                            break
                    deleteSavedTracks(trackNameList)
            elif(int(choice2) == 2):
                choice3 = input("            1.Save\n            2.Remove\nInput: ")
                if(int(choice3) == 1):
                    albumNameList = []
                    while(True):
                        albumName = input("Enter album name: ")
                        albumNameList.append(albumName)
                        flag = input("Add another?(yes/no): ")
                        if(flag == "no"):
                            break
                    saveAlbums(albumNameList)
                elif(int(choice3) == 2):
                    albumNameList = []
                    while(True):
                        albumName = input("Enter album name: ")
                        albumNameList.append(albumName)
                        flag = input("Add another?(yes/no): ")
                        if(flag == "no"):
                            break
                    deleteSavedAlbums(albumNameList)
            elif(int(choice2) == 3):
                choice3 = input("            1.Save\n            2.Remove\nInput: ")
                if(int(choice3) == 1):
                    showNameList = []
                    while(True):
                        showName = input("Enter show name: ")
                        showNameList.append(showName)
                        flag = input("Add another?(yes/no): ")
                        if(flag == "no"):
                            break
                    saveShows(showNameList)
                elif(int(choice3) == 2):
                    showNameList = []
                    while(True):
                        showName = input("Enter show name: ")
                        showNameList.append(showName)
                        flag = input("Add another?(yes/no): ")
                        if(flag == "no"):
                            break
                    deleteSavedShows(showNameList)
            elif(int(choice2) == 4):
                choice3 = input("            1.Follow\n            2.Unfollow\nInput: ")
                if(int(choice3) == 1):
                    choice4 = input("                  1.Artist\n                  2.User\nInput: ")
                    if(int(choice4) == 1):
                        artistNameList = []
                        while(True):
                            artistName = input("Enter artist name: ")
                            artistNameList.append(artistName)
                            flag = input("Add another?(yes/no): ")
                            if(flag == "no"):
                                break
                        artistFollow(artistNameList)
                    elif(int(choice4) == 2):
                        userNameList = []
                        while(True):
                            userName = input("Enter user name: ")
                            userNameList.append(userName)
                            flag = input("Add another?(yes/no): ")
                            if(flag == "no"):
                                break
                        userFollow(userNameList)
                elif(int(choice3) == 2):
                    choice4 = input("                  1.Artist\n                  2.User\nInput: ")
                    if(int(choice4) == 1):
                        artistNameList = []
                        while(True):
                            artistName = input("Enter artist name: ")
                            artistNameList.append(artistName)
                            flag = input("Add another?(yes/no): ")
                            if(flag == "no"):
                                break
                        artistUnfollow(artistNameList)
                    elif(int(choice4) == 2):
                        userNameList = []
                        while(True):
                            userName = input("Enter user name: ")
                            userNameList.append(userName)
                            flag = input("Add another?(yes/no): ")
                            if(flag == "no"):
                                break
                        userUnfollow(userNameList)
        else:
            break

playMusicSpotifyTest()