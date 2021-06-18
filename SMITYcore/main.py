#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

# -------------------------------------------------------------
from SMITY.definePATH import *
from SMITY.AlarmClock.alarmClock import *
from SMITY.counter.counter import *
from SMITY.currency_converter.ExchangeRates import *
from SMITY.fb_messages.facebook_messages_count import *
from SMITY.Forecast_weather_now.forecast_weather_script import *
from SMITY.funFactsScript.funFacts import *
from SMITY.GetDate.getDate import *
from SMITY.GetTime.getTime import *
from SMITY.gmailScripts.read import *
from SMITY.gmailScripts.send import *
from SMITY.googleMapsScripts.googleMapsDirections import *
from SMITY.googleMapsScripts.googleMapsSearch import *
from SMITY.googleSearch.googleSearchCust import *
from SMITY.instagram_messages.instagram_messages_count import *
from SMITY.jokesScript.jokes import *
from SMITY.LockScrn.lockScrn import *
from SMITY.News.ClearTheTxtOfLinks import *
from SMITY.News.news import *
from SMITY.open_program.open_program import *
from SMITY.PhotoCapture.photoCapture import *
from SMITY.playMusicLocal.playMusicLocal import *
from SMITY.playMusicSpotify.playMusicSpotify import *
from SMITY.playVideoLocal.playVideoLocal import *
from SMITY.Restart.restartDev import *
from SMITY.screenRecord.screenrecord import *
from SMITY.screenshotScript.screenshot import *
from SMITY.security.file import *
from SMITY.security.text import *
from SMITY.Shutdown.shutdownDev import *
from SMITY.SMITY_GUI.gui3 import home_page_to_calendar
from SMITY.sos_signal.sos_signal import *
# from SMITY.urlHandling.openUrls import *
from SMITY.VideoCapture.videoCapture import *
from SMITY.Wikipedia.wikipediaScript import *
from SMITY.Youtube.youtubeScript import *
from SMITY.urlHandling.openUrls import openUrl
# -------------------------------------------------------------

import multiprocessing
from printToGUI import print2gui
from init import init
from textToSpeech import Text2Speech
from wakeup import waitForWakeup
from speechToText import listen
from intentRecognition import intentRecognition
from errorHandling import handleError

# ------------------------------
# Initialize App
# ------------------------------

init()

# ------------------------------


# ------------------------------
# For Parallel Programming
# ------------------------------


def communicateWithRunningFunctions(conn):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    ##
    ## function to print the messages received from running job
    ##
    while 1:
        msg = conn.recv()
        if type(msg) == str:
            print2gui("{}".format(msg))
        elif type(msg) == int:
            pass
            # import error codes, identify the error and act accordingly
            # or, maybe, return the code. (if the codes are of problems that can be fixed, then prefer option one)
        else:
            return 1


def call_function_wCommunication(function2beCalled, *functionsArgs):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    parent_conn, child_conn = multiprocessing.Pipe()

    # if the function2beCalled doesn't sleep after sending a message, add the following code after each send :
    # from time import sleep
    # sleep(0.0000000000001)
    # so that the receiver gets its turn to receive the messages and do what he has got to do with them
    p_function = multiprocessing.Process(target=function2beCalled, args=(parent_conn, *functionsArgs))
    receiver = multiprocessing.Process(target=communicateWithRunningFunctions, args=(child_conn,))

    receiver.start()
    p_function.start()

    p_function.join()
    receiver.join()


def call_function(function2beCalled, *functionsArgs):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    # if the function2beCalled doesn't sleep after sending a message, add the following code after each send :
    # from time import sleep
    # sleep(0.0000000000001)
    # so that the receiver gets its turn to receive the messages and do what he has got to do with them
    p_function = multiprocessing.Process(target=function2beCalled, args=(*functionsArgs,))

    p_function.start()
    p_function.join()

# ------------------------------
# End <For Parallel Programming>
# ------------------------------


# ------------------------------
# Listen For Wakeup Word
# ------------------------------

## Start a parallel process that
## waits to hear the word 'SMITY'.
## When it does, it spawns a new
## speech2text to hear the request

call_function(waitForWakeup)


# ------------------------------

# ------------------------------


