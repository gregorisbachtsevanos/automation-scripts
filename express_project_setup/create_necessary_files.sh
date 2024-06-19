#!/bin/bash

# Function to create an env file and add variables
create_env_file() {
  local filename=$1
  echo "Creating $filename"
  
  if [ -f "$filename" ]; then
    echo "$filename already exists. Overwriting..."
  fi

  cat <<EOL > $filename
# Environment variables for $filename
DB_ACCESS=
SERVER_URL = http://localhost:4000
PORT = 4000
EOL

  echo "$filename created with example variables."
}

# Create .env.uat file
create_env_file ".env.uat"

# Create .env.prod file
create_env_file ".env.prod"

CONST='import * as dotenv from 'dotenv'
dotenv.config()

export const DB_ACCESS = process.env.DB_ACCESS

export const SERVER_URL = process.env.SERVER_URL

export const PORT = process.env.PORT
'

create_json_file "constants.ts" "$CONST"

echo "Constants file created successfully."


echo "Environment variable files created successfully."
