import os
import time
import requests
import configparser
from inky import InkyWHAT
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansProSemibold

root = os.path.dirname(os.path.abspath('what_weather.py.py'))

config = configparser.ConfigParser()
config.read(root + '/what_weather/config.ini')
print(root + '/what_weather/config.ini')
print(config.sections())
print(config['LOCATION']['lat'])
print(config['LOCATION']['long'])

open_weather_api_key = '98e4a007bd3bde27d02a178913ba6a1f'
one_call = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + config['LOCATION']['lat'] \
           + '&lon=' + config['LOCATION']['long'] + '&appid=' + config['OW_API']['key']

def get_weather_data(rtn=False):
    update_time = time.time()
    # convert to 12 hour time and remove seconds and AM/PM and add space between hour and min
    update_time = datetime.fromtimestamp(update_time).strftime('%I:%M %p')[:-3]
    update_time = 'Last Updated: ' + update_time
    print(update_time)

    raw = requests.get(one_call)

    if raw.status_code != 200:
        print("Scrape Error")
        print(raw)
        raw.close()

    data = raw.json()
    raw.close()
    if rtn:
        return data
    else: # update global weather_data
        global weather_data
        weather_data=data

# weather_data = get_weather_data(True)


# ic(weather_data)


def get_sunset():
    sunset = weather_data['current']['sunset']
    sunset = datetime.fromtimestamp(sunset).strftime('%I:%M %p')
    return sunset


# ic(get_sunset())

def get_sunrise():
    sunrise = weather_data['current']['sunrise']
    sunrise = datetime.fromtimestamp(sunrise).strftime('%I:%M %p')

    return sunrise


# ic(get_sunrise())

def get_day_length():
    length_of_day = weather_data['current']['sunset'] - weather_data['current']['sunrise']
    length_of_day = time.strftime('%H:%M:%S', time.gmtime(length_of_day))[:-3]
    length_of_day_split = length_of_day.split(':')
    length_of_day = length_of_day_split[0] + ' hr ' + length_of_day_split[1] + ' min'
    return length_of_day


# ic(get_length_of_day())

def get_moon_rise():
    moon_rise = weather_data['daily'][0]['moonrise']
    moon_rise = datetime.fromtimestamp(moon_rise).strftime('%I:%M %p')
    return moon_rise


# ic(get_moon_rise())

def get_moon_set():
    moon_set = weather_data['daily'][0]['moonset']
    moon_set = datetime.fromtimestamp(moon_set).strftime('%I:%M %p')
    return moon_set


# ic(get_moon_set())

def get_moon_length():
    moon_length = weather_data['daily'][0]['moonrise'] - weather_data['daily'][0]['moonset']
    moon_length = time.strftime('%H:%M:%S', time.gmtime(moon_length))[:-3]
    moon_length_split = moon_length.split(':')
    # invert time, ie if time [12, 02] then [11, 58]
    moon_length_split[0], moon_length_split[1] = str(23 - int(moon_length_split[0])), str(
        60 - int(moon_length_split[1]))

    moon_length = moon_length_split[0] + ' hr ' + moon_length_split[1] + ' min'

    return moon_length


# ic(get_moon_length())

def get_current_weather_description():
    current_weather = weather_data['current']['weather'][0]['description']
    return current_weather


# ic(get_current_weather_description())

def get_current_weather_icon():  # fix this
    current_weather_icon = weather_data['current']['weather'][0]['icon']
    return current_weather_icon


def get_current_temp():
    current_weather_temp = weather_data['current']['temp']
    # current_weather_temp = round(current_weather_temp - 273.15, 1) # convert to celcius
    current_weather_temp = round((current_weather_temp - 273.15) * 9 / 5 + 32, 0)  # convert to fahrenheit
    return current_weather_temp


# ic(get_current_weather_temp())

def get_current_feels_like():
    current_feels_like = weather_data['current']['feels_like']
    # current_feels_like = round(current_feels_like - 273.15, 1) # convert to celcius
    current_feels_like = round((current_feels_like - 273.15) * 9 / 5 + 32, 0)  # convert to fahrenheit
    return current_feels_like


