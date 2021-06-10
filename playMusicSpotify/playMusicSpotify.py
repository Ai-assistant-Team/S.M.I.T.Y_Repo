# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:08:49 2021

@author: nickk
"""
#from ......... import username (to get the username when S.M.I.T.Y is finished)
username = "" #when S.M.I.T.Y is finished delete this line

def spotifyAuth(): #used to authenticate the user with the spotify platform
    
   import spotipy 
   import spotipy.util as util
   import tkinter

   try:
       CLIENT_ID = 'f1c84641b9c34faa8bb20510ee8c9c40' #id given to the app when registered in the spotify dashboard
       CLIENT_SECRET = '1a17fbde2fd04a38a7939ce0b2120f76' #secret id given to the app when registered in the spotify dashboard
       scope = "user-read-playback-state user-modify-playback-state playlist-modify-public playlist-modify-private user-follow-read user-follow-modify user-library-read user-library-modify"
       #the permissions required for the various functions of this script
       redirect_uri = "http://localhost:8080" #the url where the users are redirected to when they log in
         
       token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri) #The authentication
       sp = spotipy.Spotify(auth=token)                                                            #proccess
       return sp
   except:
       tkinter.messagebox.showerror(title="Username Error", message="Wrong Username or Spotify premium not activated")

def getFirstAvailableDevice(): #used to return the first available device running spotify (more commonly browser,desktop or mobile)
    import tkinter
    
    try:
        sp = spotifyAuth()
          
        devices = sp.devices() #gets list of available devices
        deviceID = devices['devices'][0]['id'] #gets the id of the first device on the list
        return deviceID 
    except:
        window = tkinter.Tk()
        window.withdraw()
        tkinter.messagebox.showerror(title="Device Error", message="No device detected")

def searchForId(q,TYPE): #used to search for an id in the spotify database given a query e.g song name and a type e.g track
    try:
        sp = spotifyAuth()
        
        result=sp.search(q,1,type=TYPE) 
        resultId = result[TYPE+'s']['items'][0]['id'] #gets the id of the searched item
        return resultId
    except:
        return 1
      
def songbyTitle(songName,songArtist): #plays a song given a name and an optional artist
    try:
        sp = spotifyAuth()
        
        deviceID = getFirstAvailableDevice()
    
        if(songArtist == None):
            trackId = searchForId(songName, "track")
            sp.start_playback(deviceID, uris=["spotify:track:"+trackId])
        else:
            trackId = searchForId("track:"+songName+" artist:"+songArtist, "track")
            sp.start_playback(deviceID, uris=["spotify:track:"+trackId])
    except:
        return 1

def playEpisode(epName): #plays a podcast episode given its name
    try:
        sp = spotifyAuth()
        
        deviceID = getFirstAvailableDevice()
        
        epId = searchForId(epName, "episode")
        sp.start_playback(deviceID, uris=["spotify:episode:"+epId])
    except:
        return 1

def playShow(showName): #plays a podcast from the beginning given its name
    try:
        sp = spotifyAuth()
        
        deviceID = getFirstAvailableDevice()
        
        showId = searchForId(showName, "show")
        sp.start_playback(deviceID, "spotify:show:"+showId)
    except:
        return 1
             
def songsbyArtist(artist): #plays the top song from an artist's profile given their name
    try:
        
        sp = spotifyAuth()
    
        deviceID = getFirstAvailableDevice()
        
        artistId = searchForId(artist, "artist")
        sp.start_playback(deviceID, "spotify:artist:"+artistId)
    except:
        return 1
    
def playAlbumOrPlaylist(TYPE, name): #plays and album or a playlist from an artist's profile given its name and type (album or playlist)
    
    try:
        sp = spotifyAuth()
        
        deviceID = getFirstAvailableDevice()
        
        Id = searchForId(name, TYPE)
        if(TYPE=="album"):
            sp.start_playback(deviceID, "spotify:album:"+Id)
        else:
            sp.start_playback(deviceID, "spotify:playlist:"+Id)
    except:
        return 1
        
def resumePlayback(): #resumes a user's playback
    try:
        sp = spotifyAuth()
        
        deviceID = getFirstAvailableDevice()
        
        sp.start_playback(deviceID)
    except:
        return 1
    
def pausePlayback(): #pauses a user's playback
    
    try:
        sp = spotifyAuth()
        
        deviceID = getFirstAvailableDevice()
        
        sp.pause_playback(deviceID)
    except:
        return 1
    
def playNext(): #plays the next track in a user's playback queue
    
    try:
        sp = spotifyAuth()
    
        deviceID = getFirstAvailableDevice()
        
        sp.next_track(deviceID)
    except:
        return 1

def playPrev(): #plays the previous track in a user's playback queue

    try:   
        sp = spotifyAuth()
    
        deviceID = getFirstAvailableDevice()
        
        sp.previous_track(deviceID)
    except:
        return 1
    
def addToQueue(songName): #adds a song to the end of a user's playback queue

    try:
        sp = spotifyAuth()
    
        deviceID = getFirstAvailableDevice()
        
        itemID = searchForId(songName, "track")
        sp.add_to_queue(itemID, deviceID)
    except:
        return 1
    
def seek(whereTo): #skips to a point in the current track (input in seconds)

    try:  
        sp = spotifyAuth()
        
        deviceID = getFirstAvailableDevice()
        
        sp.seek_track(int(whereTo)*1000,deviceID)
    except:
        return 1
    
def repeatControl(whatToRepeat): #controls the repeat function of spotify (input = track/context/off)
    
    try:
        sp = spotifyAuth()
    
        deviceID = getFirstAvailableDevice()
        
        sp.repeat(whatToRepeat,deviceID)  
    except:
        return 1
    
def shuffleControl(active): #controls the repeat function of spotify (input = True/False)

    try:
        sp = spotifyAuth()
    
        deviceID = getFirstAvailableDevice()
        if(active == "True"):
            active = True
        else:
            active = False
        
        sp.shuffle(active,deviceID)
    except:
        return 1

def volumeControl(volumeLevel): #controls the inner app volume Level (input = 1-100)

    try:
        sp = spotifyAuth()
    
        deviceID = getFirstAvailableDevice()
         
        sp.volume(int(volumeLevel),deviceID)
    except:
        return 1

def playlistCreate(username, playlistName, isPublic, isCollab, description): #creates a playlist given the required parametres 

    try:
        sp = spotifyAuth()
        
        if(isPublic == "True"):
            isPublic = True
        else:
            isPublic = False
            
        if(isCollab == "True"):
            isCollab = True
        else:
            isCollab = False
        sp.user_playlist_create(username, playlistName, isPublic, isCollab, description)
    except:
        return 1
    
def playlistAddTracks(username, playlistName, trackNameList, position): #adds given tracks to a playlist

    try:
        sp = spotifyAuth()
      
        trackIDList = []
        for track in trackNameList:
            trackID = searchForId(track, "track")
            trackIDList.append(trackID)
        playlistId = searchForId(playlistName, "playlist")
        sp.user_playlist_add_tracks(username, playlistId, trackIDList, position)
    except:
        return 1
        
def playlistRemoveTracks(playlistName, trackNameList): #removes given tracks from playlist

    try:
        sp = spotifyAuth()
       
        trackIDList = []
        for track in trackNameList:
            trackID = searchForId(track, "track")
            trackIDList.append(trackID)
        playlistId = searchForId(playlistName, "playlist")
        sp.playlist_remove_all_occurrences_of_items(playlistId, trackIDList, snapshot_id=None)
    except:
        return 1
    
def playlistFollow(playlistName): #follows given playlist

    try:
        sp = spotifyAuth()
       
        playlistId = searchForId(playlistName, "playlist")
        sp.current_user_follow_playlist(playlistId)
    except:
        return 1
    
def playlistUnfollow(playlistName): #unfollows given playlist

    try:
        sp = spotifyAuth()
       
        playlistId = searchForId(playlistName, "playlist")
        sp.current_user_unfollow_playlist(playlistId)
    except:
        return 1

def artistFollow(artistNameList): #follows given artist/artists

    try:
        sp = spotifyAuth()
       
        artistIdList = []
        for artist in artistNameList:
            artistId = searchForId(artist, "artist")
            artistIdList.append(artistId)
        sp.user_follow_artists(artistIdList)
    except:
        return 1
    
def artistUnfollow(artistNameList): #unfollows given artist/artists

    try:   
        sp = spotifyAuth()
        
        artistIdList = []
        for artist in artistNameList:
            artistId = searchForId(artist, "artist")
            artistIdList.append(artistId)
        sp.user_unfollow_artists(artistIdList)
    except:
        return 1
        
def userFollow(userNameList): #follows given user/users
    
    try:
        sp = spotifyAuth()
        
        sp.user_follow_users(userNameList)
    except:
        return 1
    
def userUnfollow(userNameList): #unfollows given user/users

    try:
        sp = spotifyAuth()
        
        sp.user_unfollow_users(userNameList)
    except:
        return 1
    
def saveTracks(trackNameList): #saves given track/tracks to the user's library

    try:
        sp = spotifyAuth()
    
        trackIDList = []
        for trackName in trackNameList:
            trackID = searchForId(trackName, "track")
            trackIDList.append(trackID)
            
        isSaved = sp.current_user_saved_tracks_contains(trackIDList) 
        for i in range(len(trackIDList)-1):
            if(isSaved[i] and i<(len(trackIDList)-1)):
                trackIDList.remove(trackIDList[i])
        sp.current_user_saved_tracks_add(trackIDList)
    except:
        return 1
        
def deleteSavedTracks(trackNameList): #removes given track/tracks from the user's library

    try:
        sp = spotifyAuth()
      
        trackIDList = []
        for trackName in trackNameList:
            trackID = searchForId(trackName, "track")
            trackIDList.append(trackID)
            
        isSaved = sp.current_user_saved_tracks_contains(trackIDList)
        for i in range(len(trackIDList)-1):
            if(isSaved[i]==False and i<(len(trackIDList)-1)):
                trackIDList.remove(trackIDList[i])
        sp.current_user_saved_tracks_delete(trackIDList)
    except:
        return 1
       
def saveShows(showNameList): #saves given podcast/podcasts to the user's library

    try:
        sp = spotifyAuth()
       
        showIDList = []
        for showName in showNameList:
            showID = searchForId(showName, "show")
            showIDList.append(showID)
            
        isSaved = sp.current_user_saved_shows_contains(showIDList)
        for i in range(len(showIDList)-1):
            if(isSaved[i] and i<(len(showIDList)-1)):
                showIDList.remove(showIDList[i])
        sp.current_user_saved_shows_add(showIDList)
    except:
        return 1
      
def deleteSavedShows(showNameList): #removes given podcast/podcasts from the user's library

    try:
        sp = spotifyAuth()
        
        showIDList = []
        for showName in showNameList:
            showID = searchForId(showName, "show")
            showIDList.append(showID)
            
        isSaved = sp.current_user_saved_shows_contains(showIDList)
        for i in range(len(showIDList)-1):
            if(isSaved[i]==False and i<(len(showIDList)-1)):
                showIDList.remove(showIDList[i])
        sp.current_user_saved_shows_delete(showIDList)
    except:
        return 1
    
def saveAlbums(albumNameList): #saves given album/albums to the user's library

    try:
        sp = spotifyAuth()
        
        albumIDList = []
        for albumName in albumNameList:
            albumID = searchForId(albumName, "album")
            albumIDList.append(albumID)
        
        isSaved = sp.current_user_saved_albums_contains(albumIDList)
        for i in range(len(albumIDList)-1):
            if(isSaved[i] and i<(len(albumIDList)-1)):
                albumIDList.remove(albumIDList[i])
        sp.current_user_saved_albums_add(albumIDList)
    except:
        return 1
    
def deleteSavedAlbums(albumNameList): #removes given album/albums from the user's library
    
    try:
        sp = spotifyAuth()
       
        albumIDList = []
        for albumName in albumNameList:
            albumID = searchForId(albumName, "album")
            albumIDList.append(albumID)
        
        isSaved = sp.current_user_saved_albums_contains(albumIDList)
        for i in range(len(albumIDList)-1):
            if(isSaved[i]==False and i<(len(albumIDList)-1)):
                albumIDList.remove(albumIDList[i])
        sp.current_user_saved_albums_delete(albumIDList)
    except:
        return 1
