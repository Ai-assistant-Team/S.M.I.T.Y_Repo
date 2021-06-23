# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#

## ------------------------------
## Importing modules and declaring functions
## ------------------------------

# -------------------------------------------------------------
from SMITY.definePATH import *
from SMITY.counter.counter import *
from SMITY.fb_messages.facebook_messages_count import *
from SMITY.Forecast_weather_now.forecast_weather_script import *
from SMITY.GetDate.getDate import *
from SMITY.GetTime.getTime import *
from SMITY.googleMapsScripts.googleMapsDirections import *
from SMITY.googleMapsScripts.googleMapsSearch import *
from SMITY.instagram_messages.instagram_messages_count import *
from SMITY.jokesScript.jokes import *
from SMITY.open_program.open_program import *
from SMITY.playMusicLocal.playMusicLocal import *
from SMITY.playMusicSpotify.playMusicSpotify import *
from SMITY.playVideoLocal.playVideoLocal import *
from SMITY.Restart.restartDev import *
from SMITY.security.file import *
from SMITY.security.text import *
from SMITY.Shutdown.shutdownDev import *
from SMITY.Wikipedia.wikipediaScript import *
from SMITY.Youtube.youtubeScript import *
from SMITY.urlHandling.openUrls import openUrl
# -------------------------------------------------------------

import SMITY.SMITYcore.textToSpeech
import SMITY.SMITYcore.speechToText
import SMITY.SMITYcore.errorHandling
import SMITY.SMITYcore.parallelProgramming
import SMITY.SMITYcore.intentRecognition

import re

# -------------------------------------------------------------


def getSpotifyUsername():
    try:
        with open(os.path.join(PATH_TO_SETTINGS, 'settings.txt'), 'r') as f:
            for i in range(5):
                f.readline()

            user_name = f.readline()
            user_name = user_name.replace('Spotify username : ', '')
            return user_name
    except:
        return 'Spotify_Username'


def getLocalMusicPath():
    try:
        with open(os.path.join(PATH_TO_SETTINGS, 'settings.txt'), 'r') as f:
            for line in range(6):
                f.readline()

            path = f.readline()
            path = path.replace('Music path : ', '')
            return path
    except:
        return os.path.expanduser('~\\Music')


def getLocalVideoPath():
    return os.path.expanduser('~\\Videos')


def isSure():
    SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Are you sure you want to send an S.O.S signal ?')
    answer = SMITY.SMITYcore.speechToText.listen()

    if answer.lower() == 'yes':
        return True
    else:
        return False


## ------------------------------

