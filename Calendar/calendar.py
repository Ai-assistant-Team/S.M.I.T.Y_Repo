import datetime
from event import Event

def get_time(time, day):
    #get time from user
    time_of_the_event = input("What time this event is going to happen ? ")
    time_of_the_event = time_of_the_event.split(":")
    time_of_the_event[0] = int( time_of_the_event[0])
    time_of_the_event[1] = int( time_of_the_event[1])
    #check if hour if between 0 and 23 
    while time_of_the_event[0] >23 or time_of_the_event[0] <0:
        print (" Από 0 έως 23 ώρες πάει ρε βλακα! άντε βάλε τη σωστή ώρα")
        time_of_the_event[0] = input ("Give the hour of the event: ")
    #check if minutes if between 0 and 59
    while time_of_the_event[1] >59 or time_of_the_event[1] <0:
        print (" Από 0 έως 59 ώρες πάει ρε βλακα! άντε βάλε τη σωστή ώρα")
        time_of_the_event[0] = input ("Give the minutes of the event: ")
    if day == "today":
    # if the event is today check the the user gives a time after the present time
        while time[0] > time_of_the_event[0] or (time[1] > time_of_the_event[1] and time[0] == time_of_the_event[0] ):
            time_of_the_event = input("Unless you can travel to the past give a future time ")
            time_of_the_event = time_of_the_event.split(":")
            time_of_the_event[0] = int( time_of_the_event[0])
            time_of_the_event[1] = int( time_of_the_event[1])
    #replace current time with the time of the event
    time[0] = time_of_the_event[0]
    time[1] = time_of_the_event[1]



def tomorrow(date):
    if date[0] < 28  :
        #if the date is before 27 of the month add 1 day
        date[0] = date[0] +1
    elif date[1] == 2:
        #if the month is february
        if date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0):
            #if february has 29 days
            if date[0] < 29:
                date[0] = date[0] +1
            elif date[0] == 29:
                date[0] = 1
                date[1] = 3
        else:
            #if february has 28 days
            if date[0] == 28:
                date[0] = 1
                date[1] = 3
    elif date[1] == 4 or date[1] == 6 or date[1] == 9 or date[1] == 11:
        #if the month has 30 days
        if date[0] < 30:
            date[0] = date[0] +1
        else:
            date[0] = 1
            date[1] = date[1] +1
    elif date[1] == 1 or date[1] == 3 or date[1] == 5 or date[1] == 7 or date[1] == 8 or date[1] == 10 or date[1] == 12:
        #if month has 31 days
        if date[0] < 31:
            date[0] = date[0] +1
        elif date[0] == 31 and date[1] < 12:
            date[0] = 1
            date[1] = date[1] +1
        elif date[0] == 31 and date[1] == 12:
            #if the year changes
            date[0] = 1
            date[1] = 1
            date[2] = date[2] +1


def the_day_after_tomorrow(date):
    if ( date[0] < 27 ) :
        #if the date is before 27 of the month add 2 days
        date[0] = date[0] +2
    elif date[1] == 2:
        #if the month is february
        if date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0):
            #if february has 29 days
            if date[0] == 27:
                date[0] = date[0] +2
            elif date[0] == 28:
                date[0] = 1
                date[1] = 3
            elif date[0] == 29:
                date[0] = 2
                date[1] = 3
        else:
            #if February has 28 days
            if date[0] == 27:
                date[0] = 1
                date[1] = 3
            elif date[0] == 28:
                date[0] = 2
                date[1] = 3
    elif date[1] == 4 or date[1] == 6 or date[1] == 9 or date[1] == 11:
        #if the month has 30 days
        if date[0] < 29:
            date[0] = date[0] +2
        elif date[0] == 29:
            date[0] = 1
            date[1] = date[1] +1
        elif date[0] == 30:
            date[0] = 2
            date[1] = date[1] +1
    elif date[1] == 1 or date[1] == 3 or date[1] == 5 or date[1] == 7 or date[1] == 8 or date[1] == 10 or date[1] == 12:
        #if the month has 31 days
        if date[0] < 30:
            date[0] = date[0] +2
        elif date[0] == 30 and date[1] < 12:
            date[0] = 1
            date[1] = date[1] +1
        elif date[0] == 30 and date[1] == 12:
            #if the year ends
            date[0] = 1
            date[1] = 1
            date[2] = date[2] +1
        elif date[0] == 31 and date[1] < 12:
            date[0] = 2
            date[1] = date[1]+1
        elif date[0] == 31 and date[1] == 12:
            #if the year changes
            date[0] = 2
            date[1] = 1
            date[2] = date[2] +1


def today(date, time):
    #get the time from user
    get_time(time,"today")
    #create and add the event to the list of Events
    listOfEvents.append(Event(date[2],date[1],date[0],time[0],time[1],description))

