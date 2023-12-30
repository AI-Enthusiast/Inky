from .display_deviation import create_image as create_deviation_image


def display_deviation(inky_display, display_color):
    img = create_deviation_image(inky_display, display_color)
    img = img.rotate(180)  # flip the image so it's right side up
    inky_display.set_image(img)
    inky_display.show()