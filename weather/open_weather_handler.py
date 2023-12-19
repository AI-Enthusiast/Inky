import os
# import shutil
import time
# import my_tools
import requests
import configparser
# import pandas as pd
# from icecream import ic
# from lxml import etree as et
from datetime import datetime
# from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt
# import schedule

root = os.path.dirname(os.path.realpath("../weather_bot.py"))
config = configparser.ConfigParser()
config.read('config.ini')
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


# ic(get_forecast())
# # forcast lows and highs on graph with day of week on x axis and temp on y axis
# forcast_plt = plt.plot(get_forecast()[0], get_forecast()[2], get_forecast()[0], get_forecast()[3], get_forecast()[4])
# forcast_plt = plt.legend(['High', 'Low', 'humidity'])
# plt.ylabel('Temperature (F)')
# plt.xlabel('Day of Week')
# plt.title('Weekly Forecast')
# # label each point with forecast and day of week
# for i in range(0, 7):
#     plt.annotate(get_forecast()[1][i], (get_forecast()[0][i], get_forecast()[2][i]))

def graph_minutely_precip():
    minutely_precip, minutely_time = [], []
    for i in range(0, 60):
        minutely_precip.append(weather_data['minutely'][i]['precipitation'])
        minutely_time.append(weather_data['minutely'][i]['dt'])
    minutely_precip = [round(x * 0.0393701, 2) for x in minutely_precip]  # convert to inches
    minutely_time = [datetime.fromtimestamp(x).strftime('%I:%M %p') for x in minutely_time]
    return minutely_precip, minutely_time


# ic(graph_minutely_precip())
# # if pecipitaiton is not always 0, plot it
# if graph_minutely_precip()[0] != [0] * 60:
#     plt.plot(graph_minutely_precip()[1], graph_minutely_precip()[0])


# def get_eight_hour_forcast():
#     hour, forecast, temp, humidity = [], [], [], []
#     for i in range(0, 8): # todo change this to maintain forcast till it changes (and is at lest 2 apart)
#         # provide forcast every 2, else empty string
#         if i % 2 == 0:
#             forecast.append(weather_data['hourly'][i]['weather'][0]['description'])
#         else:
#             forecast.append('')
#
#         # append hour in 12 hour format
#         hour.append(datetime.fromtimestamp(weather_data['hourly'][i]['dt']).strftime('%I %p'))
#         temp.append(weather_data['hourly'][i]['temp'])
#         humidity.append(weather_data['hourly'][i]['humidity'])
#         # convert from kelvin to fahrenheit
#     temp = [int(round((x - 273.15) * 9 / 5 + 32, 0)) for x in temp]
#     return hour, forecast, temp, humidity
# get_eight_hour_forcast()

# def get_eight_hour_forcast_png():
#     hour, forecast, temp, humidity = get_eight_hour_forcast()
#     pt = plt.figure(figsize=(3.5, 2), dpi=120)  # where 1 is 80 pixels and we want a 280x160 image
#     # reduce font size
#     plt.rcParams.update({'font.size': 6})
#     pt = plt.plot(hour, humidity, hour, temp)
#     pt = plt.ylabel('Humidity(%) and Temperature(F)')
#     pt = plt.xlabel('Time')
#     pt = plt.title('8 Hour Forcast', fontsize=8)
#     # label each point with forecast and time
#     for i in range(0, 8):
#         plt.annotate(forecast[i], (hour[i], temp[i]))
#
#     pt = plt.savefig(root + '/etc/weather/eight_hour_forcast_2.png')
#     # overlay humidity and temp
#     # humidity_plt = plt.plot(hour, humidity,
#     #                         hour, temp)
#     # humidity_plt = plt.legend(['Humidity', 'Temperature'])
#     # plt.ylabel('Humidity and Temperature')
#     # plt.xlabel('Time')
#     # plt.title('8 Hour Forcast')
#     # where 1 is 80 pixels and we want a 280x160 image
#     # plt.figure(figsize=(2, 3.5), dpi=120)
#
#     # save graph to file
#     # plt.savefig(root + '/etc/weather/eight_hour_forcast.png')


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
# print(get_aqi_data())