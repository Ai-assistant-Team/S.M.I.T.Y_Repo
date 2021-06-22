# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:08:49 2021

@author: nickk
"""
def spotifyAuth(): #used to authenticate the user with the spotify platform
    
   import spotipy #used to comunicate with spotify
   import spotipy.util as util #used for authentication

   try:
       CLIENT_ID = 'f1c84641b9c34faa8bb20510ee8c9c40' #id given to the app when registered in the spotify dashboard
       CLIENT_SECRET = '1a17fbde2fd04a38a7939ce0b2120f76' #secret id given to the app when registered in the spotify dashboard
       scope = 'user-read-playback-state user-modify-playback-state playlist-modify-public playlist-modify-private user-follow-read user-follow-modify user-library-read user-library-modify'
       #the permissions required for the various functions of this script
       redirect_uri = 'http://localhost:8080' #the url where the users are redirected to when they log in
         
       token = util.prompt_for_user_token('', scope, CLIENT_ID, CLIENT_SECRET, redirect_uri) #The authentication
       sp = spotipy.Spotify(auth=token)                                                            #proccess
       return sp
   except:
       return 1

def getFirstAvailableDevice(): #used to return the first available device running spotify (more commonly browser,desktop or mobile)
    from urlHandling.openUrls import openUrl #used to open spotify web page in case it or the spotify desktop app is not already open
    from time import sleep #used to delay authentication until the spotify web page is loaded
    
    for i in range(5):
        try:
            sp = spotifyAuth()
              
            devices = sp.devices() #gets list of available devices
            deviceid = devices['devices'][0]['id'] #gets the id of the first device on the list
            return deviceid 
        except:
            openUrl('https://open.spotify.com/')
            sleep(5)
            print(i)
    
        

def searchForId(q,idtype): #used to search for an id in the spotify database given a query e.g song name and a type e.g track
    try:
        sp = spotifyAuth()
        
        result=sp.search(q,1,type=idtype) 
        resultid = result[idtype+'s']['items'][0]['id'] #gets the id of the searched item
        return resultid
    except:
        return 1
      
def songbyTitle(songname,songartist): #plays a song given a name and an optional artist
    try:
        sp = spotifyAuth()
        
        deviceid = getFirstAvailableDevice()
    
        if(songartist == None):
            trackid = searchForId(songname, 'track')
            sp.start_playback(deviceid, uris=['spotify:track:'+trackid])
        else:
            trackid = searchForId('track:'+songname+' artist:'+songartist, 'track')
            sp.start_playback(deviceid, uris=['spotify:track:'+trackid])
            return 0
    except:
        return 1
        

def playEpisode(epname): #plays a podcast episode given its name
    try:
        sp = spotifyAuth()
        
        deviceid = getFirstAvailableDevice()
        
        epid = searchForId(epname, 'episode')
        sp.start_playback(deviceid, uris=['spotify:episode:'+epid])
        return 0
    except:
        return 1

def playShow(showname): #plays a podcast from the beginning given its name
    try:
        sp = spotifyAuth()
        
        deviceid = getFirstAvailableDevice()
        
        showid = searchForId(showname, 'show')
        sp.start_playback(deviceid, 'spotify:show:'+showid)
        return 0
    except:
        return 1
             
def songsbyArtist(artist): #plays the top song from an artist's profile given their name
    try:
        
        sp = spotifyAuth()
    
        deviceid = getFirstAvailableDevice()
        
        artistid = searchForId(artist, 'artist')
        sp.start_playback(deviceid, 'spotify:artist:'+artistid)
        return 0
    except:
        return 1
    
def playAlbumOrPlaylist(itemtype, name): #plays and album or a playlist from an artist's profile given its name and type (album or playlist)
    
    try:
        sp = spotifyAuth()
        
        deviceid = getFirstAvailableDevice()
        
        itemid = searchForId(name, itemtype)
        if(itemtype=='album'):
            sp.start_playback(deviceid, 'spotify:album:'+itemid)
        else:
            sp.start_playback(deviceid, 'spotify:playlist:'+itemid)
        return 0
    except:
        return 1
        
def resumePlayback(): #resumes a user's playback
    try:
        sp = spotifyAuth()
        
        deviceid = getFirstAvailableDevice()
        
        sp.start_playback(deviceid)
        return 0
    except:
        return 1
    
def pausePlayback(): #pauses a user's playback
    
    try:
        sp = spotifyAuth()
        
        deviceid = getFirstAvailableDevice()
        
        sp.pause_playback(deviceid)
        return 0
    except:
        return 1
    
def playNext(): #plays the next track in a user's playback queue
    
    try:
        sp = spotifyAuth()
    
        deviceid = getFirstAvailableDevice()
        
        sp.next_track(deviceid)
        return 0
    except:
        return 1

def playPrev(): #plays the previous track in a user's playback queue

    try:   
        sp = spotifyAuth()
    
        deviceid = getFirstAvailableDevice()
        
        sp.previous_track(deviceid)
        return 0
    except:
        return 1
    
def addToQueue(songname): #adds a song to the end of a user's playback queue

    try:
        sp = spotifyAuth()
    
        deviceid = getFirstAvailableDevice()
        
        itemid = searchForId(songname, 'track')
        sp.add_to_queue(itemid, deviceid)
        return 0
    except:
        return 1
    
def seek(whereto): #skips to a point in the current track (input in seconds)

    try:  
        sp = spotifyAuth()
        
        deviceid = getFirstAvailableDevice()
        
        sp.seek_track(int(whereto)*1000,deviceid)
        return 0
    except:
        return 1
    
def repeatControl(whattorepeat): #controls the repeat function of spotify (input = track/context/off)
    
    try:
        sp = spotifyAuth()
    
        deviceid = getFirstAvailableDevice()
        
        sp.repeat(whattorepeat,deviceid)  
        return 0
    except:
        return 1
    
def shuffleControl(active): #controls the repeat function of spotify (input = True/False)

    try:
        sp = spotifyAuth()
    
        deviceid = getFirstAvailableDevice()
        if(active == 'True'):
            active = True
        else:
            active = False
        
        sp.shuffle(active,deviceid)
        return 0
    except:
        return 1

def volumeControl(volumelevel): #controls the inner app volume Level (input = 1-100)

    try:
        sp = spotifyAuth()
    
        deviceid = getFirstAvailableDevice()
         
        sp.volume(int(volumelevel),deviceid)
        return 0
    except:
        return 1

def playlistCreate(username, playlistname, ispublic, iscollab, description): #creates a playlist given the required parametres 

    try:
        sp = spotifyAuth()
        
        if(ispublic == 'True'):
            ispublic = True
        else:
            ispublic = False
            
        if(iscollab == 'True'):
            iscollab = True
        else:
            iscollab = False
        sp.user_playlist_create(username, playlistname, ispublic, iscollab, description)
        return 0
    except:
        return 1
    
def playlistAddTracks(username, playlistname, tracknamelist, position): #adds given tracks to a playlist

    try:
        sp = spotifyAuth()
      
        trackidlist = []
        for track in tracknamelist:
            trackid = searchForId(track, 'track')
            trackidlist.append(trackid)
        playlistid = searchForId(playlistname, 'playlist')
        sp.user_playlist_add_tracks(username, playlistid, trackidlist, position)
        return 0
    except:
        return 1
        
def playlistRemoveTracks(playlistname, tracknamelist): #removes given tracks from playlist

    try:
        sp = spotifyAuth()
       
        trackidlist = []
        for track in tracknamelist:
            trackid = searchForId(track, 'track')
            trackidlist.append(trackid)
        playlistid = searchForId(playlistname, 'playlist')
        sp.playlist_remove_all_occurrences_of_items(playlistid, trackidlist, snapshot_id=None)
        return 0
    except:
        return 1
    
def playlistFollow(playlistname): #follows given playlist

    try:
        sp = spotifyAuth()
       
        playlistid = searchForId(playlistname, 'playlist')
        sp.current_user_follow_playlist(playlistid)
        return 0
    except:
        return 1
    
def playlistUnfollow(playlistname): #unfollows given playlist

    try:
        sp = spotifyAuth()
       
        playlistid = searchForId(playlistname, 'playlist')
        sp.current_user_unfollow_playlist(playlistid)
        return 0
    except:
        return 1

def artistFollow(artistnamelist): #follows given artist/artists

    try:
        sp = spotifyAuth()
       
        artistidlist = []
        for artist in artistnamelist:
            artistid = searchForId(artist, 'artist')
            artistidlist.append(artistid)
        sp.user_follow_artists(artistidlist)
        return 0
    except:
        return 1
    
def artistUnfollow(artistnamelist): #unfollows given artist/artists

    try:   
        sp = spotifyAuth()
        
        artistidlist = []
        for artist in artistnamelist:
            artistid = searchForId(artist, 'artist')
            artistidlist.append(artistid)
        sp.user_unfollow_artists(artistidlist)
        return 0
    except:
        return 1
        
def userFollow(usernamelist): #follows given user/users
    
    try:
        sp = spotifyAuth()
        
        sp.user_follow_users(usernamelist)
        return 0
    except:
        return 1
    
def userUnfollow(usernamelist): #unfollows given user/users

    try:
        sp = spotifyAuth()
        
        sp.user_unfollow_users(usernamelist)
        return 0
    except:
        return 1
    
def saveTracks(tracknamelist): #saves given track/tracks to the user's library

    try:
        sp = spotifyAuth()
    
        trackidlist = []
        for trackname in tracknamelist:
            trackid = searchForId(trackname, 'track')
            trackidlist.append(trackid)
            
        issaved = sp.current_user_saved_tracks_contains(trackidlist) 
        for i in range(len(trackidlist)-1):
            if(issaved[i] and i<(len(trackidlist)-1)):
                trackidlist.remove(trackidlist[i])
        sp.current_user_saved_tracks_add(trackidlist)
        return 0
    except:
        return 1
        
def deleteSavedTracks(tracknamelist): #removes given track/tracks from the user's library

    try:
        sp = spotifyAuth()
      
        trackidlist = []
        for trackname in tracknamelist:
            trackid = searchForId(trackname, 'track')
            trackidlist.append(trackid)
            
        issaved = sp.current_user_saved_tracks_contains(trackidlist)
        for i in range(len(trackidlist)-1):
            if(issaved[i]==False and i<(len(trackidlist)-1)):
                trackidlist.remove(trackidlist[i])
        sp.current_user_saved_tracks_delete(trackidlist)
        return 0
    except:
        return 1
       
def saveShows(shownamelist): #saves given podcast/podcasts to the user's library

    try:
        sp = spotifyAuth()
       
        showidlist = []
        for showname in shownamelist:
            showid = searchForId(showname, 'show')
            showidlist.append(showid)
            
        issaved = sp.current_user_saved_shows_contains(showidlist)
        for i in range(len(showidlist)-1):
            if(issaved[i] and i<(len(showidlist)-1)):
                showidlist.remove(showidlist[i])
        sp.current_user_saved_shows_add(showidlist)
        return 0
    except:
        return 1
      
def deleteSavedShows(shownamelist): #removes given podcast/podcasts from the user's library

    try:
        sp = spotifyAuth()
        
        showidlist = []
        for showname in shownamelist:
            showid = searchForId(showname, 'show')
            showidlist.append(showid)
            
        issaved = sp.current_user_saved_shows_contains(showidlist)
        for i in range(len(showidlist)-1):
            if(issaved[i]==False and i<(len(showidlist)-1)):
                showidlist.remove(showidlist[i])
        sp.current_user_saved_shows_delete(showidlist)
        return 0
    except:
        return 1
    
def saveAlbums(albumnamelist): #saves given album/albums to the user's library

    try:
        sp = spotifyAuth()
        
        albumidlist = []
        for albumname in albumnamelist:
            albumid = searchForId(albumname, 'album')
            albumidlist.append(albumid)
        
        issaved = sp.current_user_saved_albums_contains(albumidlist)
        for i in range(len(albumidlist)-1):
            if(issaved[i] and i<(len(albumidlist)-1)):
                albumidlist.remove(albumidlist[i])
        sp.current_user_saved_albums_add(albumidlist)
        return 0
    except:
        return 1
    
def deleteSavedAlbums(albumnamelist): #removes given album/albums from the user's library
    
    try:
        sp = spotifyAuth()
       
        albumidlist = []
        for albumname in albumnamelist:
            albumid = searchForId(albumname, 'album')
            albumidlist.append(albumid)
        
        issaved = sp.current_user_saved_albums_contains(albumidlist)
        for i in range(len(albumidlist)-1):
            if(issaved[i]==False and i<(len(albumidlist)-1)):
                albumidlist.remove(albumidlist[i])
        sp.current_user_saved_albums_delete(albumidlist)
        return 0
    except:
        return 1

