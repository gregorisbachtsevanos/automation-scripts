import os
import shutil
from datetime import datetime, timedelta

# Folder paths
source_folder = "C:/Users/YourUser/Documents/Downloads"  # Source folder to organize
image_folder = "C:/Users/YourUser/Documents/Images"
doc_folder = "C:/Users/YourUser/Documents/Documents"
archive_folder = "C:/Users/YourUser/Documents/Archive"

# File types to move
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov"],
}

# Move files by extension
def move_files_by_type():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    category_folder = globals()[category.lower() + "_folder"]
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved {filename} to {category}")

# Archive old files
def archive_old_files():
    today = datetime.now()
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            last_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
            if today - last_modified > timedelta(days=180):  # files older than 6 months
                if not os.path.exists(archive_folder):
                    os.makedirs(archive_folder)
                shutil.move(file_path, os.path.join(archive_folder, filename))
                print(f"Archived {filename}")

# Main execution
move_files_by_type()
archive_old_files()
