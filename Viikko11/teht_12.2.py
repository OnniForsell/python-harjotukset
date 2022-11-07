import json
import requests


def string_to_float(convertable_object):
    i = 0
    cut_string = convertable_object
    list_of_degrees = []
    while i < len(cut_string):
        if cut_string[i].isdigit() or cut_string[i] == ".":
            only_necessary = cut_string[i]
            list_of_degrees.append(only_necessary)
        i += 1
    convertable_string = ' '.join(list_of_degrees)
    spaces_removed = convertable_string.replace(" ", "")
    degrees_in_float = float(spaces_removed)
    return degrees_in_float


def get_latitude(place):
    geo_codes = (f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=2&appid={API_key}")
    data = requests.get(geo_codes).json()
    get_lat_formatted = json.dumps(data)
    index_of_lat = get_lat_formatted.find('"lat":')
    lat_ends_index = get_lat_formatted.find(' "lon": ')
    cut_string = get_lat_formatted[index_of_lat:lat_ends_index]
    latitude = string_to_float(cut_string)
    return latitude


def get_longitude(place):
    geo_codes = (f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=2&appid={API_key}")
    data = requests.get(geo_codes).json()
    get_lon_formatted = json.dumps(data)
    index_of_lon = get_lon_formatted.find('"lon":')
    lon_ends_index = get_lon_formatted.find(' "country":')
    cut_string = get_lon_formatted[index_of_lon:lon_ends_index]
    longitude = string_to_float(cut_string)
    return longitude


def get_weather_desc(lat, lon):
    get_places_weather = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric")
    weather = requests.get(get_places_weather).json()
    desc = weather["weather"]
    description = desc[0]["description"]
    return description


def get_the_weather(lat, lon):
    get_places_weather = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric")
    weather = requests.get(get_places_weather).json()
    degrees = weather["main"]["temp"]
    celsius = degrees
    return round(celsius, 2)


city = input("Input the name of a city: ")
API_key = ("55f0162a334513bf7549f2464d869580")

latitude = get_latitude(city)
longitude = get_longitude(city)

celsius = get_the_weather(latitude, longitude)
desc = get_weather_desc(latitude, longitude)
print(f"The weather in {city} is {desc}")
print(f"It's {celsius} C\u00B0 in {city} right now.")