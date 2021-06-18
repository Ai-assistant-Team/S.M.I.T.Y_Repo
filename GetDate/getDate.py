import datetime

def getDate():
    try:
        return(datetime.datetime.now().strftime("%d-%m-%Y "))
    except:
        return 1
