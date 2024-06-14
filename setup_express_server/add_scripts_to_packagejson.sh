#!/bin/bash

# Add scripts to package.json
echo "Adding scripts to package.json"
npx json -I -f package.json -e 'this.scripts["dev"]="nodemon ./bin/www.js --ignore client"'

echo "Scripts added to package.json successfully."
