import SMITY.urlHandling.openUrls

##
## This function is searching youtube the video you want
##


def Youtube_Search(toSearch):  # declaring a function
    try:  # using Exception Handling to avoid unprecedented errors

        return SMITY.urlHandling.openUrls.openUrl('https://www.youtube.com/results?search_query=' + toSearch)  # it searches a youtube video of what you typed

    except Exception:
        return 1  # 1 : Undefined Error

# end of youtubeScript
