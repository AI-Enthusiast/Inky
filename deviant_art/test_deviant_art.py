from inky import InkyWHAT
from what_deviation import create_image as create_deviation_image
import argparse

# color options:
DISPLAY_COLORS = ["black", "red", "yellow"]
parser = argparse.ArgumentParser()
parser.add_argument('--color', '-c', type=str, required=False, choices=DISPLAY_COLORS, help="Display colour")
color = parser.parse_args().color
if color is None:
    color = "black"


inky_display = InkyWHAT(color)
img = create_deviation_image(inky_display)
img = img.rotate(180)  # flip the image so it's right side up
inky_display.set_image(img)
inky_display.show()