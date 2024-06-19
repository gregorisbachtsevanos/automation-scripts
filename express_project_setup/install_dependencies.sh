#!/bin/bash

echo "Installing Dependencies"
npm install mongoose cors debug dotenv express prettier eslint eslint-config-prettier eslint-plugin-prettier env-cmd

echo "Installing development dependencies"
npm install --save-dev nodemon

echo "Dependencies and development dependencies installed successfully."
