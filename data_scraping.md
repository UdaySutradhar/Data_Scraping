Weather Data Scraping
This project demonstrates weather data scraping using a command-line interface (CLI) and a Flask-based front-end. It allows users to retrieve weather information for a specific location, including the description, temperature, humidity, and timezone.

-:Tech Stack:-
1.Python: Programming language used for the CLI and Flask app
2.Flask: Web framework used to create the front-end interface
3.geopy: Python library for geocoding and getting location data
4.requests: Library for making HTTP requests to retrieve weather data
5.BeautifulSoup: Library for parsing HTML data (optional for web scraping)
6.argparse: Library for parsing command-line arguments

-:Features:-
1.Retrieve weather information for a specified location
2.Display weather description, temperature, humidity, and timezone
3.Command-line interface (CLI) for direct usage
4.Web interface built with Flask for easy interaction

Usage
Clone the repository:
git clone https://github.com/your-username/weather-data-scraping.git

Install the required dependencies:
pip install -r requirements.txt

Run the CLI:
python weather_cli.py [location] [--description] [--temp] [--humidity] [--timezone]
