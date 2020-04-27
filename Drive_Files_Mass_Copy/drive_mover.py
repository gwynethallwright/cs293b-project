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
    filenames = open('filenames.txt', 'r') 
    Lines = filenames.readlines() 
    
    count = 1
    # Strips the newline character 
    for line in Lines: 
        filename = line.strip()+".mkv"
        print(str(count) + " Starting for " + filename) 
        count = count + 1

        #find file_id from filename
        page_token = None
        while True:
            response = service.files().list(q="name=\'"+filename+"\'",
                                                spaces='drive',
                                                fields='nextPageToken, files(id, name)',
                                                pageToken=page_token).execute()
            for file in response.get('files', []):
                file_id = file.get('id')
                print("Found file")
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break        

        #download file from file_id to a temporary storage
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO("temp/"+filename, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download complete")
    

        #upload file to google drive folder
        folder_id = str(sys.argv[1])
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        media = MediaFileUpload("temp/"+filename,
                                mimetype='video/x-matroska',
                                resumable=True)
        file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id',
                                            supportsAllDrives=True).execute()

        print("Upload completed")

        #delete file from temporary folder
        if os.path.exists("temp/"+filename):
            os.remove("temp/"+filename)
            print("File deleted in local storage")
        else:
            print("The file does not exist")


if __name__ == '__main__':
    main()

