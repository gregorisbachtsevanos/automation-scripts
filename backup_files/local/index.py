import os
import shutil
from datetime import datetime

# Define the source and backup directories
source_dir = '/path/to/source'
backup_dir = '/path/to/backup'

# Create a timestamped backup directory
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
target_dir = os.path.join(backup_dir, f'backup_{timestamp}')
os.makedirs(target_dir, exist_ok=True)

# Function to perform the backup
def backup_files():
    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(target_dir, filename)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)

backup_files()
