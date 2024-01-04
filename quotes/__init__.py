from .what_quotes import create_image as create_quotes_image


def display_quote(inky_display, display_color):
    print("Displaying quotes")
    return create_quotes_image(inky_display, display_color)