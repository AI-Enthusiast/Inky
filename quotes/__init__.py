from .what_quotes import create_image as create_quotes_image


def display_quote(inky_display, display_color):
    print("Displaying quotes")
    img = create_quotes_image(inky_display, display_color)
    img = img.rotate(180)  # flip the image so it's right side up
    inky_display.set_image(img)
    inky_display.show()