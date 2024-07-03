import os
import pickle
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate_drive_api():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('drive', 'v3', credentials=creds)
    return service

def create_drive_folder(service, folder_name, parent_folder_id):
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_folder_id] if parent_folder_id else []
    }
    file = service.files().create(body=file_metadata, fields='id').execute()
    return file.get('id')

def upload_to_drive(service, local_file, drive_folder_id):
    file_metadata = {
        'name': os.path.basename(local_file),
        'parents': [drive_folder_id]
    }
    media = MediaFileUpload(local_file, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Uploaded {local_file} to Drive, file ID: {file.get('id')}")

def backup_files_to_drive(source_dir, parent_drive_folder_id=None):
    service = authenticate_drive_api()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder_name = f"backup_{current_time}"
    backup_folder_id = create_drive_folder(service, backup_folder_name, parent_drive_folder_id)
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            local_file_path = os.path.join(root, file)
            upload_to_drive(service, local_file_path, backup_folder_id)

if __name__ == "__main__":
    source_directory = r"C:\path\to\source"
    parent_drive_folder_id = None  # Specify parent folder ID if needed, else None for root
    backup_files_to_drive(source_directory, parent_drive_folder_id)
