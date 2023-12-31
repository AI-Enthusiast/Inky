# navigate to /media/ and check for usb drives
# if found, check for images (jpg) and display them
import os
import random
from PIL import Image, ImageFont, ImageDraw

# find drive
def get_drive():
    drives = os.listdir('/media/')
    # return random drive
    drive_choice = random.choice(drives)
    print('chose drive: ' + drive_choice)
    return drive_choice

# find image
def get_image(drive):
    images = os.listdir('/media/' + drive)
    # return random image
    image_choice = random.choice(images)
    print('chose image: ' + image_choice)
    return image_choice

def create_image(inky_display, color=black):
    drive = get_drive()
    image = get_image(drive)

    inky_display.set_border(inky_display.WHITE)
    img = Image.open('/media/' + drive + '/' + image)

    w, h = img.size
    ptype = ''
    # determin if imgage is portrait or landscape
    ptype = 'landscape' if w >= h else 'portrait'

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

    return img