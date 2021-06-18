import datetime

def checkTime():
    try:
        f = open("hours.txt", "r")

        l = f.read(2)



        if (int(l) == datetime.datetime.now().hour) :
            print ("WAKE UP!")

            g = open("hours.txt", "w") #deletes everything in the file

            g.close()
        f.close()

    except OSError :
        return 8 #It could not open and read the file

