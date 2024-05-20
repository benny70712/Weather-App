# Weather App
#### Video Demo:  <URL [HERE](https://youtu.be/0fMAzEMUFqg)>
#### Description:
Hello, my name is Kyaw Lin Tun and here is my final project for CS50P. The project is a weather application that retrieves and displays weather information for a specified city using the OpenWeather API. The application is designed to be used from the command line and provides temperature readings in either Celsius or Fahrenheit based on user input.

#### check_command_line_arg()
The check_command_line_arg() function is responsible for validating the command line arguments provided by the user. It ensures that there are exactly two arguments: the script name and one additional argument, which should be either 'c' or 'f'. The argument 'c' indicates that the temperature should be displayed in Celsius, while 'f' indicates Fahrenheit. If the argument count is incorrect or the unit is invalid, the function exits the program with an appropriate error message.

#### kelvin_to_celsius(temp_kelvin)
The kelvin_to_celsius() function converts a temperature from Kelvin to Celsius. The conversion formula used is Celsius = Kelvin - 273.15. This function takes a single argument, temp_kelvin, and returns the temperature in Celsius, rounded to the nearest integer.

#### kelvin_to_fahrenheit(temp_kelvin)
Similarly, the kelvin_to_fahrenheit() function converts a temperature from Kelvin to Fahrenheit using the formula Fahrenheit = (Kelvin - 273.15) * 9/5 + 32. It also takes one argument, temp_kelvin, and returns the temperature in Fahrenheit, rounded to the nearest integer.

#### get_weather_data(city)
The get_weather_data() function fetches weather data for a given city using the OpenWeather API. The function constructs the request URL using the city name and a predefined API key, then sends a GET request to the API. If the request is successful (status code 200), it processes the JSON response to extract relevant weather information, such as description, temperature, feels-like temperature, humidity, wind speed, and wind direction.

#### print_weather_table(weather_data)
The print_weather_table() function takes the weather data dictionary returned by get_weather_data() and prints it in a neatly formatted table using the tabulate library. The table includes headers for the city name and weather information, and rows for each piece of weather data, such as description, temperature, feels-like temperature, humidity, wind speed, and wind direction.

#### Main Function
The main function ties everything together. It first calls check_command_line_arg() to ensure the command line arguments are valid. It then prompts the user to enter a city name. The city name is converted to lowercase to ensure consistency in the API request.

The function then calls get_weather_data() with the city name. If the function returns None, indicating that the city was not found or there was an error, the program exits with an appropriate message. Otherwise, it calls print_weather_table() to display the weather information to the user.


