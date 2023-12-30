from .what_weather import create_image as create_weather_image


def display_weather(inky_display, display_color):
    img = create_weather_image(inky_display, display_color)
    img = img.rotate(180)  # flip the image so it's right side up
    inky_display.set_image(img)
    inky_display.show()