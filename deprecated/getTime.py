from datetime import datetime # imports the needed library
# made by Γεωργία Βαλκάνη

while True:

    Q = input("Want to know the time? Yes or No: ")  # Checks if user wants to know time
    if Q == "Yes":  # Checks if answer is "Yes" or "No"
        def time():  # if answer is "Y"

            now = datetime.now()
            time_is = now.strftime("%H:%M:%S")
            print("The time now is =", time_is)  # prints the time

        time()
        break

        # end of <time>
    elif Q == "No" :
        print("Have a good day")  # prints a message if user dont want to know time
        break
    else:
         print("Invalid command.")

    # end of if

#end of while
