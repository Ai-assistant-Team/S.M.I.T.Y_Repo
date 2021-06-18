import os

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
        f = open("hours.txt", "a") #opens file

        if os.stat("hours.txt").st_size == 0 :

            f.write(str(hours))

        else :

            f.write("\n" + str(hours)) #rewrites and replaces all content with the variable hours

        f.close()
    except :
        return 9 #problem with file saving


check_alarm_input(20)

f = open("hours.txt", "r")
print(f.read())
f.close()