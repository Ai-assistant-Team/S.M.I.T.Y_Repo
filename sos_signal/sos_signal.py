import gmail

email = 'dai19078@uom.edu.gr'

# This method sends the email
def send_sos():
    gmail.send.create_send(create_msg(), email, 'Help!')
# end of <send_sos()>

# This method is used to modify - get the message
def create_msg():
    msg = 'The situation is dire pls send help!!'

    return msg
# end of <create_msg()>

# This is the main method that confirms if the user wish to continue
# and send the sos message to his contacts
def confirmation():
    response = False

    print('Are you sure you want to send the SOS message?')

    val = input('Are you sure you want to send the SOS message? Type Yes or No: ')

    # Checks if the user typed replied Yes or No
    if val == 'Yes':
        response = True
    # end of if

    # only if response = True then the message is going to be send
    if response:
        send_sos()
    # end of if

# end of <confirmation()>

confirmation()