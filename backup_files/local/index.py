import os
import shutil
import datetime

def backup_files(source_dir, dest_dir):
    # Get current date and time for the backup folder name
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder_name = f"backup_{current_time}"
    backup_folder_path = os.path.join(dest_dir, backup_folder_name)

    # Create the backup directory
    if not os.path.exists(backup_folder_path):
        os.makedirs(backup_folder_path)

    # Copy files and directories from source to backup directory
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(backup_folder_path, item)
        
        if os.path.isdir(source_item):
            shutil.copytree(source_item, dest_item)
        else:
            shutil.copy2(source_item, dest_item)
    
    print(f"Backup completed successfully. Files are backed up to {backup_folder_path}")

if __name__ == "__main__":
    source_directory = r"C:\path\to\source"
    destination_directory = r"D:\path\to\backup"

    backup_files(source_directory, destination_directory)
