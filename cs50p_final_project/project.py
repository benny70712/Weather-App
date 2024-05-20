"""
Project title - Weather App
Name - Kyaw Lin Tun
GitHub Name - benny70712
Edx Name - kyawlintun2023
City - Toronto
Country - Canada
Date - 5/19/2024
"""

import requests, sys
from tabulate import tabulate


def main():
    check_command_line_arg()

    city = input("Enter the city: ").lower()
    if (get_weather_data(city) == None):
        sys.exit(f"Sorry, the city '{city}' doesn't exist")

    weather_data = get_weather_data(city)
    print_weather_table(weather_data)

# check the command line argument
def check_command_line_arg():
    # the length of sys.argv should be 2
    if len(sys.argv) < 2:
        sys.exit("Insufficient command line argument")

    if len(sys.argv) > 2:
        sys.exit("Too many command line argument")

    # sys.argv[1] should be either c or f
    if not sys.argv[1].lower() in ['c','f']:
        sys.exit("Incorrect unit")


# change from kelvin to celisus
def kelvin_to_celsius(temp_kelvin):
    return round(temp_kelvin - 273.15)

# change from kelvin to fahrenheit
def kelvin_to_fahrenheit(temp_kelvin):
    return round(((temp_kelvin - 273.15) * (9/5)) + 32)

# get the weather data
def get_weather_data(city):
    API_KEY = "495bdceb8b11fb2a39dbd37242912dac"
    REQUEST_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(REQUEST_URL)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather']
        temp_data = data['main']

        description = weather[0]['description']
        humidity = temp_data['humidity']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']

        if sys.argv[1] == 'c':
            temp = kelvin_to_celsius(temp_data['temp'])
            temp_feel_like = kelvin_to_celsius(temp_data['feels_like'])
            return {"header": [city.upper(), "WEATHER'S INFO"],
                "table": [["Description", description.title()], ["Temperature", f"{temp}°C"], ["Feel like", f"{temp_feel_like}°C"],
                ["Humidity", f"{humidity} %"], ["Wind Speed", f"{wind_speed} m/s"], ["Wind Deg", f"{wind_deg} deg"]]}

        elif sys.argv[1] == 'f':
            temp = kelvin_to_fahrenheit(temp_data['temp'])
            temp_feel_like = kelvin_to_fahrenheit(temp_data['feels_like'])
            return {"header": [city.upper(), "INFO"],
                "table": [["Description", description.title()], ["Temperature", f"{temp} °F"], ["Feel like", f"{temp_feel_like} °F"],
                ["Humidity", f"{humidity} %"], ["Wind Speed", f"{wind_speed} m/s"], ["Wind Deg", f"{wind_deg} deg"]]}
    else:
        return None


# print the weather table in terminal
def print_weather_table(weather_data):
    table = weather_data["table"]
    headers = weather_data["header"]
    print(tabulate(table, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
