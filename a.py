import argparse
import requests
import json
from geopy.geocoders import Nominatim

# Create the parser
parser = argparse.ArgumentParser(description='Scrape weather data')

# Add the location argument
parser.add_argument('location', type=str, help='The location to get weather data for')

# Add the options
parser.add_argument('--description', action='store_true', help='Display the weather description')
parser.add_argument('--temp', action='store_true', help='Display the minimum and maximum temperature')
parser.add_argument('--humidity', action='store_true', help='Display the humidity')
parser.add_argument('--timezone', action='store_true', help='Display the timezone')

# Parse the arguments
args = parser.parse_args()

def get_weather_data(location):
    # Get the latitude and longitude using geocoding
    geolocator = Nominatim(user_agent='weather-scraper')
    location_data = geolocator.geocode(location)

    # Handle error if location is not valid
    if location_data is None:
        print('Invalid location')
        return None

    lat = location_data.latitude
    lon = location_data.longitude

    # Make the API request
    api_key = '907203e6a9bdef2ae66c76c1636d30d9'  # Replace with your Weatherstack API key
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={lat},{lon}'
    response = requests.get(url)
    data = json.loads(response.text)

    return data

# Get the weather data
data = get_weather_data(args.location)

# Display the weather information based on options selected
if args.description or args.temp or args.humidity or args.timezone:
    if data is None:
        print('Weather information not available')
    else:
        if args.description:
            print(data['current']['weather_descriptions'][0])

        if args.temp:
            if 'temperature' in data['current']:
                temp = data['current']['temperature']
                print(f'Temperature: {temp}°C')
            else:
                print('Temperature information not available')

        if args.humidity:
            if 'humidity' in data['current']:
                humidity = data['current']['humidity']
                print(f'Humidity: {humidity}%')
            else:
                print('Humidity information not available')

        if args.timezone:
            if 'timezone_id' in data['location']:
                timezone = data['location']['timezone_id']
                print(f'Timezone: {timezone}')
            else:
                print('Timezone information not available')
else:
    print('At least one option is required')
