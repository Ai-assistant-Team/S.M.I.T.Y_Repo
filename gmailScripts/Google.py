import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

"""This file's purpose is to create a token via authenticating to google's api client.
"""


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    """Searching for a pre existing token,if not found in the current folder it creates it.

        Args:
            client_secret_file :Numbers of emails that will be displayed.
            api_version : The version of the api currently the version is 1.
            api_name : The name of the api.
            scopes : The privileges provided from google to us.


        """
#  print(client_secret_file, api_name, api_version, scopes, sep='-')

    scopes = [scope for scope in scopes[0]]


    cred = None

    pickle_file = f'token_{api_name}_{api_version}.pickle'
    print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
            cred = flow.run_local_server(port=0)

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_name, api_version, credentials=cred)
        print(api_name, 'service created successfully')
        return service

    except scopes:
        return 2

    except ConnectionError:
        return 10

    except Exception as e:
        return 1

