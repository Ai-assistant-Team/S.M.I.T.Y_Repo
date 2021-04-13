from datetime import date # imports the needed library

def theDate():
   # made by Γεωργία Βαλκάνη
   today = date.today()

   print("1.dd/mm/YY\n2.mm/dd/y\n3.Textual month, day and year\n4.Month abbreviation, day and year") # print the date forms


   while True:

      # <choose> is the prefence from the user for the date form
      choose = input("Choose the date form: ") # ask the form from the user

      if choose == "1": #Checks if answer is valid
         form1 = today.strftime("%d/%m/%Y")
         print("The date is =", form1)   # prints the given date form
         break

      elif choose == "2": #Checks if answer is valid
         form2 = today.strftime("%m/%d/%y")
         print("The date is =", form2) # prints the given date form
         break


      elif choose == "3": #Checks if answer is valid
         form3 = today.strftime("%B, %d %Y")
         print("The date is =", form3) # prints the given date form
         break

      elif choose == "4": #Checks if answer is valid
         form4 = today.strftime("%b-%d-%Y")
         print("The date is =", form4) # prints the given date form
         break


      else: # the answer is not valid
          print("Try again. Invalid command") # prints to try again
      # end of if
  # end of while
theDate()
# end of <timeDate>










