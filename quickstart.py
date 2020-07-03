#!/home/kaobe/Desktop/Programming_Projects/Inter-Language_Projects/Backup/venv/bin/python3.6

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload
import sys


 
def get_authentification():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file(serv,name):
    # Call the Drive v3 API
    file_metadata = {'name':name,'parents':["17ag2b22XaS_rMs7chtygS2QoDMktoAkH"]}
    media = MediaFileUpload("Backups/{}".format(name),mimetype='text/plain',chunksize=1024*1024*1,resumable=True)
    file = serv.files().create(body=file_metadata,media_body=media,fields='id').execute()
    return 1

def main(name):
    service = get_authentification()
    upload_file(service,name)
    print(name)
    return 1

if __name__ == '__main__':
    print(sys.argv[1])
    main(sys.argv[1])