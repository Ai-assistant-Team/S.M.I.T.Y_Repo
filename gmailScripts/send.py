"""
Created on Sat May 15
@author: Τάσος Παπαδόπουλος
"""
from Google import Create_Service
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create_send(msg='',  to='', subject=''):
##      Show a number of emails.
##
##          Args:
##              msg :The message in a string format.
##             to  :The email destination.
##              subject :The subject of the specific email.
##
##     
      client_secret_file = 'credentials.json'

      api_name = 'gmail'

      api_version = 'v1'

      scopes = ['https://mail.google.com/']


##          Creating a connection.
##
##          Variables : client_secret_file, api_name, api_version, scopes are needed in order to create a token 
##          therefore a service.
##
##      
      services = Create_Service(client_secret_file, api_name, api_version, scopes)
      #Creates



      #Creating  a mimeMessage email object and converting it to a raw format in order to send it.
      try:
            emailmsg = msg
            #assignes msg to emailmsg
            
            mimeMessage = MIMEMultipart()
            #makes mimeMessage a MIMEMultipart object
            
            mimeMessage['to'] = to
            #Takes variable to which is the mail receiver and assignes it to mimeMessage
            
            mimeMessage['subject'] = subject
            #Takes variable to which is the subject body and pass it to mimeMessage
            
            mimeMessage.attach(MIMEText(emailmsg, 'plain'))

            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
            #making the mimeMessage into a raw string in order to send it
            
            message = services.users().messages().send(userId='me', body={'raw': raw_string}).execute()
            #Send the mail to the user
            return 0

      except to:
            return 1


