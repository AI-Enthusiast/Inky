from .what_news import create_image as create_news_image


def display_news(inky_display, display_color):
    print("Displaying news")
    img = create_news_image(inky_display, display_color)
    img = img.rotate(180)  # flip the image so it's right side up
    inky_display.set_image(img)
    inky_display.show()
