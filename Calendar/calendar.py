import datetime
import pathlib

def make_event(date,time,description):
    try:
        date = get_date(date)
        if date.__contains__('of the event must in the present or in the future not in the past YOU IDIOT'):
            return date
        time = get_time(time,date)
        if time.__contains__('of the event must be between') or time.__contains__('Unless you time travel you can not schedule something in the past'):
            return time
        put_on_record(date)
        put_on_record(time)
        get_description(description)
        return 0
    except:
        return 1


def turn_text_to_date(users_input):
    try:
        #todays date
        todays_date_and_hour = datetime.datetime.now()
        date = [0,0,0000]
        date[0] = todays_date_and_hour.day
        date[1] = todays_date_and_hour.month
        date[2] = todays_date_and_hour.year

        if users_input == 'tomorrow':
            date[0] = date[0] +1
            return '/'.join([str(elem) for elem in date])
        elif users_input == 'the day after tomorrow':
            date[0] = date[0] +2
            return '/'.join([str(elem) for elem in date])
        return users_input
    except:
        return 1

def show_me(date):
    try:
        location = pathlib.Path(__file__).parent.absolute()
        events_found =''
        f = open("%s\\calendar_record.txt"%(location), "r")
        while 5>4:
            line = f.readline()
            if not line:
                break
            temp = date + '\n'
            if line == temp:
                events_found = events_found + line.replace("\n", " ")
                line = f.readline()
                events_found = events_found + line.replace("\n", " ")
                line = f.readline()
                events_found = events_found + line
        f.close()
        return events_found
    except :
        return 8

def show_me_in_range(date1,date2):
    try:
        events_found =''
        while 5>4:
            a =show_me(date1)
            if a == 1:
                return 8
            events_found = events_found +a
            if date1 == date2:
                break
            date1 = next_day(date1)
            if date1 == 1:
                return 1
        return events_found
    except:
        return 1
        
            
def next_day (date):
    try:
        date = date.split("/")
        date[0] = int (date[0])
        date[1] = int (date[1])
        date[2] = int (date[2])

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
        return '/'.join([str(elem) for elem in date])
    except :
        return 1



def put_on_record(something):
    try:
        location = pathlib.Path(__file__).parent.absolute()
        f = open("%s\\calendar_record.txt"%(location), "a+")
        f.write(something)
        f.write('\n')
        f.close()
        return 0
    except:
        return 9

def get_description(description):
    a = put_on_record(description)
    if a == 1:
        return 9

def get_date(date):
    try:
        #todays date
        todays_date_and_hour = datetime.datetime.now()
        #split
        date = date.split("/")
        #turn time from str to int
        day = int (date[0])
        month = int (date[1])
        year = int (date[2])
        print(str(todays_date_and_hour.year),' ',str(todays_date_and_hour.month),' ',str(todays_date_and_hour.day))
        print(str(year),' ',str(month),' ',str(day))
        #Check
        if todays_date_and_hour.year > year:
            return 'The year of the event must in the present or in the future not in the past YOU IDIOT'
        if todays_date_and_hour.year == year and todays_date_and_hour.month > month:
            return 'The month of the event must in the present or in the future not in the past YOU IDIOT'
        if todays_date_and_hour.year == year and todays_date_and_hour.month == month and todays_date_and_hour.day > day:
            return 'The day of the event must in the present or in the future not in the past YOU IDIOT'
        return '/'.join([str(elem) for elem in date])
    except:
        return 1
    

def get_time(time_of_the_event,date):
    try:
        date = date.split("/")
        #turn time from str to int
        day = int (date[0])
        month = int (date[1])
        year = int (date[2])
        #todays date and time
        todays_date_and_time = datetime.datetime.now()
        #split
        time_of_the_event = time_of_the_event.split(":")
        #str -> int
        hour = int( time_of_the_event[0])
        minutes = int( time_of_the_event[1])
        #check if hour if between 0 and 23 
        if hour >23 or hour <0:
            return 'The hour of the event must be between 0 and 24. YOU IDIOT'
        if minutes >59 or minutes <0:
            return 'The minutes of the event must be between 0 and 59. YOU IDIOT'
        if day== todays_date_and_time.day and month == todays_date_and_time.month and year== todays_date_and_time.year:
            if hour < todays_date_and_time.hour or (hour == todays_date_and_time.hour and minutes< todays_date_and_time.minute) :
                return 'Unless you time travel you can not schedule something in the past'
        return ':'.join([str(elem) for elem in time_of_the_event])
    except :
        return 1