# ic(get_current_feels_like())

def get_current_humidity():
    current_humidity = weather_data['current']['humidity']
    return current_humidity


# ic(get_current_humidity())

def get_current_wind_speed():
    current_wind_speed = weather_data['current']['wind_speed']
    return current_wind_speed


# ic(get_current_wind_speed())

def get_current_wind_direction():
    current_wind_direction = weather_data['current']['wind_deg']
    # convert degrees to cardinal direction
    current_wind_direction = round(current_wind_direction / 22.5) % 16
    current_wind_direction = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                              'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'][current_wind_direction]
    return current_wind_direction


# ic(get_current_wind_direction())

def get_current_clouds():
    current_clouds = weather_data['current']['clouds']
    return current_clouds


# ic(get_current_clouds())


def interprate_pressure(pressure):
    if pressure <= 980:
        return "Very Low"
    elif pressure <= 1000:
        return "Low"
    elif pressure <= 1020:
        return "Moderate"
    elif pressure <= 1040:
        return "High"
    else:
        return "Very High"


def get_current_pressure():
    current_pressure = weather_data['current']['pressure']
    return interprate_pressure(current_pressure)


# ic(get_current_pressure())

def interprate_visibility(visibility):
    if visibility <= 1000:
        return "Very Low"
    elif visibility <= 3000:
        return "Low"
    elif visibility <= 6000:
        return "Moderate"
    elif visibility <= 9000:
        return "High"
    else:
        return "Very High"

def get_current_visibility():
    current_visibility = weather_data['current']['visibility']
    return interprate_visibility(current_visibility)


# ic(get_current_visibility())
def interprate_uv_index(uv_index):
    if uv_index <= 2:
        return "Low"
    elif uv_index <= 5:
        return "Moderate"
    elif uv_index <= 7:
        return "High"
    elif uv_index <= 10:
        return "Very High"
    else:
        return "Extreme"

def get_current_uv_index():
    current_uv_index = weather_data['current']['uvi']
    return interprate_uv_index(current_uv_index)


# ic(get_current_uv_index())

def get_current_dew_point():
    current_dew_point = weather_data['current']['dew_point']
    # current_dew_point = round(current_dew_point - 273.15, 1) # convert to celcius
    current_dew_point = round((current_dew_point - 273.15) * 9 / 5 + 32, 0)  # convert to fahrenheit
    return current_dew_point


# ic(get_current_dew_point())

def graph_weekly_temp():
    daily_temp, daily_time = [], []
    for i in range(0, 7):
        daily_temp.append(weather_data['daily'][i]['temp']['day'])
        daily_time.append(weather_data['daily'][i]['dt'])
    daily_temp = [round((x - 273.15) * 9 / 5 + 32, 0) for x in daily_temp]  # convert to fahrenheit
    daily_temp = [int(x) for x in daily_temp]
    daily_time = [datetime.fromtimestamp(x).strftime('%a') for x in daily_time]
    return daily_temp, daily_time


# ic(graph_weekly_temp())
# plt.plot(graph_weekly_temp()[1], graph_weekly_temp()[0])

def get_forecast():
    day, forecast, high, low, humidity = [], [], [], [], []
    for i in range(0, 7):
        forecast.append(weather_data['daily'][i]['weather'][0]['description'])
        day.append(datetime.fromtimestamp(weather_data['daily'][i]['dt']).strftime('%a'))
        high.append(weather_data['daily'][i]['temp']['max'])
        low.append(weather_data['daily'][i]['temp']['min'])
        humidity.append(weather_data['daily'][i]['humidity'])
        # convert from kelvin to fahrenheit
    high = [int(round((x - 273.15) * 9 / 5 + 32, 0)) for x in high]
    low = [int(round((x - 273.15) * 9 / 5 + 32, 0)) for x in low]

    return day, forecast, high, low, humidity

def read_csv(path):
    with open(path, 'r') as f:
        return f.read()

