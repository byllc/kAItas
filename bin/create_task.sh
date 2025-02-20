#!/bin/bash

# Check if the folder name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <folder_name>"
  exit 1
fi

FOLDER_NAME=$1

# Check if the folder name is valid (alphanumeric and underscores only)
if [[ ! "$FOLDER_NAME" =~ ^[a-zA-Z0-9_]+$ ]]; then
  echo "Error: Folder name '$FOLDER_NAME' is not valid. Use only alphanumeric characters and underscores."
  exit 1
fi

# Check if the folder already exists
if [ -d "$FOLDER_NAME" ]; then
  echo "Error: Folder '$FOLDER_NAME' already exists."
  exit 1
fi

# Create the folder
mkdir "$FOLDER_NAME"

# Create the required files
touch "$FOLDER_NAME/run.py"
touch "$FOLDER_NAME/README.md"
touch "$FOLDER_NAME/tests.py"
touch "$FOLDER_NAME/examples.py"

echo "Project folder '$FOLDER_NAME' created with run.py, README.md, tests.py, and examples.py."