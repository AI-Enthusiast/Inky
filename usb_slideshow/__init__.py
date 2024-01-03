from .slideshow import create_image as create_slideshow_image


def display_slideshow(inky_display, display_color):
    print("Displaying slideshow")
    img = create_slideshow_image(inky_display, display_color)
    if img is None:
        print('no image found')
        return None # todo move img diplay portion to og init
    img = img.rotate(180)  # flip the image so it's right side up
    inky_display.set_image(img)
    inky_display.show()