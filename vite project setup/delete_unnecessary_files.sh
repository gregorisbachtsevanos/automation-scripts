#!/bin/bash

# Delete unnecessary file if it exists
if [ -f ".eslintrc.cjs" ]; then
  echo "Deleting .eslintrc.cjs file..."
  rm .eslintrc.cjs
  echo ".eslintrc.cjs file deleted successfully."
else
  echo ".eslintrc.cjs file not found. No need to delete."
fi

if [ -f "file_to_delete1.txt" ]; then
  echo "Deleting file_to_delete1.txt file..."
  rm file_to_delete1.txt
  echo "file_to_delete1.txt file deleted successfully."
else
  echo "file_to_delete1.txt file not found. No need to delete."
fi

if [ -f "file_to_delete2.js" ]; then
  echo "Deleting file_to_delete2.js file..."
  rm file_to_delete2.js
  echo "file_to_delete2.js file deleted successfully."
else
  echo "file_to_delete2.js file not found. No need to delete."
fi

# Add more deletion logic for other files as needed

echo "Deletion of specified files completed."