def graph_minutely_precip():
    minutely_precip, minutely_time = [], []
    for i in range(0, 60):
        minutely_precip.append(weather_data['minutely'][i]['precipitation'])
        minutely_time.append(weather_data['minutely'][i]['dt'])
    minutely_precip = [round(x * 0.0393701, 2) for x in minutely_precip]  # convert to inches
    minutely_time = [datetime.fromtimestamp(x).strftime('%I:%M %p') for x in minutely_time]
    return minutely_precip, minutely_time

def get_aqi_data():
    aqi_out = []
    aqi_data = {'pm10': [20, 50,100, 200, 250, 430],
                'pm2_5': [10, 25, 50, 75, 85, 95],
                'no2': [40,70,150, 200, 280, 400],
                'o3': [50, 100, 140, 180, 200, 400],
                'co': [4400,9400,12400,15400,18400,21400],
                'so2': [20,80,250,350,400,700],
                'nh3': [10,20,40,60,80,90],
                'level': ['good', 'fair', 'moderate', 'bad', 'very bad', 'severe'],
                'level_num': [1, 2, 3, 4, 5, 6]}
    aqi_url = 'http://api.openweathermap.org/data/2.5/air_pollution?lat=' + config['LOCATION']['lat'] \
              + '&lon=' + config['LOCATION']['long'] + '&appid=' + config['OW_API']['key']
    raw = requests.get(aqi_url)
    data = raw.json()
    raw.close()
    data = data['list'][0]['components']
    levels = aqi_data['level']
    total_aqi = 0
    for i in range(len(data)):
        cat = list(data.keys())[i]
        aqi = data[cat]
        bottom = -0.01 # bottom of the interval
        try:
            cat_range = aqi_data[cat]
            for j in range(len(cat_range)):
                top = cat_range[j] # top of the interval
                if bottom < aqi <= top: # if the aqi is in the interval
                    # print(cat + ': ' + levels[j]) # return the category
                    aqi_out.append(cat + ': ' + levels[j])
                    total_aqi += aqi_data['level_num'][j] # add the level number to the total
                bottom = top # update the bottom of the interval
        except KeyError: # skips no (nitrogen monoxide) because it's not in the aqi_data dict
            pass
    mean_aqi = total_aqi / len(aqi_out)
    return aqi_out, aqi_data['level'][int(mean_aqi - 1)]

def create_image(inky_display, color="black"):
    get_weather_data()

    sun_set                     = get_sunset()
    sun_rise                    = get_sunrise()
    moon_rise                   = get_moon_rise()
    moon_set                    = get_moon_set()
    moon_length                 = get_moon_length()
    day_length                  = get_day_length()
    current_weather_description = get_current_weather_description()
    current_weather_icon        = get_current_weather_icon()
    current_temp                = get_current_temp()
    current_feels_like          = get_current_feels_like()
    current_humidity            = get_current_humidity()
    current_wind_speed          = get_current_wind_speed()
    current_wind_direction      = get_current_wind_direction()
    current_clouds              = get_current_clouds()
    current_pressure            = get_current_pressure()
    current_visibility          = get_current_visibility()
    current_uv_index            = get_current_uv_index()
    current_dew_point           = get_current_dew_point()
    weekly_temps                = graph_weekly_temp()
    minutely_precip             = graph_minutely_precip()
    # eight_hour_forecast         = get_eight_hour_forcast()
    aqi_data, aqi_mean          = get_aqi_data()

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
    if color == "black":
        draw.text((10, 0), "Current Weather " + str(datetime.now()), inky_display.BLACK, font=font_small)
        draw.text((10, 10), str(int(current_temp)) + "°F", inky_display.BLACK,
                  font=font_xxlarge)  # big font for temp
    elif color == "yellow":
        draw.text((10, 0), "Current Weather " + str(datetime.now()), inky_display.YELLOW, font=font_small)
        draw.text((10, 10), str(int(current_temp)) + "°F", inky_display.YELLOW,
                  font=font_xxlarge)
    else:
        draw.text((10, 0), "Current Weather " + str(datetime.now()), inky_display.RED, font=font_small)
        draw.text((10, 10), str(int(current_temp)) + "°F", inky_display.RED,
                  font=font_xxlarge)

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
    return img
