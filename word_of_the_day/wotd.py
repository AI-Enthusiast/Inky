import requests
from bs4 import BeautifulSoup

# this script gets the word of the day
url = 'https://www.dictionary.com/e/word-of-the-day/'
raw = requests.get(url)
soup = BeautifulSoup(raw.content, 'html.parser')


# get word of the day
def get_word_of_the_day():
    word = soup.find('h1', class_="js-fit-text").text
    return word


# get pronunciation
def get_pronunciation():
    pronunciation = soup.find('span',
                              class_="otd-item-headword__pronunciation__text").text
    # remove brackets and empty space
    pronunciation = pronunciation.replace('[', '').replace(']', '').replace(' ', '').replace('\n', '')
    return pronunciation


# get part of speach
def get_part_of_speach():
    part_of_speach = soup.find('span', class_="luna-pos").text
    return part_of_speach

# get definition
def get_definition():
    definition = soup.find('div', class_="otd-item-headword__pos-blocks").text

    definition = definition.split('\n', 1)[1].replace(get_part_of_speach(), '').replace('\n', '')

    # find the first non blank space and remove everything before it
    for i in range(0, len(definition)):
        if definition[i] != ' ':
            definition = definition[i:]
            break

    return definition

