#!/bin/bash

# ANSI color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the absolute path to the directory containing the index.sh script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Variable to track setup status
SETUP_SUCCESS=true
ERROR_LOG=""

# Function to display messages in green color
print_success() {
  echo -e "${GREEN}$1${NC}"
}

# Function to display messages in red color
print_error() {
  echo -e "${RED}$1${NC}"
}

# Execute each script with error handling
execute_script() {
  local script_name="$1"
  local description="$2"
  if [ "$SETUP_SUCCESS" = true ]; then
    print_success "Executing $description..."
    if ! bash "$script_name"; then
      print_error "Error executing $description"
      SETUP_SUCCESS=false
      ERROR_LOG+="Error executing $description\n"
      print_error "Setup was not completed successfully. Please check the logs for errors."
      exit 1  # Exit the script if an error occurs
    fi
  else
    ERROR_LOG+="Error executing $description\n"
  fi
}

# Execute each script
execute_script "$SCRIPT_DIR/delete_unnecessary_files.sh" "delete_unnecessary_files.sh"
execute_script "$SCRIPT_DIR/create_env_files.sh" "create_env_files.sh"
execute_script "$SCRIPT_DIR/create_config_files.sh" "create_config_files.sh"
execute_script "$SCRIPT_DIR/install_dependencies.sh" "install_dependencies.sh"
execute_script "$SCRIPT_DIR/add_scripts_to_packagejson.sh" "add_scripts_to_packagejson.sh"
execute_script "$SCRIPT_DIR/create_directory_structure.sh" "create_directory_structure.sh"
execute_script "$SCRIPT_DIR/create_store_and_api_files.sh" "create_store_and_api_files.sh"

if [ "$SETUP_SUCCESS" = true ]; then
  print_success "Setup completed successfully."
fi
