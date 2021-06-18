import datetime

def checkTime():
    try:


        with open("hours.txt", "r") as f:


            a = [a.strip() for a in f]

        s = []

        for x in a:
            s.append(int(x) - datetime.datetime.now().hour)


        min = 24

        for x in s:

            if int(x) < min and int(x)>=0 :
                min = int(x)



        p = []
        j = 0
        k = 0
        for x in s:

            if int(x) != 0:
                p.append(x)
                k += 1
            else:
                j += 1

        y=0

        for x in p:
            p[y] = int(x) + datetime.datetime.now().hour
            y += 1

        print(p)
        b=0
        if (min == 0) :
            print ("WAKE UP!")

            with open("hours.txt", "w") as txt_file:
                for line in p:
                    if b == 0:

                        txt_file.write(str(line) )

                    else:

                        txt_file.write( "\n" + "".join(str(line)) )
                    b += 1
                    if b == (k-j):
                        txt_file.close()
                        f.close()
                        break


            txt_file.close()
        f.close()

    except OSError :
        return 8 #It could not open and read the file


checkTime()
