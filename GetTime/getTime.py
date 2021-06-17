from datetime import datetime


def getTime():

    try:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        return 0
    except :
        return 1