def recognizeAndAct(userInput):
    import re

    def getSpotifyUsername():
        try:
            with open(os.path.join(PATH_TO_SETTINGS, 'settings.txt'), 'r') as f:
                for i in range(5):
                    line = f.readline()

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
        Text2Speech().speak('Are you sure you want to send an S.O.S signal ?')
        answer = listen()

        if answer.lower() == 'yes':
            return True
        else:
            return False

    key = intentRecognition(userInput)

    SPOTIFY_USERNAME = getSpotifyUsername()

    if key == 'addToQueueSpotify_Keywords':
        Text2Speech().speak('What is the title of the song you wish to add to queue?')
        songName = listen()
        if type(songName) == str:
            addToQueue(songName)
    elif key == 'alarmClock_Keywords':
        Text2Speech().speak('What time should the alarm go off?')
        hours = listen()
        if type(hours) == str:
            check_alarm_input(hours)
    elif key == 'artistFollowSpotify_Keywords':
        Text2Speech().speak('Which artist would you like to follow')
        artistName = listen()
        if type(artistName) == str:
            artistNameList = [artistName]
            artistFollow(artistNameList)
    elif key == 'artistUnfollowSpotify_Keywords':
        Text2Speech().speak('Which artist would you like to unfollow')
        artistName = listen()
        if type(artistName) == str:
            artistNameList = [artistName]
            artistUnfollow(artistNameList)
    elif key == 'calendar_make_event_Keywords':
        Text2Speech().speak('I am sorry, this is not available yet.')
        # make_event(date, time, description)

    elif key == 'calendar_Keywords':

        home_page_to_calendar('<Button-1>')

    elif key == 'calendar_showMeInRange_Keywords':
        Text2Speech().speak('I am sorry, this is not available yet.')

        # show_me_in_range(date1, date2)

    elif key == 'calendar_showMe_Keywords':
        Text2Speech().speak('I am sorry, this is not available yet.')

        # show_me(date)

    elif key == 'countDown_Keywords':
        Text2Speech().speak('What number would you like to count to')
        to = listen()
        if type(to) == str:
            to = int(re.search(r'\d+', to).group())
            call_function_wCommunication(countTo, to)

    elif key == 'countTo_Keywords':
        Text2Speech().speak('What number would you like to count down from')
        countDownFrom = listen()
        if type(countDownFrom) == str:
            countDownFrom = int(re.search(r'\d+', countDownFrom).group())
            call_function_wCommunication(countDown, countDownFrom)

    elif key == 'currencyConverter_Keywords':
        Text2Speech().speak('From what currency would you like to convert?')
        c1 = listen()
        Text2Speech().speak('What currency what would you like to convert to?')
        c2 = listen()
        Text2Speech().speak('What is the amount of ' + c1 + ' ?')
        amount = listen()
        if type(c1) == type(c2) == type(amount) == str:
            if c1 == 'dollar':
                c1 = 'United States Dollar'
            if c2 == 'dollar':
                c2 = 'United States Dollar'
            amount = int(re.search(r'\d+', amount).group())
            result = cconvert(c1, c2, amount)
            if type(result) == str:
                Text2Speech().speak(result)
    elif key == 'decryptFile_Keywords':
        Text2Speech().speak('What is the name of the file you want to decrypt ?')
        filename = listen()
        Text2Speech().speak('What is the password used to encrypt this file ?')
        aKey = listen()
        if type(filename) == type(aKey) == str:
            handleError(fileSecurity().decrypt(filename, aKey))

    elif key == 'decryptText_Keywords':
        Text2Speech().speak('What is the text you want to decrypt ?')
        cipherText = listen()
        Text2Speech().speak('What is the password used to encrypt this text ?')
        aKey = listen()
        if type(cipherText) == type(aKey) == str:
            decrypted = textSecurity().decrypt(cipherText, aKey='')
            if type(decrypted) == str:
                Text2Speech().speak(decrypted)

    elif key == 'deleteSavedAlbumsSpotify_Keywords':
        Text2Speech().speak('What is the name of the album you wish to delete ?')
        albumNameList = listen()
        if type(albumNameList) == str:
            handleError(deleteSavedAlbums(albumNameList))

    elif key == 'deleteSavedShowsSpotify_Keywords':
        Text2Speech().speak('What is the name of the show you wish to delete ?')
        showName = listen()
        if type(showName) == str:
            showNameList = [showName]
            handleError(deleteSavedShows(showNameList))
    elif key == 'deleteSavedTracksSpotify_Keywords':
        Text2Speech().speak('What is the name of the track you wish to delete ?')
        trackName = listen()
        if type(trackName) == str:
            trackNameList = [trackName]
            handleError(deleteSavedTracks(trackNameList))

    elif key == 'encryptFile_Keywords':
        Text2Speech().speak('What is the name of the file you wish to decrypt ?')
        filename = listen()
        Text2Speech().speak('What password would you like to use ?')
        aKey = listen()

        if type(filename) == type(aKey) == str:
            if aKey.lower() == 'no password':
                aKey = ''
            handleError(fileSecurity().encrypt(filename, aKey))

    elif key == 'encryptText_Keywords':
        Text2Speech().speak('What is the text you wish to decrypt ?')
        clearText = listen()
        Text2Speech().speak('What password would you like to use ?')
        aKey = listen()
        if type(clearText) == type(aKey) == str:
            if aKey.lower() == 'no password':
                aKey = ''
            encrypted = textSecurity().encrypt(clearText, aKey)
            if type(encrypted) is str:
                Text2Speech().speak(encrypted)

    elif key == 'facebookMessagesCount_Keywords':

        result = facebook_messages_count()
        if type(result) is str:
            Text2Speech().speak(result)
        else:
            handleError(result)

    elif key == 'forecastWeather_Keywords':
        Text2Speech().speak('For what city would you like to know the weather ?')
        city = listen()
        if type(city) == str:
            result = Forecast_weather_now(city)
            if type(result) is str:
                Text2Speech().speak(result)
            else:
                handleError(result)

    elif key == 'funFacts_Keywords':

        result = funFacts()
        if type(result) is str:
            Text2Speech().speak(result)
        else:
            handleError(result)

    elif key == 'getDate_Keywords':

        result = getDate()
        if type(result) == str:
            Text2Speech().speak(result)
        else:
            handleError(result)

    elif key == 'getTime_Keywords':

        result = getTime()
        if type(result) == str:
            Text2Speech().speak(result)
        else:
            handleError(result)

    elif key == 'get_news_Keywords':

        result = get_news()
        if type(result) == str:
            Text2Speech().speak(result)
        else:
            handleError(result)

    elif key == 'gmailRead_Keywords':

        result = show_emails()
        if type(result) == str:
            Text2Speech().speak(result)
        else:
            handleError(result)

    elif key == 'gmailSend_Keywords':
        Text2Speech().speak('What would you like the email to say ?')
        msg = listen()
        Text2Speech().speak("What would you like the email's subject to be ?")
        subject = listen()
        Text2Speech().speak('To whom should I send the email  ?')
        to = listen()

        if type(msg) == type(subject) == type(to) == str:
            result = create_send(msg, to, subject)
            if type(result) is str:
                Text2Speech().speak(result)
            else:
                handleError(result)

    elif key == 'googleMapsDirections_Keywords':
        Text2Speech().speak('Where would you like to go ?')
        destination = listen()
        Text2Speech().speak('From where would you like to go there ?')
        origin = listen()

        if type(destination) == type(origin) == str:
            result = googleMapsDirections(origin, destination)
            handleError(result)

    elif key == 'googleMapsSearch_Keywords':
        Text2Speech().speak('What would you like to search for in Google Maps ?')
        query = listen()
        if type(query) == str:
            handleError(googleMapsSearch(query))

    elif key == 'googleSearch_Keywords':
        Text2Speech().speak('What would you like to search for in Google Maps ?')
        query = listen()
        if type(query) == str:
            handleError(searching(query))

    elif key == 'instagramMessagesCount_Keywords':
        result = instagram_messages_count()
        if type(result) is str:
            Text2Speech().speak(result)
        else:
            handleError(result)


    elif key == 'jokes_Keywords':
        result = jokes()
        if type(result) is str:
            Text2Speech().speak(result)
        else:
            handleError(result)

    elif key == 'lockScreen_Keywords':

        lockScrnTimer(0)  # t=0 to lock instantly

    elif key == 'openProgram_Keywords':
        Text2Speech().speak('Which program should I open ?')
        program_name = listen()
        if type(program_name) == str:
            handleError(open_program(program_name))

    elif key == 'openUrls_Keywords':
        Text2Speech().speak('What url would you like me to open ?')
        url = listen()
        if type(url) == str:
            handleError(openUrl(url))

    elif key == 'open_news_page_Keywords':
        Text2Speech().speak('I am sorry, this is not available yet.')

        # open_news_page(title)
    elif key == 'pausePlaybackSpotify_Keywords':
        handleError(pausePlayback())

    elif key == 'photoCapture_Keywords':
        handleError(capturing())

    elif key == 'playAlbumSpotify_Keywords':
        Text2Speech().speak('What is the name of the album you would like to hear ?')
        name = listen()
        if type(name) == str:
            handleError(playAlbumOrPlaylist('album', name))

    elif key == 'playEpisodeSpotify_Keywords':
        Text2Speech().speak('What is the name of the episode you would like to hear ?')
        epName = listen()
        if type(epName) == str:
            handleError(playEpisode(epName))

    elif key == 'playlistAddTracksSpotify_Keywords':
        Text2Speech().speak('In which playlist would you like to add the song ?')
        playlistName = listen()
        Text2Speech().speak('What is the name of the song you would like to add ?')
        trackNameList = listen()

        if type(playlistName) == type(trackNameList) == str:
            handleError(playlistAddTracks(SPOTIFY_USERNAME, playlistName, trackNameList, '1'))

    elif key == 'playlistCreateSpotify_Keywords':
        Text2Speech().speak('What name would you like to give to your new playlist ?')
        playlistName = listen()
        if type(playlistName) == str:
            handleError(playlistCreate(SPOTIFY_USERNAME, playlistName, False, False, ''))

    elif key == 'playlistFollowSpotify_Keywords':
        Text2Speech().speak('What is the name of the playlist you like to follow ?')
        playlistName = listen()
        if type(playlistName) == str:
            handleError(playlistFollow(playlistName))

    elif key == 'playlistRemoveTracksSpotify_Keywords':
        Text2Speech().speak('Please, tell me the name of the playlist from which you would like to remove the track')
        playlistName = listen()
        Text2Speech().speak('What is the name of the track you would like to remove from this playlist ?')
        trackName = listen()
        if type(playlistName) == type(trackName) == str:
            trackNameList = [trackName]
            handleError(playlistRemoveTracks(playlistName, trackNameList))

    elif key == 'playlistUnfollowSpotify_Keywords':
        Text2Speech().speak('What is the name of the playlist you would like to unfollow ?')
        playlistName = listen()
        if type(playlistName) == str:
            handleError(playlistUnfollow(playlistName))

    elif key == 'playMusicLocal_Keywords':
        Text2Speech().speak('What is the name of the song you would like to listen ?')
        songName = listen()
        if type(songName) == str:
            songPath = getLocalMusicPath()
            handleError(playMusicLocal(songName, songPath))

    elif key == 'playMusicSpotify_Keywords':
        Text2Speech().speak('What is the name of the song you would like Spotidfy to play ?')
        songName = listen()
        if type(songName) == str:
            handleError(songbyTitle(songName, None))

    elif key == 'playNextSpotify_Keywords':
        handleError(playNext())

    elif key == 'playPlaylistSpotify_Keywords':
        Text2Speech().speak('What is the name of the playlist you would like to play ?')
        name = listen()
        if type(name) == str:
            handleError(playAlbumOrPlaylist('playlist', name))

    elif key == 'playPrevSpotify_Keywords':
        handleError(playPrev())

    elif key == 'playShowSpotify_Keywords':
        Text2Speech().speak('What is the name of the show that you would like to hear ?')
        showName = listen()
        if type(showName) == str:
            handleError(playShow(showName))

    elif key == 'playVideoLocal_Keywords':
        Text2Speech().speak('What is the name of the video you would like to watch ?')
        videoName = listen()
        if type(videoName) == str:
            videoPath = getLocalVideoPath()
            handleError(playVideoLocal(videoName, videoPath))
    elif key == 'repeatControlSpotify_Keywords':
        Text2Speech().speak('Repeat track, context or off ?')
        whatToRepeat = listen()
        if type(whatToRepeat) == str:
            if whatToRepeat.lower() not in ['track', 'context', 'off']:
                Text2Speech().speak('Invalid Value')
            else:
                handleError(repeatControl(whatToRepeat))

    elif key == 'restartDevice_Keywords':
        handleError(restartDevTimer(0))  # t=0 for instant restart

    elif key == 'resumePlaybackSpotify_Keywords':
        handleError(resumePlayback())

    elif key == 'saveAlbumsSpotify_Keywords':
        Text2Speech().speak('What is the name of the album you would like to save ?')
        albumName = listen()
        if type(albumName) == str:
            albumNameList = [albumName]
            handleError(saveAlbums(albumNameList))

    elif key == 'saveShowsSpotify_Keywords':
        Text2Speech().speak('What is the name of the show you would like to save ?')
        showName = listen()
        if type(showName) == str:
            showNameList = [showName]
            handleError(saveShows(showNameList))

    elif key == 'saveTracksSpotify_Keywords':
        Text2Speech().speak('What is the name of the track you would like to save ?')
        trackName = listen()
        if type(trackName) == str:
            trackNameList = [trackName]
            handleError(saveTracks(trackNameList))

    elif key == 'screenRecord_Keywords':
        handleError(screenRecord())

    elif key == 'screenshot_Keywords':
        handleError(screenshot())

    elif key == 'seekSpotify_Keywords':
        Text2Speech().speak('Which song would to like to skip to')
        whereTo = listen()
        if type(whereTo) == str:
            handleError(seek(whereTo))

    elif key == 'shuffleControlSpotify_Keywords':
        Text2Speech().speak('Would you like to activate shuffle ?')
        ans = listen()
        if type(ans) == str:
            if ans.lower() == 'yes':
                handleError(shuffleControl(True))
            elif ans.lower() == 'no':
                handleError(shuffleControl(False))
            else:
                Text2Speech().speak('Invalid Answer')

    elif key == 'shutdownDevice_Keywords':
        handleError(shutdownDevTimer(0))  # t = 0 for instant shutdown

    elif key == 'songsbyArtistSpotify_Keywords':
        Text2Speech().speak("What artist's songs would you like to play ?")
        Artist = listen()
        if type(Artist) == str:
            handleError(songsbyArtist(Artist))

    elif key == 'sosSignal_Keywords':
        if isSure():
            send_sos()
        else:
            Text2Speech().speak('Ok, I will not proceed')
    elif key == 'translateText_Keywords':
        Text2Speech().speak('I am sorry, this option is not supported yet.')

        # translateText(textToTranslate, lang)

    elif key == 'userFollowSpotify_Keywords':
        Text2Speech().speak('What is the name of the user you would like to follow ?')
        userName = listen()
        if type(userName) == str:
            userNameList = [userName]
            handleError(userFollow(userNameList))

    elif key == 'userUnfollowSpotify_Keywords':
        Text2Speech().speak('What is the name of the user you would like to unfollow ?')
        userName = listen()
        if type(userName) == str:
            userNameList = [userName]
            userUnfollow(userNameList)

    elif key == 'videoCapture_Keywords':
        videocap()

    elif key == 'volumeControlSpotify_Keywords':
        Text2Speech().speak('Which value should I set to the volume')
        volumeLevel = listen()
        if type(volumeLevel) == str:
            volumeLevel = int(re.search(r'\d+', volumeLevel).group())
            if 1 <= volumeLevel <= 100:
                handleError(volumeControl(volumeLevel))
            else:
                Text2Speech().speak('Invalid Value')

    elif key == 'wikipedia_Keywords':
        Text2Speech().speak('What would you like to search in Wikipedia ?')
        toSearch = listen()
        if type(toSearch) == str:
            handleError(Wiki_Search(toSearch))

    elif key == 'youtube_Keywords':
        Text2Speech().speak('What would you like to search in YouTube ?')
        toSearch = listen()
        if type(toSearch) == str:
            handleError(Youtube_Search(toSearch))

    else:
        return 7

    return 0



if __name__ == '__main__':
    pass
