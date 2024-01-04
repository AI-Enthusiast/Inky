import os
from inky import InkyWHAT
from news import display_news
from word_of_the_day import display_wotd
from deviant_art import display_deviation
from usb_slideshow import display_slideshow
from weather import display_weather
from quotes import display_quote
import argparse
import random

# color options:
DISPLAY_COLORS = ["black", "red", "yellow"]
parser = argparse.ArgumentParser()
parser.add_argument('--color', '-c', type=str, required=False, choices=DISPLAY_COLORS, help="Display colour")
color = parser.parse_args().color
if color is None:
    color = "black"
# determin screen type (black, red, yellow)
inky_display = InkyWHAT(color)

# pick at random a news or word of the day
choices = {"news": display_news,
           "news2": display_news,
           "news3": display_news,
           "wotd": display_wotd,
           "deviation": display_deviation,
           "weather": display_weather,
           "slideshow": display_slideshow,
           "slideshow2": display_slideshow,
           "slideshow3": display_slideshow,
           "slideshow4": display_slideshow,
           "quote": display_quote,
           "quote": display_quote}
img = None
while img is None:
    choice = random.choice(list(choices.keys()))
    img    = choices[choice](inky_display, color)
img = img.rotate(180)  # flip the image so it's right side up
inky_display.set_image(img)
inky_display.show()
