#!/bin/bash

# Navigate to the directory where your project is located
cd /home/pi/Code/Inky

# Pull the latest changes from your GitHub repository
git fetch
git checkout
git pull

# Install or update project requirements from requirements.txt
#pip install -r requirements-what-weather.txt

# # Initiate logging
# run_date="$(date +'%Y-%m-%d')"
# exec 2>> ~/home/pi/Code/Metropolis/source/log/logfile_parent_${run_date}.log # write stderr to a log file
#
# # Run the Python script and log the job run
# time python ~/home/pi/Code/Metropolis/source/what_weather/what_weather.py 1>> ~/home/pi/Code/Metropolis/source/what_weather/log/logfile_${run_date}.log 2>> ~/home/pi/Code/Metropolis/source/what_weather/log/errfile_${run_date}.lo

# run the script
python3 __init__.py --color black