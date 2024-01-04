import bs4 as BeautifulSoup
from PIL import Image
import requests
import os

def create_image(inky_display, color="black"):
    start_url = 'https://darebee.com/'
    r = requests.get(start_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    daily_exercise = soup.find('div', id='exercise')
    daily_exercise_url = daily_exercise.find('a')['href'] # daily/january-4-2024.html
    # exract the date from the url
    date = daily_exercise_url.split('/')[-1].split('.')[0].split('-')
    date_str = date[0] + ' ' + date[1] + ' - ' + date[2]
    url = start_url + daily_exercise_url

    r = requests.get(url, allow_redirects=True)
    open(date_str + '.gif', 'wb').write(r.content) # save gif

    im = Image.open(date_str + '_gif.gif')     # open gif
    im.save(date_str + '_png.png')             # save as png
    im2 = Image.open(date_str + '_png.png')    # open png
    rgb_im = im2.convert('RGB')                # convert to rgb
    rgb_im.save(date_str + '_jpg.jpg')         # save as jpg
    img = Image.open(date_str + '_jpg.jpg')    # open jpg

    inky_display.set_border(inky_display.WHITE)
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