import os
from news import display_news
from word_of_the_day import display_wotd
from inky.auto import auto
import argparse
import random

# color options:
DISPLAY_COLORS = ["black", "red", "yellow"]
parser = argparse.ArgumentParser()
parser.add_argument('--color', '-c', type=str, required=False, choices=DISPLAY_COLORS, help="Display colour")
color = parser.parse_args().color
# determin screen type (black, red, yellow)
inky_display = auto(ask_user=True, verbose=True)

# pick at random a news or word of the day
choices = {"news": display_news, "wotd": display_wotd}
choice = random.choice(list(choices.keys()))
choices[choice](inky_display, color)

