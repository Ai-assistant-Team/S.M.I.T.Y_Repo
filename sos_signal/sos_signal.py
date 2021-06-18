import send

email = 'dai19078@uom.edu.gr'

# This method sends the email
def send_sos():
    try:
        send.create_send(create_msg(), email, 'Help!') #sends the sos email

        return 0 #all went good

    except:

        return 1 #there was a general error

# end of <send_sos()>

# This method is used to modify - get the message
def create_msg():
    try:
        msg = 'The situation is dire pls send help!!'

        return msg
    except:
        return 1
# end of <create_msg()>

# This is the main method that confirms if the user wish to continue
# and send the sos message to his contacts
