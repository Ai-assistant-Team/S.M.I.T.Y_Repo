import datetime

def getDate():
    try:
        print (datetime.datetime.now().strftime("%d-%m-%Y "))

        return 0
    except:
        return 1
