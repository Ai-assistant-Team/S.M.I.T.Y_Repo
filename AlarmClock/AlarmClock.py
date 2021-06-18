

def check_alarm_input(hours = 0):
#Checks to see if the user has entered in a valid alarm time
    try:
        if hours < 24 and hours >= 0:

            insert_db(hours) #inserts the time in file hours.txt

            return 0


    except:

        return 1 #the time format was invalid



def insert_db(hours):
    try:
        f = open("hours.txt", "w") #opens file

        f.write(str(hours)) #rewrites and replaces all content with the variable hours

        f.close()
    except :
        return 9 #problem with file saving




