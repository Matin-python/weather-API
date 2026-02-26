import requests, json

# Your API key
api_key = 'Your API key'

# Base URL for the API
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

# Get city name from the user
city_name = input("Enter your city name: ")

# Construct the complete URL
complete_url = base_url + 'appid=' + api_key + '&q=' + city_name + '&&units=metric'

# Make the GET request to fetch the weather data
response = requests.get(complete_url)

# Convert the response to JSON
data = response.json()

# Check if the API response is valid
if data['cod'] == 200:
    # Extract the relevant weather data
    main = data['main']
    weather = data['weather'][0]
    
    # Get temperature and weather description
    temp = main['temp']
    feels_like = main['feels_like']
    pressure = main['pressure']
    humidity = main['humidity']
    weather_description = weather['description']

    # Display the results
    print(f"\nWeather in {city_name.capitalize()}:")
    print(f"Temperature: {temp}°C")
    print(f"Temperature feels like: {feels_like}°C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description.capitalize()}")
else:
    print("City not found or API request failed. Please check the city name and try again.")