from Google import Create_Service
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create_send(msg='',  to='', subject=''):
      """Show a number of emails.

          Args:
              msg :The message in a string format.
              to  :The email destination.
              subject :The subject of the specific email.

      """
      client_secret_file = 'credentials.json'

      api_name = 'gmail'

      api_version = 'v1'

      scopes = ['https://mail.google.com/']


      """Creating a connection.

          Variables : client_secret_file, api_name, api_version, scopes are needed in order to create a token 
          therefore a service.

      """
      services = Create_Service(client_secret_file, api_name, api_version, scopes)



      "Creating  a mimeMessage email object and converting it to a raw format in order to send it."

      emailmsg = msg

      mimeMessage = MIMEMultipart()

      mimeMessage['to'] = to

      mimeMessage['subject'] = subject

      mimeMessage.attach(MIMEText(emailmsg, 'plain'))

      raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

      message = services.users().messages().send(userId='me', body={'raw': raw_string}).execute()

      print('Your email has been sent')


