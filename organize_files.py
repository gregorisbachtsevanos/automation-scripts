import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]
            folder_name = os.path.join(directory, file_extension.upper())

            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            shutil.move(os.path.join(directory, filename), os.path.join(folder_name, filename))

    print("Files have been organized.")

if __name__ == "__main__":
    directory = input("Enter the path of the directory to organize: ")
    organize_files(directory)
