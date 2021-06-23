import time  # library to slow the system in order to count in a specific speed


def countTo(conn, to, countFrom=1, speed="Normal"):  # 3 variables

    try:
        while countFrom <= to:
            if speed == "Normal":  # if the speed is set to "Normal" the scrip counts every one second
                conn.send(str(countFrom))
                time.sleep(1)
                countFrom += 1
            elif speed == "Slow":  # if the speed is set to "Slow" the scrip counts every two seconds
                conn.send(str(countFrom))
                time.sleep(2)
                countFrom += 1
            elif speed == "Fast":  # if the speed is set to "Fast" the scrip counts every three seconds
                conn.send(str(countFrom))
                time.sleep(0.5)
                countFrom += 1
        conn.send(None)
        conn.close()
        return 0
    except:
        conn.close()
        return 1


# function to count down from a number to 1. The default number to count down to is 1 but the user can
# switch it and start counting down to another number. He can also choose a speed to count down. The default speed
# is "Normal" but he can choose between "Fast" or "Slow".Any other words for speed wont be accepted.

def countDown(conn, countDownFrom, countDownTo=1, speed="Normal"):
    try:
        while countDownFrom >= countDownTo:
            if speed == "Normal":  # if the speed is set to "Normal" the scrip counts down every one second
                conn.send(str(countDownFrom))
                time.sleep(1)
                countDownFrom -= 1
            elif speed == "Slow":  # if the speed is set to "Slow" the scrip counts down every two seconds
                conn.send(str(countDownFrom))
                time.sleep(2)
                countDownFrom -= 1
            elif speed == "Fast":  # if the speed is set to "Fast" the scrip counts every three seconds
                conn.send(str(countDownFrom))
                time.sleep(0.5)
                countDownFrom -= 1
        conn.send(None)
        conn.close()
        return 0
    except:
        conn.close()
        return 1