def recognizeAndAct(userInput):

    # calling intentRecognition and getting a key which
    # refers to the action the user probably wants
    key = SMITY.SMITYcore.intentRecognition.intentRecognition(userInput)

    # declaring a constant that is needed by
    # many of the possible actions
    SPOTIFY_USERNAME = getSpotifyUsername()

    ## ------------------------------
    # The following long if-elif-else statement, is a map to the action
    # that needs to be taken for each possible command given by the user.

    if key == 'addToQueueSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the title of the song you wish to add to queue?')
        songName = SMITY.SMITYcore.speechToText.listen()
        if type(songName) == str:
            addToQueue(songName)

    elif key == 'alarmClock_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'artistFollowSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Which artist would you like to follow')
        artistName = SMITY.SMITYcore.speechToText.listen()
        if type(artistName) == str:
            artistNameList = [artistName]
            artistFollow(artistNameList)

    elif key == 'artistUnfollowSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Which artist would you like to unfollow')
        artistName = SMITY.SMITYcore.speechToText.listen()
        if type(artistName) == str:
            artistNameList = [artistName]
            artistUnfollow(artistNameList)

    elif key == 'calendar_make_event_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'calendar_Keywords':
        
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'calendar_showMeInRange_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'calendar_showMe_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'countTo_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What number would you like to count to')
        to = SMITY.SMITYcore.speechToText.listen()

        if type(to) == str:
            try:
                to = int(re.search(r'\d+', to).group())

                SMITY.SMITYcore.parallelProgramming.call_function_wCommunication(countTo, to)
            except:
                SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Invalid Input')

    elif key == 'countDown_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What number would you like to count down from')
        countDownFrom = SMITY.SMITYcore.speechToText.listen()
        if type(countDownFrom) == str:
            try:
                countDownFrom = int(re.search(r'\d+', countDownFrom).group())
                SMITY.SMITYcore.parallelProgramming.call_function_wCommunication(countDown, countDownFrom)
            except:
                SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Invalid Input')

    elif key == 'currencyConverter_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'decryptFile_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the file you want to decrypt ?')
        filename = SMITY.SMITYcore.speechToText.listen()
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the password used to encrypt this file ?')
        aKey = SMITY.SMITYcore.speechToText.listen()
        if type(filename) == type(aKey) == str:
            SMITY.SMITYcore.errorHandling.handleError(fileSecurity().decrypt(filename, aKey))

    elif key == 'decryptText_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the text you want to decrypt ?')
        cipherText = SMITY.SMITYcore.speechToText.listen()
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the password used to encrypt this text ?')
        aKey = SMITY.SMITYcore.speechToText.listen()
        if type(cipherText) == type(aKey) == str:
            decrypted = textSecurity().decrypt(cipherText, aKey='')
            if type(decrypted) == str:
                SMITY.SMITYcore.textToSpeech.Text2Speech().speak(decrypted)

    elif key == 'deleteSavedAlbumsSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the album you wish to delete ?')
        albumNameList = SMITY.SMITYcore.speechToText.listen()
        if type(albumNameList) == str:
            SMITY.SMITYcore.errorHandling.handleError(deleteSavedAlbums(albumNameList))

    elif key == 'deleteSavedShowsSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the show you wish to delete ?')
        showName = SMITY.SMITYcore.speechToText.listen()
        if type(showName) == str:
            showNameList = [showName]
            SMITY.SMITYcore.errorHandling.handleError(deleteSavedShows(showNameList))

    elif key == 'deleteSavedTracksSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the track you wish to delete ?')
        trackName = SMITY.SMITYcore.speechToText.listen()
        if type(trackName) == str:
            trackNameList = [trackName]
            SMITY.SMITYcore.errorHandling.handleError(deleteSavedTracks(trackNameList))

    elif key == 'encryptFile_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the file you wish to decrypt ?')
        filename = SMITY.SMITYcore.speechToText.listen()
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What password would you like to use ?')
        aKey = SMITY.SMITYcore.speechToText.listen()

        if type(filename) == type(aKey) == str:
            if aKey.lower() == 'no password':
                aKey = ''
            SMITY.SMITYcore.errorHandling.handleError(fileSecurity().encrypt(filename, aKey))

    elif key == 'encryptText_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the text you wish to decrypt ?')
        clearText = SMITY.SMITYcore.speechToText.listen()
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What password would you like to use ?')
        aKey = SMITY.SMITYcore.speechToText.listen()
        if type(clearText) == type(aKey) == str:
            if aKey.lower() == 'no password':
                aKey = ''
            encrypted = textSecurity().encrypt(clearText, aKey)
            if type(encrypted) is str:
                SMITY.SMITYcore.textToSpeech.Text2Speech().speak(encrypted)

    elif key == 'facebookMessagesCount_Keywords':

        result = facebook_messages_count()
        if type(result) is str:
            SMITY.SMITYcore.textToSpeech.Text2Speech().speak(result)
        else:
            SMITY.SMITYcore.errorHandling.handleError(result)

    elif key == 'forecastWeather_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('For what city would you like to know the weather ?')
        city = SMITY.SMITYcore.speechToText.listen()
        if type(city) == str:
            result = forecast_weather_now(city)
            if type(result) is str:
                SMITY.SMITYcore.textToSpeech.Text2Speech().speak(result)
            else:
                SMITY.SMITYcore.errorHandling.handleError(result)

    elif key == 'funFacts_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'getDate_Keywords':

        result = getDate()
        if type(result) == str:
            SMITY.SMITYcore.textToSpeech.Text2Speech().speak(result)
        else:
            SMITY.SMITYcore.errorHandling.handleError(result)

    elif key == 'getTime_Keywords':

        result = getTime()
        if type(result) == str:
            SMITY.SMITYcore.textToSpeech.Text2Speech().speak(result)
        else:
            SMITY.SMITYcore.errorHandling.handleError(result)

    elif key == 'get_news_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'gmailRead_Keywords':

        # Though the script is fully functional, it can't use the user's credentials if Google doesn't authorize the app
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'gmailSend_Keywords':

        # Though the script is fully functional, it can't use the user's credentials if Google doesn't authorize the app
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'googleMapsDirections_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Where would you like to go ?')
        destination = SMITY.SMITYcore.speechToText.listen()
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('From where would you like to go there ?')
        origin = SMITY.SMITYcore.speechToText.listen()

        if type(destination) == type(origin) == str:
            result = googleMapsDirections(origin, destination)
            SMITY.SMITYcore.errorHandling.handleError(result)

    elif key == 'googleMapsSearch_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What would you like to search for in Google Maps ?')
        query = SMITY.SMITYcore.speechToText.listen()
        if type(query) == str:
            SMITY.SMITYcore.errorHandling.handleError(googleMapsSearch(query))

    elif key == 'googleSearch_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'instagramMessagesCount_Keywords':

        result = instagram_messages_count()
        if type(result) is str:
            SMITY.SMITYcore.textToSpeech.Text2Speech().speak(result)
        else:
            SMITY.SMITYcore.errorHandling.handleError(result)


    elif key == 'jokes_Keywords':

        result = jokes()
        if type(result) is str:
            SMITY.SMITYcore.textToSpeech.Text2Speech().speak(result)
        else:
            SMITY.SMITYcore.errorHandling.handleError(result)

    elif key == 'lockScreen_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'openProgram_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Which program should I open ?')
        program_name = SMITY.SMITYcore.speechToText.listen()
        if type(program_name) == str:
            SMITY.SMITYcore.errorHandling.handleError(open_program(program_name))

    elif key == 'openUrls_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What url would you like me to open ?')
        url = SMITY.SMITYcore.speechToText.listen()
        if type(url) == str:
            SMITY.SMITYcore.errorHandling.handleError(openUrl(url))

    elif key == 'open_news_page_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'pausePlaybackSpotify_Keywords':

        SMITY.SMITYcore.errorHandling.handleError(pausePlayback())

    elif key == 'photoCapture_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'playAlbumSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the album you would like to hear ?')
        name = SMITY.SMITYcore.speechToText.listen()
        if type(name) == str:
            SMITY.SMITYcore.errorHandling.handleError(playAlbumOrPlaylist('album', name))

    elif key == 'playEpisodeSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the episode you would like to hear ?')
        epName = SMITY.SMITYcore.speechToText.listen()
        if type(epName) == str:
            SMITY.SMITYcore.errorHandling.handleError(playEpisode(epName))

    elif key == 'playlistAddTracksSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('In which playlist would you like to add the song ?')
        playlistName = SMITY.SMITYcore.speechToText.listen()
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the song you would like to add ?')
        trackNameList = SMITY.SMITYcore.speechToText.listen()

        if type(playlistName) == type(trackNameList) == str:
            SMITY.SMITYcore.errorHandling.handleError(playlistAddTracks(SPOTIFY_USERNAME, playlistName, trackNameList, '1'))

    elif key == 'playlistCreateSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What name would you like to give to your new playlist ?')
        playlistName = SMITY.SMITYcore.speechToText.listen()
        if type(playlistName) == str:
            SMITY.SMITYcore.errorHandling.handleError(playlistCreate(SPOTIFY_USERNAME, playlistName, False, False, ''))

    elif key == 'playlistFollowSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'playlistRemoveTracksSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Please, tell me the name of the playlist from which you would like to remove the track')
        playlistName = SMITY.SMITYcore.speechToText.listen()
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the track you would like to remove from this playlist ?')
        trackName = SMITY.SMITYcore.speechToText.listen()
        if type(playlistName) == type(trackName) == str:
            trackNameList = [trackName]
            SMITY.SMITYcore.errorHandling.handleError(playlistRemoveTracks(playlistName, trackNameList))

    elif key == 'playlistUnfollowSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the playlist you would like to unfollow ?')
        playlistName = SMITY.SMITYcore.speechToText.listen()
        if type(playlistName) == str:
            SMITY.SMITYcore.errorHandling.handleError(playlistUnfollow(playlistName))

    elif key == 'playMusicLocal_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the song you would like to listen ?')
        songName = SMITY.SMITYcore.speechToText.listen()
        if type(songName) == str:
            songPath = getLocalMusicPath()
            SMITY.SMITYcore.errorHandling.handleError(playMusicLocal(songName, songPath))

    elif key == 'playMusicSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the song you would like Spotify to play ?')
        songName = SMITY.SMITYcore.speechToText.listen()
        if type(songName) == str:
            SMITY.SMITYcore.errorHandling.handleError(songbyTitle(songName, None))

    elif key == 'playNextSpotify_Keywords':

        SMITY.SMITYcore.errorHandling.handleError(playNext())

    elif key == 'playPlaylistSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the playlist you would like to play ?')
        name = SMITY.SMITYcore.speechToText.listen()
        if type(name) == str:
            SMITY.SMITYcore.errorHandling.handleError(playAlbumOrPlaylist('playlist', name))

    elif key == 'playPrevSpotify_Keywords':

        SMITY.SMITYcore.errorHandling.handleError(playPrev())

    elif key == 'playShowSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the show that you would like to hear ?')
        showName = SMITY.SMITYcore.speechToText.listen()
        if type(showName) == str:
            SMITY.SMITYcore.errorHandling.handleError(playShow(showName))

    elif key == 'playVideoLocal_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the video you would like to watch ?')
        videoName = SMITY.SMITYcore.speechToText.listen()
        if type(videoName) == str:
            videoPath = getLocalVideoPath()
            SMITY.SMITYcore.errorHandling.handleError(playVideoLocal(videoName, videoPath))

    elif key == 'repeatControlSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'restartDevice_Keywords':

        SMITY.SMITYcore.errorHandling.handleError(restartDevTimer(0))  # t=0 for instant restart

    elif key == 'resumePlaybackSpotify_Keywords':

        SMITY.SMITYcore.errorHandling.handleError(resumePlayback())

    elif key == 'saveAlbumsSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the album you would like to save ?')
        albumName = SMITY.SMITYcore.speechToText.listen()
        if type(albumName) == str:
            albumNameList = [albumName]
            SMITY.SMITYcore.errorHandling.handleError(saveAlbums(albumNameList))

    elif key == 'saveShowsSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the show you would like to save ?')
        showName = SMITY.SMITYcore.speechToText.listen()
        if type(showName) == str:
            showNameList = [showName]
            SMITY.SMITYcore.errorHandling.handleError(saveShows(showNameList))

    elif key == 'saveTracksSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What is the name of the track you would like to save ?')
        trackName = SMITY.SMITYcore.speechToText.listen()
        if type(trackName) == str:
            trackNameList = [trackName]
            SMITY.SMITYcore.errorHandling.handleError(saveTracks(trackNameList))

    elif key == 'screenRecord_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'screenshot_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'seekSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('To which minute of the song would to like to skip to')
        whereTo = SMITY.SMITYcore.speechToText.listen()

        try:
            whereTo = int(re.search(r'\d+', whereTo).group())
            whereTo = whereTo * 60  # to become seconds from minutes
            if type(whereTo) == int:
                SMITY.SMITYcore.errorHandling.handleError(seek(whereTo))
        except:
            SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Invalid Input')

    elif key == 'shuffleControlSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Would you like to have shuffle activated ?')
        ans = SMITY.SMITYcore.speechToText.listen()
        if type(ans) == str:
            if ans.lower() == 'yes':
                SMITY.SMITYcore.errorHandling.handleError(shuffleControl('True'))
            elif ans.lower() == 'no':
                SMITY.SMITYcore.errorHandling.handleError(shuffleControl('False'))
            else:
                SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Invalid Answer')

    elif key == 'shutdownDevice_Keywords':

        SMITY.SMITYcore.errorHandling.handleError(shutdownDevTimer(0))  # t = 0 for instant shutdown

    elif key == 'songsbyArtistSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak("What artist's songs would you like to play ?")
        Artist = SMITY.SMITYcore.speechToText.listen()
        if type(Artist) == str:
            SMITY.SMITYcore.errorHandling.handleError(songsbyArtist(Artist))

    elif key == 'sosSignal_Keywords':

        # The script uses the gmail send function which is not supported yet for reasons explained before
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'translateText_Keywords':
        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this option is not supported yet.')

    elif key == 'userFollowSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'userUnfollowSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')


    elif key == 'videoCapture_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('I am sorry, this is not supported yet.')

    elif key == 'volumeControlSpotify_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Which value should I set to the volume')
        volumeLevel = SMITY.SMITYcore.speechToText.listen()
        if type(volumeLevel) == str:
            try:
                volumeLevel = int(re.search(r'\d+', volumeLevel).group())

                if 1 <= volumeLevel <= 100:
                    SMITY.SMITYcore.errorHandling.handleError(volumeControl(volumeLevel))
                else:
                    SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Invalid Value')
            except:
                SMITY.SMITYcore.textToSpeech.Text2Speech().speak('Invalid Input')

    elif key == 'wikipedia_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What would you like to search in Wikipedia ?')
        toSearch = SMITY.SMITYcore.speechToText.listen()
        if type(toSearch) == str:
            SMITY.SMITYcore.textToSpeech.Text2Speech().speak(Wiki_Search(toSearch))
        else:
            SMITY.SMITYcore.errorHandling.handleError(Wiki_Search(toSearch))

    elif key == 'youtube_Keywords':

        SMITY.SMITYcore.textToSpeech.Text2Speech().speak('What would you like to search in YouTube ?')
        toSearch = SMITY.SMITYcore.speechToText.listen()
        if type(toSearch) == str:
            SMITY.SMITYcore.errorHandling.handleError(Youtube_Search(toSearch))

    else:
        # If none of key is none of the above, it means that a wrong
        # command was given. So error code 7 is returned.
        return 7    # 7 : I did not understand that

    return 0
# end of recognizeAndAct


def writtenCommandFromGUI(command):
    recognizeAndAct(command)
# end of writtenCommandFromGUI
