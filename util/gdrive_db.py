import time
import io
import base64
import json
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Decode the service account JSON from the .env variable
service_account_json = os.getenv("SERVICE_ACCOUNT_JSON")
db_path = os.getenv("DB_PATH")
google_drive_file_id = os.getenv("GDRIVE_FILE_ID")

decoded_json = base64.b64decode(service_account_json).decode("utf-8")

# Parse JSON and create credentials
credentials_info = json.loads(decoded_json)
credentials = service_account.Credentials.from_service_account_info(credentials_info)

# Initialize the Google Drive API client
drive_service = build('drive', 'v3', credentials=credentials)

# Function to download the database file from Google Drive
def download_database():
    request = drive_service.files().get_media(fileId=google_drive_file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print("Download database from Google Drive: %d%%." % int(status.progress() * 100))
    with open(db_path, 'wb') as f:
        f.write(fh.getbuffer())

# Function to replace the list.db file on Google Drive
def replace_list_db_on_google_drive():
    media = MediaFileUpload(db_path, resumable=True)
    drive_service.files().update(fileId=google_drive_file_id, media_body=media).execute()
    
    print('list.db file on Google Drive has been updated.')

# Function to periodically replace list.db on Google Drive
def start_replacing():
    while True:
        replace_list_db_on_google_drive()
        time.sleep(600)  # Sleep for 600 seconds before the next update
