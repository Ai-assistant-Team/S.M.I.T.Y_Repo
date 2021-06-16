from __future__ import print_function
from Google import Create_Service
import time


def show_emails(Number_of_emails = 1):
##    Show a number of emails.
##
##    Args:
##        Number_of_emails:Numbers of emails that will be displayed
##
##    
    client_secret_file = 'credentials.json'

    api_name = 'gmail'

    api_version = 'v1'

    scopes = ['https://mail.google.com/']

##    Creating a connection.
##    
##    Variables : client_secret_file, api_name, api_version, scopes are needed in order to create a token 
##    therefore a service.
##    
##    

    services = Create_Service(client_secret_file, api_name, api_version, scopes)
    #Creates Google services

    results = services.users().messages().list(userId='me', labelIds=['INBOX'], maxResults = 20).execute()
    #Getting a number of emails from inbox.Limited to 20 in order not to overflow the system.

    messages = results.get('messages', [])
    #Storing the results to messages

    try:
        print('Messages:\n')
        for Number_of_emails in messages[:Number_of_emails]:

            msg = services.users().messages().get(userId='me', id=Number_of_emails['id']).execute()
            #Getting a specific message.

            print(msg['snippet'])
            #Snippet is a part of the entire message.

            print('\n')

            time.sleep(1)
        return 0

    except messages:
        return 1








