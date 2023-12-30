# choose a random folder from images then a random image from that folder
# diplay in on the inky display
from datetime import datetime
import random
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansProSemibold
import os

root = os.path.dirname(os.path.realpath("display_deviation.py"))

# 1. choose a random folder from images
def choose_random_folder():
    # get all folders in /images/
    folders = os.listdir('images')
    # choose a random folder
    folder = folders[random.randint(0, len(folders) - 1)]
    if folder == '.keep':
        return choose_random_folder()
    else:
        print('chose folder: ' + folder)
        return folder


# 2. choose a random image from that folder
def choose_random_image(folder):
    # get all images in the folder
    images = os.listdir(root + '/images/' + folder)
    # choose a random image
    image = images[random.randint(0, len(images) - 1)]
    print('chose image: ' + image)
    return image

# 3. display in on the inky display
def create_image(inky_display, color="black"):
    folder = choose_random_folder()
    image = choose_random_image(folder)

    inky_display.set_border(inky_display.WHITE)
    img = Image.open(root + '/images/' + folder + '/' + image)

    w, h = img.size
    ptype = ''
    # determin if imgage is portrait or landscape
    ptype = 'landscape' if w > h else 'portrait'

    if ptype == 'landscape':
        h_new = 300
        w_new = int((float(w) / h) * h_new)
        w_cropped = 400
        img = img.resize((w_new, h_new), resample=Image.LANCZOS)

        x0 = int((w_new - w_cropped) / 2)
        x1 = int(x0 + w_cropped)
        y0 = 0
        y1 = h_new
    else:
        w_new = 400
        h_new = int((float(h) / w) * w_new)
        h_cropped = 300
        img = img.resize((w_new, h_new), resample=Image.LANCZOS)

        x0 = 0
        x1 = w_new
        y0 = int((h_new - h_cropped) / 2)
        y1 = int(y0 + h_cropped)

    img = img.crop((x0, y0, x1, y1))

    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

    img = img.convert("RGB").quantize(palette=pal_img)

    # draw = ImageDraw.Draw(img)
    #
    # font_main = ImageFont.truetype(SourceSansProSemibold, 14)
    # challenge_word = image.split('_')[0]
    # draw.text((5, 5), challenge_word, inky_display.BLACK, font=font_main)

    return img