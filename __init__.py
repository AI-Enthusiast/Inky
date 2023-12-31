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
choices = {"news": display_news, "wotd": display_wotd, "deviation": display_deviation,
           "weather": display_weather, "slideshow": display_slideshow, "quote": display_quote}
choice = random.choice(list(choices.keys()))
choices[choice](inky_display, color)

