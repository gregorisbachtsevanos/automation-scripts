# Instructions to Use the Script
### Install Python
Ensure Python is installed on your Windows system. You can download it from python.org.

### Edit Script Paths
Modify the source_directory and destination_directory variables in the script to reflect the actual paths you want to use for the source and backup locations.

### Run the Script
Save the script to a file, for example, backup_script.py.
Open Command Prompt.
Navigate to the directory where backup_script.py is saved.
Run the script by typing python backup_script.py and pressing Enter.

## Explanation
### Libraries Used:

os: To handle directory operations.\
shutil: To copy files and directories.\
datetime: To generate a timestamp for the backup folder.

### Backup Process:
The script creates a new backup folder in the destination directory with the current date and time as its name.
It iterates over all items in the source directory and copies each file and directory to the new backup folder.
shutil.copytree() is used for copying directories and their contents.
shutil.copy2() is used for copying files along with their metadata.
