import os
import datetime
from mega import Mega

def login_to_mega(email, password):
    mega = Mega()
    mega.login(email, password)
    return mega

def upload_to_mega(mega, local_file, mega_folder):
    print(f"Uploading {local_file} to MEGA folder {mega_folder}")
    mega.upload(local_file, mega_folder)
    print(f"Uploaded {local_file} to MEGA")

def backup_files_to_mega(source_dir, mega_folder, email, password):
    # Log in to MEGA
    mega = login_to_mega(email, password)
    
    # Create a backup folder in MEGA with the current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder_name = f"backup_{current_time}"
    folder = mega.create_folder(backup_folder_name, mega_folder)
    
    # Walk through the source directory and upload files
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            local_file_path = os.path.join(root, file)
            upload_to_mega(mega, local_file_path, folder[0])

if __name__ == "__main__":
    source_directory = r"C:\path\to\source"
    mega_folder = 'Root'  # Root or specify another folder if needed
    mega_email = 'your-mega-email@example.com'
    mega_password = 'your-mega-password'
    
    backup_files_to_mega(source_directory, mega_folder, mega_email, mega_password)
