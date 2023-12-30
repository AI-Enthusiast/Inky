from inky import InkyWHAT
from what_weather import create_image as create_weather_image
inky_display = InkyWHAT(color)
img = create_weather_image(inky_display)
img = img.rotate(180)  # flip the image so it's right side up
inky_display.set_image(img)
inky_display.show()