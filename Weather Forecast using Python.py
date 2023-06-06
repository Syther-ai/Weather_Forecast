'''WEATHER FORECAST'''


import requests

# Enter your API key and desired URL endpoint from OpenWeatherMap
api_key = "75e1df5e73d003c78abc839cdd296ce5"
url_base = "https://api.openweathermap.org/data/2.5/weather?"

# Ask user for their location or city name input.
location = input("Enter Location: ")

# Use try-except block to handle any potential errors with user inputs.
try:
    # Check if user input is numeric - this means they entered latitude/longitude coordinates instead of city name.
    if location.isnumeric():
        lat, lon = location.split(",")
        query_params = f"lat={lat}&lon={lon}"
    else:
        query_params = f"q={location}"
    
    # Add API key to URL parameters and send GET request to OpenWeatherMap API
    url_full = url_base + query_params + "&units=metric&appid=" + api_key
    response = requests.get(url_full)

    # Parse JSON data returned by API response 
    data_json = response.json()
    
    if data_json["cod"] != 200:
        print("Error:", data_json["message"])
        
    else:
        # Extract relevant temperature and weather condition information from parsed JSON object.
         temp_celsius=data_json['main']['temp']
         description=data_json['weather'][0]['description'].capitalize()

         
        
         # Print formatted output containing current temperature and description of weather conditions at given location/city name.
         
         print(f"\n\nCurrent Temperature in {data_json['name']}: {temp_celsius}°C")
         print(f"Conditions: {description}")
         
except Exception as e:
    print("Error:", str(e))
