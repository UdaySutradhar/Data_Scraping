import argparse
import requests
import json
from geopy.geocoders import Nominatim

parser = argparse.ArgumentParser(description='Scrape weather data')

parser.add_argument('location', type=str, help='The location to get weather data for')
parser.add_argument('--description', action='store_true', help='Display the weather description')
parser.add_argument('--temp', action='store_true', help='Display the minimum and maximum temperature')
parser.add_argument('--humidity', action='store_true', help='Display the humidity')
parser.add_argument('--timezone', action='store_true', help='Display the timezone')
parser.add_argument('--unit', choices=['metric', 'imperial'], help='Unit system for temperature')
parser.add_argument('--forecast', type=int, metavar='DAYS', help='Number of days for weather forecast')
parser.add_argument('--history', type=str, metavar='DATE', help='Retrieve historical weather for a specific date (YYYY-MM-DD)')

args = parser.parse_args()

def get_weather_data(location):
    geolocator = Nominatim(user_agent='weather-scraper')
    location_data = geolocator.geocode(location)

    if location_data is None:
        print('Invalid location')
        return None

    lat = location_data.latitude
    lon = location_data.longitude

    api_key =  '907203e6a9bdef2ae66c76c1636d30d9'
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={lat},{lon}'
    response = requests.get(url)
    data = json.loads(response.text)

    return data

data = get_weather_data(args.location)

if args.description or args.temp or args.humidity or args.timezone or args.wind or args.precipitation:
    if data is None:
        print('Weather information not available')
    else:
        if args.description:
            if args.history:
                print(data['current']['weather_descriptions'][0])
            else:
                print(data['current']['weather_descriptions'][0])

        if args.temp:
            if args.history:
                if 'temperature' in data['current']:
                    temp = data['current']['temperature']
                    print(f'Temperature: {temp}°{data["request"]["unit"]} ({args.unit})')
                else:
                    print('Temperature information not available')
            else:
                temp_min = data['current']['temperature']
                temp_max = data['current']['temperature']
                print(f'Minimum temperature: {temp_min}°{data["request"]["unit"]} ({args.unit})')
                print(f'Maximum temperature: {temp_max}°{data["request"]["unit"]} ({args.unit})')

        if args.humidity:
            if args.history:
                if 'humidity' in data['current']:
                    humidity = data['current']['humidity']
                    print(f'Humidity: {humidity}%')
                else:
                    print('Humidity information not available')
            else:
                humidity = data['current']['humidity']
                print(f'Humidity: {humidity}%')

        if args.timezone:
            if 'timezone_id' in data['location']:
                timezone = data['location']['timezone_id']
                print(f'Timezone: {timezone}')
            else:
                print('Timezone information not available')
else:
    print('At least one option is required')
