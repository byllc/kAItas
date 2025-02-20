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

# Add the shebang line to the run.py file
echo "#!/usr/bin/env python3" > "$FOLDER_NAME/run.py"
# Add the shebang line to the tests.py file
echo "#!/usr/bin/env python3" > "$FOLDER_NAME/tests.py"
echo "import unittest" >> "$FOLDER_NAME/tests.py"

# make files executable 
chmod +x "$FOLDER_NAME/run.py"
chmod +x "$FOLDER_NAME/tests.py"


echo "Project folder '$FOLDER_NAME' created with run.py, README.md, tests.py, and examples.py."