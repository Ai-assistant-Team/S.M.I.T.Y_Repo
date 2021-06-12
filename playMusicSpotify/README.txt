---------- 7/6/2021 ----------
playMusicSpotify.py : 
	spotifyAuth(): used to authenticate the user with the spotify platform
	getFirstAvailableDevice(): used to return the first available device running spotify (more commonly browser,desktop or mobile)
	searchForId(q,TYPE): used to search for an id in the spotify database given a query e.g song name and a type e.g track
	songbyTitle(songName,songArtist): plays a song given a name and an optional artist
	playEpisode(epName): plays a podcast episode given its name
	playShow(showName): plays a podcast from the beginning given its name
	songsbyArtist(artist): plays the top song from an artist's profile given their name
	playAlbumOrPlaylist(TYPE, name): plays and album or a playlist from an artist's profile given its name and type (album or playlist)
	resumePlayback(): resumes a user's playback
	pausePlayback(): pauses a user's playback
	playNext(): plays the next track in a user's playback queue
	playPrev(): plays the previous track in a user's playback queue
	addToQueue(songName): adds a song to the end of a user's playback queue
	seek(whereTo): skips to a point in the current track (input in seconds)
	repeatControl(whatToRepeat): controls the repeat function of spotify (input = track/context/off)
	shuffleControl(active): controls the repeat function of spotify (input = True/False)
	volumeControl(volumeLevel): controls the inner app volume Level (input = 1-100)
	playlistCreate(username, playlistName, isPublic, isCollab, description): #creates a playlist given the required parametres
	playlistAddTracks(username, playlistName, trackNameList, position): adds given tracks to a playlist
	playlistRemoveTracks(playlistName, trackNameList): removes given tracks from playlist
	playlistFollow(playlistName): follows given playlist
	playlistUnfollow(playlistName): unfollows given playlist
	artistFollow(artistNameList): follows given artist/artists
	artistUnfollow(artistNameList): unfollows given artist/artists
	userFollow(userNameList): follows given user/users
	userUnfollow(userNameList): unfollows given user/users
	saveTracks(trackNameList): saves given track/tracks to the user's library
	deleteSavedTracks(trackNameList): removes given track/tracks from the user's library
	saveShows(showNameList): saves given podcast/podcasts to the user's library
	deleteSavedShows(showNameList): removes given podcast/podcasts from the user's library
	saveAlbums(albumNameList): saves given album/albums to the user's library
	deleteSavedAlbums(albumNameList): removes given album/albums from the user's library

	
	