from .slideshow import create_image as create_slideshow_image


def display_slideshow(inky_display, display_color):
    print("Displaying slideshow")
    return create_slideshow_image(inky_display, display_color)
