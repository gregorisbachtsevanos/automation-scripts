#!/bin/bash

# ANSI color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to display messages in green color
print_success() {
  echo -e "${GREEN}$1${NC}"
}

# Function to display messages in red color
print_error() {
  echo -e "${RED}$1${NC}"
}

if [ -d "./public" ]; then
  echo "Deleting ./public directory and its contents..."
  rm -rf "./public"
  if [ $? -eq 0 ]; then
    print_success "./public directory and its contents deleted successfully."
  else
    print_error "Failed to delete ./public directory."
    exit 1
  fi
else
  print_success "./public directory does not exist. No need to delete."
fi

if [ -d "./views" ]; then
  echo "Deleting ./views directory and its contents..."
  rm -rf "./views"
  if [ $? -eq 0 ]; then
    print_success "./views directory and its contents deleted successfully."
  else
    print_error "Failed to delete ./views directory."
    exit 1
  fi
else
  print_success "./views directory does not exist. No need to delete."
fi