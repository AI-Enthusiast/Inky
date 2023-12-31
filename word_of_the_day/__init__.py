from .what_word_of_the_day import create_image as create_wotd_image


def display_wotd(inky_display, display_color):
    print("Displaying word of the day")
    img = create_wotd_image(inky_display, display_color)
    img = img.rotate(180)  # flip the image so it's right side up
    inky_display.set_image(img)
    inky_display.show()