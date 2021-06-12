import datetime
from Calendar import get_description
from Calendar import get_date
from Calendar import get_time
from Calendar import put_on_record
from Calendar import show_me_in_range
from Calendar import show_me
from Calendar import turn_text_to_date

def test():
    description_of_the_event = input ('What do you have to do? ')
    #date
    date_of_the_event = input('Whene is this event is going to happen ? D/M/Y ')
    date = get_date(date_of_the_event)
    while date == 'The year of the event must in the present or in the future not in the past YOU IDIOT' or date == 'The month of the event must in the present or in the future not in the past YOU IDIOT' or date == 'The day of the event must in the present or in the future not in the past YOU IDIOT':
        print(date)
        date_of_the_event = input('Whene is this event is going to happen ? D/M/Y ')
        date = get_date(date_of_the_event)
    #time
    time_of_the_event = input('What time is this event is going to happen ? HH:MM ')
    time = get_time(time_of_the_event,date)
    while time == 'The hour of the event must be between 0 and 24. YOU IDIOT' or time == 'The minutes of the event must be between 0 and 59. YOU IDIOT' or time == 'Unless you time travel you can not schedule something in the past':
        print(time)
        time_of_the_event = input('What time is this event is going to happen ? HH:MM ')
        time = get_time(time_of_the_event,date)

    put_on_record(date)
    put_on_record(time)
    get_description(description_of_the_event)
    

#test()
print(show_me_in_range('4/4/4444','7/4/4444'))
p = input("enter to exit")