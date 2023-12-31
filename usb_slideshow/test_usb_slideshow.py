from inky import InkyWHAT
import argparse
from slideshow import create_image as create_slideshow_image

# color options:
DISPLAY_COLORS = ["black", "red", "yellow"]
parser = argparse.ArgumentParser()
parser.add_argument('--color', '-c', type=str, required=False, choices=DISPLAY_COLORS, help="Display colour")
color = parser.parse_args().color
if color is None:
    color = "black"
# determin screen type (black, red, yellow)
inky_display = InkyWHAT(color)

img = create_slideshow_image(inky_display, color)
img = img.rotate(180)  # flip the image so it's right side up
inky_display.set_image(img)
inky_display.show()