def create_event(listOfEvents):

    #Present Time
    time = datetime.datetime.now()
    time = time.strftime("%H:%M")
    time = time.split(":")
    #turn time from str to int
    time[0] = int( time[0])
    time[1] = int( time[1])

    #Present day - Month - Year
    date = datetime.datetime.now()
    date = date.strftime("%d-%m-%Y")
    date = date.split("-")
    #turn time from str to int
    date[0] = int (date[0])
    date[1] = int (date[1])
    date[2] = int (date[2])

    description = input ("What do you have to do? ")
    whene_is_the_event_happening = input("Whene is this event is going to happen ?")
    if whene_is_the_event_happening == "today":
        today(date, time)
    elif whene_is_the_event_happening == "tomorrow":
            tomorrow(date)
            get_time(time,"tomorrow")
            listOfEvents.append(Event(date[2],date[1],date[0],time[0],time[1],description))
    elif whene_is_the_event_happening == "the day after tomorrow":
        the_day_after_tomorrow(date)
        #get_time(time,"the day after tomorrow")
        listOfEvents.append(Event(date[2],date[1],date[0],time[0],time[1],description))
        #get secific date from user
    else:
        whene_is_the_event_happening = whene_is_the_event_happening.split("-")
        whene_is_the_event_happening[0] = int (whene_is_the_event_happening[0])
        whene_is_the_event_happening[1] = int (whene_is_the_event_happening[1])
        whene_is_the_event_happening[2] = int (whene_is_the_event_happening[2])
        #check if the date that the user gave is today
        if whene_is_the_event_happening[0] == date [0] and whene_is_the_event_happening[1] == date [1] and whene_is_the_event_happening[2] == date [2]:
            today(date, time)
        else:
            specific_date ( whene_is_the_event_happening,date, time)
            listOfEvents.append(Event(whene_is_the_event_happening[2],whene_is_the_event_happening[1],whene_is_the_event_happening[0],time[0],time[1],description))




def specific_date (whene_is_the_event_happening,date, time):

     #if the user gives a specific date check that the date is in the future not in the past
    while(whene_is_the_event_happening[2] < date[2] ):
        whene_is_the_event_happening[2] = input ("the year of the event must the present year or in the future ")
        whene_is_the_event_happening[2] = int(whene_is_the_event_happening[2])
    while(whene_is_the_event_happening[1] < date[1] and whene_is_the_event_happening[2] == date[2]  ):
        whene_is_the_event_happening[1] = input ("the month of the event must the present year or in the future ")
        whene_is_the_event_happening[1] = int(whene_is_the_event_happening[1])
    while(whene_is_the_event_happening[0] < date[0] and whene_is_the_event_happening[1] == date[1] and whene_is_the_event_happening[2] == date[2] ):
        whene_is_the_event_happening[0] = input ("the day of the event must the present year or in the future ")
        whene_is_the_event_happening[0] = int(whene_is_the_event_happening[0])

    get_time(time,"date")
    

def show_me(comand , listOfEvents):

    #Present Time
    time = datetime.datetime.now()
    time = time.strftime("%H:%M")
    time = time.split(":")
    #turn time from str to int
    #hour
    time[0] = int( time[0])
    #minutes
    time[1] = int( time[1])

    #Present day - Month - Year
    date = datetime.datetime.now()
    date = date.strftime("%d-%m-%Y")
    date = date.split("-")
    #turn time from str to int
    #Year
    date[0] = int (date[0])
    #month
    date[1] = int (date[1])
    #day
    date[2] = int (date[2])

    if comand == "show me my tasks for today":
        for x in listOfEvents:
            if x.day == date[0] and x.month == date[1] and x.year == date[2] and ( x.hour > time[1] or (x.hour == time[1] and x.minutes >= time[2])):
                print(x.year,x.month,x.day,x.hour, x.minutes, x.description)
    elif comand == "show me my tasks for tomorrow":
        tomorrow(date)
        for x in listOfEvents:
            if x.day == date[0] and x.month == date[1] and x.year == date[2] :
                print(x.year,x.month,x.day,x.hour, x.minutes, x.description)
    elif comand == "show me my tasks for the day after tomorrow":
        the_day_after_tomorrow(date)
        for x in listOfEvents:
            if x.day == date[0] and x.month == date[1] and x.year == date[2] :
                print(x.year,x.month,x.day,x.hour, x.minutes, x.description)
    
    


def test2(listOfEvents):
    listOfEvents.append(Event(2021,12,5,5,50,"ddd"))
    listOfEvents.append(Event(2020,3,2,6,00,"ffff"))
    listOfEvents.append(Event(2021,4,2,7,22,"rrrr"))
    listOfEvents.append(Event(2020,4,4,11,30,"wwwww"))


def test():
    listOfEvents = []
    #create_event(listOfEvents)
    test2(listOfEvents)
    for x in listOfEvents:
        print(x.year,x.month,x.day,x.hour, x.minutes, x.description)
    print("----------------------------")
    show_me("show me my tasks for the day after tomorrow" , listOfEvents)

test()
p = input("enter to exit")





    
