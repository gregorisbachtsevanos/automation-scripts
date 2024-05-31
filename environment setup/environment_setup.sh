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
VITE_API_URL=http://your-api-url.com
VITE_API_KEY=your-api-key
VITE_OTHER_VARIABLE=your-other-variable
EOL

  echo "$filename created with example variables."
}

# Create .env.uat file
create_env_file ".env.uat"

# Create .env.prod file
create_env_file ".env.prod"

# Create Prettier configuration file
echo "Creating .prettierrc"
cat <<EOL > .prettierrc
{
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 100,
  "tabWidth": 2,
  "bracketSpacing": true,
  "bracketSameLine": false,
  "endOfLine": "auto"
}
EOL

echo ".prettierrc created with Prettier configuration."

# Install Prettier and other dev dependencies
echo "Installing Prettier and other dev dependencies"
npm install --save-dev prettier eslint eslint-config-prettier eslint-plugin-prettier

echo "Prettier and other dev dependencies installed successfully."

echo "Environment variable files created successfully."
