import os
import shutil

# Define the source directory and the target directories
source_dir = '/path/to/source'
image_dir = '/path/to/Photos'
document_dir = '/path/to/Documents'
music_dir = '/path/to/Music'

# Create target directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(document_dir, exist_ok=True)
os.makedirs(music_dir, exist_ok=True)

# Define file type associations
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Music': ['.mp3', '.wav']
}

# Function to move files based on their extension
def move_files():
    for filename in os.listdir(source_dir):
        file_ext = os.path.splitext(filename)[1].lower()
        src_path = os.path.join(source_dir, filename)
        
        if file_ext in file_types['Images']:
            shutil.move(src_path, os.path.join(image_dir, filename))
        elif file_ext in file_types['Documents']:
            shutil.move(src_path, os.path.join(document_dir, filename))
        elif file_ext in file_types['Music']:
            shutil.move(src_path, os.path.join(music_dir, filename))

move_files()
