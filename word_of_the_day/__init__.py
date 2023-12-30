from .what_word_of_the_day import creat_wotd_image


def display_wotd(inky_display, display_color):
    img = creat_wotd_image(inky_display, display_color)
    img = img.rotate(180)  # flip the image so it's right side up
    inky_display.set_image(img)
    inky_display.show()