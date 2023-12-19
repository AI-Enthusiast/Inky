from datetime import datetime
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansProSemibold
import os
# import slack_handler
# import slack
# import time
# import requests
# import zipfile
# import matplotlib.pyplot as plt
# import numpy as np
import open_weather_handler

root = os.path.dirname(os.path.realpath("../weather_bot.py"))


def read_csv(path):
    with open(path, 'r') as f:
        return f.read()


def update():
    open_weather_handler.get_weather_data()

    sun_set                     = open_weather_handler.get_sunset()
    sun_rise                    = open_weather_handler.get_sunrise()
    moon_rise                   = open_weather_handler.get_moon_rise()
    moon_set                    = open_weather_handler.get_moon_set()
    moon_length                 = open_weather_handler.get_moon_length()
    day_length                  = open_weather_handler.get_day_length()
    current_weather_description = open_weather_handler.get_current_weather_description()
    current_weather_icon        = open_weather_handler.get_current_weather_icon()
    current_temp                = open_weather_handler.get_current_temp()
    current_feels_like          = open_weather_handler.get_current_feels_like()
    current_humidity            = open_weather_handler.get_current_humidity()
    current_wind_speed          = open_weather_handler.get_current_wind_speed()
    current_wind_direction      = open_weather_handler.get_current_wind_direction()
    current_clouds              = open_weather_handler.get_current_clouds()
    current_pressure            = open_weather_handler.get_current_pressure()
    current_visibility          = open_weather_handler.get_current_visibility()
    current_uv_index            = open_weather_handler.get_current_uv_index()
    current_dew_point           = open_weather_handler.get_current_dew_point()
    weekly_temps                = open_weather_handler.graph_weekly_temp()
    minutely_precip             = open_weather_handler.graph_minutely_precip()
    # eight_hour_forecast         = open_weather_handler.get_eight_hour_forcast()
    aqi_data, aqi_mean          = open_weather_handler.get_aqi_data()

    inky_display = InkyWHAT("black")
    inky_display.set_border(inky_display.WHITE)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    img = img.rotate(180)  # flip the image so it's right side up
    draw = ImageDraw.Draw(img)
    font_small = ImageFont.truetype(SourceSansProSemibold, 12)
    font_main = ImageFont.truetype(SourceSansProSemibold, 14)
    font_large = ImageFont.truetype(SourceSansProSemibold, 18)
    font_xlarge = ImageFont.truetype(SourceSansProSemibold, 24)
    font_xxlarge = ImageFont.truetype(SourceSansProSemibold, 32)

    # draw current tem in the top left corner, write 'current weather', with a timestamp
    draw.text((10, 0), "Current Weather " + str(datetime.now()), inky_display.BLACK, font=font_small)
    draw.text((10, 10), str(int(current_temp)) + "°F", inky_display.BLACK,
              font=font_xxlarge)  # big font for temp

    # # draw sunrise and sunset
    draw.text((160, 10), "Sunrise: " + sun_rise + " Sunset: " + sun_set, inky_display.BLACK,
              font=font_small)

    # draw moonrise and moonset
    draw.text((160, 20), "Moonrise: " + moon_rise + " Moonset: " + moon_set, inky_display.BLACK,
              font=font_small)

    # draw moon length and day length
    draw.text((70, 34),
              " Day Length: " + day_length + "Moon Length: " + moon_length.replace('\n', ''),
              inky_display.BLACK, font=font_main)

    # draw current weather description
    draw.text((70, 10), current_weather_description.title(), inky_display.BLACK, font=font_main)

    # draw current weather icon
    # draw.text((10, 180), current_weather_icon, inky_display.BLACK, font=font_main)

    # draw current feels like
    draw.text((70, 22), "Feels Like " + str(int(current_feels_like)) + "°",
              inky_display.BLACK, font=font_main)

    # draw current humidity
    draw.text((10, 46), "Humidity: " + str(current_humidity) + "%", inky_display.BLACK, font=font_main)

    # draw current wind speed
    draw.text((105, 46), "Wind Speed: " + str(current_wind_speed) + "km/h", inky_display.BLACK,
              font=font_main)

    # draw current wind direction
    draw.text((250, 46), "Direction: " + current_wind_direction, inky_display.BLACK, font=font_main)

    if current_clouds > 10:
        # draw current clouds
        draw.text((290, 70), "Clouds: " + str(current_clouds) + "%", inky_display.BLACK, font=font_main)

    # draw current pressure
    draw.text((10, 60), "Pressure: " + current_pressure, inky_display.BLACK, font=font_main)

    # draw current visibility
    draw.text((140, 60), "Visibility: " + current_visibility, inky_display.BLACK,
              # todo change to words
              font=font_main)

    # draw current uv index
    draw.text((280, 60), "UV Index: " + current_uv_index, inky_display.BLACK, font=font_main)

    # draw the aqi data, if it's not good then draw the aqi data. if it is good then draw the aqi mean
    if aqi_mean != 'good':
        i = 0
        for aqi_info in aqi_data:
            draw.text((10, 70 + i), aqi_info, inky_display.BLACK, font=font_main)
            i += 10
    else:
        draw.text((10, 70), 'AQI: ' + aqi_mean, inky_display.BLACK, font=font_main)
    # # draw eight_hour_forecast.png in the bottom left corner
    # eight_hour_forecast_img = Image.open(root + '/etc/weather/eight_hour_forcast_2.png')
    # img.paste(eight_hour_forecast_img, (0, 75))
    #
    # # display the image on the screen
    # inky_display.set_image(img)  # instead of drawing a png graph, pass the graph as an image array

    # # draw a graph using eight_hour_forecast.csv
    # import csv
    #
    # graph_csv = root + '/etc/weather/eight_hour_forecast.csv'
    # with open(graph_csv, 'r') as f:
    #     reader = csv.reader(f)
    #     graph_list = list(reader)
    #
    #
    # # print(graph_list) # eg: [['05 PM', '06 PM', '07 PM', '08 PM', '09 PM', '10 PM', '11 PM', '12 AM'], ['clear sky', '', 'clear sky', '', 'clear sky', '', 'scattered clouds', ''], ['77', '77', '74', '68', '60', '53', '52', '50'], ['46', '47', '52', '61', '70', '82', '90', '93']]
    #
    # # # Render plot image using matplotlib and pillow
    # def render_figure(wlist, width=inky_display.WIDTH, height=inky_display.HEIGHT, dpi=120):
    #     # graph_list is a list of lists, each list is a row of data containing 8 values, the lists are in order of time, weather description, temp, and humidity
    #     hour, humidity, hour, temp = wlist[0], wlist[3], wlist[0], wlist[2]
    #     pt = plt.figure(figsize=(width, height), dpi=dpi)
    #     plt.rcParams.update({'font.size': 6})  # reduce font size
    #     pt = plt.plot(hour, humidity, hour, temp)
    #     pt = plt.ylabel('Humidity % and Temp °F')
    #     pt = plt.xlabel('Time')
    #     pt = plt.title('8 Hour Forecast', fontsize=9)
    #
    #     for i in range(0, 8):  # overlay weather description text on temp line by hour
    #         plt.annotate(wlist[1][i], (hour[i], temp[i]), fontsize=6, ha='center', va='bottom', rotation=45)
    #
    #     # return fig
    #     pt.tight_layout()
    #     pt.canvas.draw()
    #     data = np.frombuffer(pt.canvas.tostring_rgb(), dtype=np.uint8)
    #     data = data.reshape(pt.canvas.get_width_height()[::-1] + (3,))
    #
    #     return Image.fromarray(data)
    #
    #
    # # Render plot image using matplotlib and pillow
    # graph_img = render_figure(graph_list)
    #
    # # Display image on Inky wHAT in the botom left corner
    # img.paste(graph_img, (0, 75))
    img = img.rotate(180)
    inky_display.set_image(img)

    inky_display.show()



if __name__ == "__main__":
    #get_weather_update()
    update()