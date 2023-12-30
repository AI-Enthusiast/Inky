#!/bin/bash

# Navigate to the directory where your project is located
cd /home/pi/Code/Inky

# Pull the latest changes from your GitHub repository
git fetch
git checkout
git pull

# run the script
python3 __init__.py --color red