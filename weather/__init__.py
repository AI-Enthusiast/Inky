from .what_weather import create_image as create_weather_image


def display_weather(inky_display, display_color):
    print("Displaying weather")
    return create_weather_image(inky_display, display_color)
