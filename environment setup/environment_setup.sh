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
REACT_APP_API_URL=http://your-api-url.com
REACT_APP_API_KEY=your-api-key
REACT_APP_OTHER_VARIABLE=your-other-variable
EOL

  echo "$filename created with example variables."
}

# Function to create a JSON configuration file
create_json_file() {
  local filename=$1
  local content=$2
  echo "Creating $filename"
  
  if [ -f "$filename" ]; then
    echo "$filename already exists. Overwriting..."
  fi

  echo "$content" > $filename

  echo "$filename created with specified content."
}

# Create .env.uat file
create_env_file ".env.uat"

# Create .env.prod file
create_env_file ".env.prod"

# Create Prettier configuration file
PRETTIER_CONFIG='{
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 100,
  "tabWidth": 2,
  "bracketSpacing": true,
  "bracketSameLine": false,
  "endOfLine": "auto"
}'
create_json_file ".prettierrc" "$PRETTIER_CONFIG"

# Create tsconfig.json file
TSCONFIG='{
  "compilerOptions": {
    "target": "ESNext",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ESNext"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": false,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "baseUrl": "./src"
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}'
create_json_file "tsconfig.json" "$TSCONFIG"

# Create tsconfig.node.json file
TSCONFIG_NODE='{
  "compilerOptions": {
    "composite": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}'
create_json_file "tsconfig.node.json" "$TSCONFIG_NODE"

# Install Prettier, env-cmd, and other dev dependencies
echo "Installing Prettier, env-cmd, and other dev dependencies"
npm install --save-dev prettier eslint eslint-config-prettier eslint-plugin-prettier env-cmd

echo "Prettier, env-cmd, and other dev dependencies installed successfully."

# Add scripts to package.json
echo "Adding scripts to package.json"
npx json -I -f package.json -e 'this.scripts["dev:uat"]="env-cmd -f .env.uat vite"'
npx json -I -f package.json -e 'this.scripts["dev:prod"]="env-cmd -f .env.prod vite"'
npx json -I -f package.json -e 'this.scripts["build:uat"]="env-cmd -f .env.uat vite build"'
npx json -I -f package.json -e 'this.scripts["build:prod"]="env-cmd -f .env.prod vite build"'

echo "Scripts added to package.json successfully."
echo "Environment variable files, Prettier configuration file, TypeScript configuration files, and package.json scripts setup completed."
