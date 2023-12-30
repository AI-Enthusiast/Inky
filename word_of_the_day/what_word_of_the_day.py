import os
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansProSemibold
from font_fredoka_one import FredokaOne
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


def creat_wotd_image(inky_display, color="black"):
    inky_display.set_border(inky_display.WHITE)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    font_small = ImageFont.truetype(SourceSansProSemibold, 12)
    font_main = ImageFont.truetype(SourceSansProSemibold, 14)
    font_large = ImageFont.truetype(SourceSansProSemibold, 18)
    font_xlarge = ImageFont.truetype(SourceSansProSemibold, 24)
    font_xxlarge = ImageFont.truetype(SourceSansProSemibold, 32)
    font_xxxlarge = ImageFont.truetype(FredokaOne, 38)

    root = os.path.dirname(os.path.realpath("what_word_of_the_day.py"))

    # 1. get the word of the day, pronunciation, and definition
    word = get_word_of_the_day().title()
    pronunciation = '[' + get_pronunciation() + ']'  # add brackets around pronunciation
    part_of_speach = get_part_of_speach()
    definition = get_definition()

    # 2. create the image to display, Word large at the top, then pronunciation, then definition
    ## 2.1. Word
    w, h = font_xxxlarge.getsize(word)
    x = 400 / 2 - w / 2
    y = 50 / 2 - h / 2
    # word is colored! Wow so fancy
    if color == "black":
        draw.text((x, y), word, inky_display.BLACK, font=font_xxxlarge)
    elif color == "yellow":
        draw.text((x, y), word, inky_display.YELLOW, font=font_xxxlarge)
    else:
        draw.text((x, y), word, inky_display.RED, font=font_xxxlarge)

    ## 2.2. Pronunciation (put on the left side)
    w, h = font_large.getsize(pronunciation)
    x = 10
    y = 100 / 2 - h / 2 + 25
    draw.text((x, y), pronunciation, inky_display.BLACK, font=font_large)

    ## 2.3. Part of speach (put on the right side)
    w, h = font_large.getsize(part_of_speach)
    x = 400 - w - 10
    y = 100 / 2 - h / 2 + 25
    draw.text((x, y), part_of_speach, inky_display.BLACK, font=font_large)

    ## 2.4. Definition (put on the right side)
    # for after 24 chars put a new line in the definition
    break_length = 35
    last_space = 0
    last_break = 0
    for i in range(0, len(definition)):
        if definition[i] == ' ':
            last_space = i
        if i - last_break > break_length:
            definition = definition[:last_space] + '\n' + definition[last_space + 1:]
            last_break = last_space
    w, h = font_main.getsize(definition)
    x = 10
    y = 200 / 2 - h / 2
    draw.text((x, y), definition, inky_display.BLACK, font=font_xlarge)

    return img
