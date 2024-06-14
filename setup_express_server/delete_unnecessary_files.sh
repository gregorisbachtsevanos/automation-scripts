#!/bin/bash

# Delete unnecessary file if it exists
if [ -f "./bin/www" ]; then
  echo "Deleting www file..."
  rm www
  echo "www file deleted successfully."
else
  echo "www file not found. No need to delete."
fi

if [ -f "./views/index.js" ]; then
  echo "Deleting index.js file..."
  rm index.js
  echo "index.js file in router dir deleted successfully."
else
  echo "index.js file file in router dir not found. No need to delete."
fi

if [ -f "./views/users.js" ]; then
  echo "Deleting users.js file..."
  rm users.js
  echo "users.js file in router dir deleted successfully."
else
  echo "users.js file in router dir not found. No need to delete."
fi

if [ -f "./app.js" ]; then
  echo "Deleting file_to_delete1.txt file..."
  rm file_to_delete1.txt
  echo "file_to_delete1.txt file deleted successfully."
else
  echo "file_to_delete1.txt file not found. No need to delete."
fi

echo "Deletion of specified files completed."
