# Weather_Forecast
This repo contains a project worked on Weather Forecasting using Python and Open Weather API 

This is Python program used for weather forecasting using Python(request module), open weather map API and JSON.
Temprature, weather forecast and historical climate data can be known using this code snippet.
The working of the code snippet is provided below.

***WEATHER FORECAST USING PYTHON***

This code uses the OpenWeatherMap API to get real-time weather data based on user input for a location or city name. Here's what each part of this code does:
import requests: Imports the Python requests module, which is used to send HTTP requests and receive responses.
api_key = "75e1df5e73d003c78abc839cdd296ce5": Assigns an API key from OpenWeatherMap to a variable.(YOU CAN USE THIS API KEY OR GET AN API KEY FOR YOURSELF FROM www.openweathermap.org)
url_base = "https://api.openweathermap.org/data/2.5/weather?": Specifies the base URL endpoint for the OpenWeatherMap API.
location = input("Enter Location: "): Asks the user to enter their desired location/city name or latitude/longitude coordinates as input.
The next few lines use a try-except block to handle any potential errors with user inputs:
If the entered value is numeric (latitude/longitude), it splits those values and forms query parameters accordingly.
Otherwise, it simply forms query parameters using city names.
It then adds API key and necessary units in query params and sends GET request using 'requests' library of python
It parses JSON response returned by OpenWeatherMap api call
If there are any error messages returned by OenWeatheerAPI ,then prints them. Else extracts relevant temperature information & description of weather conditions from parsed JSON object.
Finally, it prints formatted output containing current temperature in Celsius along with description of weather condition at given location/city name.

