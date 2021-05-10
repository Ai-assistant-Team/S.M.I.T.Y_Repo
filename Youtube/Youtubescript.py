import webbrowser                                                                                   # importing webbrowser module

##
## This function is searching youtube the video you want
##

def Youtube_Search(toSearch):                                                                       # declaring a function
    try:                                                                                            # using Exception Handling to avoid unprecedented errors
        return(webbrowser.open('https://www.youtube.com/results?search_query=' + toSearch))         # it searches a youtube video of what you typed
    except:                                                                                         # printing the error message
        print('An unknown error occured')
