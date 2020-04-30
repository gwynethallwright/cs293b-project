from __future__ import print_function
import pickle
import os
import io
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
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


    # Using readlines() 
    old_filenames = open('filenames.txt', 'r') 
    Lines = old_filenames.readlines() 
    contains_humans = []
    for line in Lines: 
        old_filename = line.strip()+".mkv"
        contains_humans.append(old_filename)

    count = 0
    doesnt_contain_humans = open("doesnt_contain_humans.txt", "w")
    search_term = "createdTime > '2020-04-06T07:00:00' and createdTime < '2020-04-12T23:00:00' and mimeType contains 'video/'"
    #find file_id from filename
    page_token = None
    while True:
        response = service.files().list(q=search_term,
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=page_token).execute()
        
        for file in response.get('files', []):
            file_name = file.get('name')
            if(file_name not in contains_humans):
                if(file_name.startswith("FARM1")):
                    hr_of_video = int(file_name[24:26])
                    #check for videos taken during daylight
                    if((hr_of_video > 7) and (hr_of_video < 17)):
                        print(count," Found file with name ",file_name)
                        doesnt_contain_humans.write(file_name[:-4]+"\n")
                        count = count + 1
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break    
    
    doesnt_contain_humans.close()    

        


if __name__ == '__main__':
    main()
