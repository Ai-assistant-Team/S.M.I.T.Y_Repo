from datetime import datetime


def getTime():

    try:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        return 0
    except :
        return 1

    
    #we have imported datetime class from the datetime module.
    #Then, we used now() method to get a datetime object containing current date and time.
    #Using datetime.strftime() method, we created a string representing current time.
