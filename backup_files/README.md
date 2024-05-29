## Google Drive
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

Set Up Google Drive API:

Go to the Google Cloud Console.
Enable the Google Drive API.
Create OAuth 2.0 credentials and download the credentials.json file.


Certainly! Here's a Python script to back up files from a local directory to Google Drive using the Google Drive API. This example will use the google-auth, google-auth-oauthlib, google-auth-httplib2, and google-api-python-client libraries.

Prerequisites
Google Account: You need a Google account.
Google Drive API: Enable the Google Drive API in your Google Cloud Console.
OAuth 2.0 Credentials: Set up OAuth 2.0 credentials and download the credentials.json file.
Install Required Libraries: Install the required Python libraries using pip:
sh
Copy code
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
Backup Script to Google Drive
Here's the script that uploads files from a local directory to Google Drive:

python
Copy code
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
Instructions to Use the Script
Set Up Google Drive API:

Go to the Google Cloud Console.
Enable the Google Drive API.
Create OAuth 2.0 credentials and download the credentials.json file.
Install Libraries:

sh
Copy code
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
Run the Script:

Save the script to a file, for example, backup_to_drive.py.
Ensure you have the credentials.json file in the same directory as your script.
Open Command Prompt or Terminal.
Navigate to the directory where backup_to_drive.py is saved.
Run the script by typing python backup_to_drive.py and pressing Enter.
Explanation
Authenticate and Create the Drive Service:

The script uses OAuth 2.0 to authenticate with Google Drive.
Credentials are stored in token.pickle for reuse.
Create a Backup Folder:

The script creates a new folder in Google Drive with the current date and time as its name.
Upload Files:

The script walks through the source directory and uploads each file to the backup folder in Google Drive.
Additional Considerations
Security: Store your credentials.json file securely and do not hardcode sensitive information in the script.
Error Handling: Add error handling to manage cases where the upload fails or the Google Drive API is not accessible.
Incremental Backups: Implement checks to upload only new or modified files to avoid re-uploading unchanged files.

## Mega Drive

pip install mega.py

Configure the Script:

source_directory: Path to the directory you want to back up.
mega_folder: The folder in your MEGA account where you want to upload the files (use 'Root' for the root directory).
mega_email: Your MEGA account email.
mega_password: Your MEGA account password.
Run the Script:

Save the script to a file, for example, backup_to_mega.py.
Open Command Prompt or Terminal.
Navigate to the directory where backup_to_mega.py is saved.
Run the script by typing python backup_to_mega.py and pressing Enter.
Explanation
mega.py Library: This library provides an easy way to interact with the MEGA API.
Login to MEGA: The login_to_mega function logs into your MEGA account using your email and password.
Create Backup Folder: The script creates a backup folder in your MEGA account with the current date and time.
Upload Files: The script walks through the source directory and uploads each file to the backup folder on MEGA.
Additional Considerations
Security: For security reasons, do not hardcode your MEGA credentials in the script. Instead, use environment variables or a configuration file to store them securely.
Error Handling: You may want to add error handling to manage cases where the upload fails or the MEGA API is not accessible.
Incremental Backups: To avoid re-uploading unchanged files, consider implementing checks to upload only new or modified files.
