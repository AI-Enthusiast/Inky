#!/bin/bash

# Navigate to the directory where your project is located
cd /home/pi/Code/Inky

# Pull the latest changes from your GitHub repository
git fetch
git checkout
git pull

# Initiate logging
run_date="$(date +'%Y-%m-%d--%H-%M')"
exec 2>> ~/home/pi/Code/Inky/log/logfile_parent_${run_date}.log

# Run the Python script and log the job run
time python3 __init__.py --color yellow 1>> ~/Code/Inky/log/logfile_${run_date}.log 2>> ~/Code/Inky/log/errfile_${run_date}.log


# run the script
# python3 __init__.py --color yellow