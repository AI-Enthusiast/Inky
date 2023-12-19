# this script runs daily at [TBD]
# It downloads images from deviant art and saves them to a local folder that is dated
# It maintains the latest 3 days of images

import os
import uuid
import requests
from bs4 import BeautifulSoup
from datetime import datetime

root = os.path.dirname(os.path.realpath('jack_the_ripper.py'))
kill_date = 7  # days

# 1. get the date
date_current = datetime.date(datetime.now())


# 2. remove the oldest folder if it's more than 3 days old (/images/)
def remove_oldest_folder(date_curr):
    # get all folders in /images/
    folders = os.listdir('images')
    # if a folder is more than 3 days old, delete it
    for folder in folders:
        # skip .keep file
        if folder == '.keep':
            continue
        date_folder = datetime.date(datetime.strptime(folder, '%Y-%m-%d'))
        if (date_curr - date_folder).days > kill_date:
            # remove folder in /images/ and all its contents
            os.system('rm -rf images/' + folder)


# 3. create a new folder with the current date
def create_new_folder(date_curr):
    # check if a folder with the current date exists
    if os.path.exists('images/' + str(date_curr)):
        print('folder already exists: ' + str(date_curr))
        return

    # create a new folder in /images/
    os.mkdir('images/' + str(date_curr))
    print('created folder: ' + str(date_curr))


def get_challenge_word(soup_raw):
    word = soup_raw.find('h2', class_="_31Qjh").text
    return word


# img  src="https://images-wixmp
# get all img with src that starts with https://images-wixmp
def get_all_image_url(soup_raw):
    imgs = soup_raw.find_all('img', src=lambda x: x and x.startswith('https://images-wixmp'))
    return imgs


if __name__ == '__main__':
    # 4. download the images from deviant art
    url = "https://www.deviantart.com/dailychallenges"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    remove_oldest_folder(date_current)
    create_new_folder(date_current)
    challenge_word = get_challenge_word(soup)
    # new_url  = 'https://www.deviantart.com/tag/' + challenge_word + '?order=all-time'
    # page = requests.get(new_url)
    # soup = BeautifulSoup(page.content, 'html.parser')
    dl_count = 0
    for img in get_all_image_url(soup):
        img_url = img['src']

        # download the image
        img_data = requests.get(img_url).content

        # save the image
        with open(os.path.join(root, 'images', str(date_current),
                               challenge_word + "_" + str(uuid.uuid1()) + '.png'), 'wb') as handler:
            handler.write(img_data)
            dl_count += 1
    print('downloaded ' + str(dl_count) + ' images')
