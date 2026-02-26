# Weather App

This is a simple Python program that fetches real-time weather data for a given city using the OpenWeatherMap API. It provides details like temperature, humidity, pressure, and weather description.

## Features

City Weather Info: Get current weather data for any city.
Temperature: Displays the temperature and how it feels.
Humidity & Pressure: Provides humidity and atmospheric pressure information.
Weather Description: Displays the weather condition (e.g., clear sky, rain, etc.).

## Requirements

- Python 3.x
- No additional libraries required (used for making HTTP requests)

## How to Run

1. Clone or download this repository.
2. Obtain an API key from OpenWeatherMap�.
3. Replace the api_key in the code with your own API key.
4. Run the script:

bash
    python main.py

5. When prompted, enter the city name to get the weather information.

## Example Usage

`bash

        Enter your city name: London

        Weather in London:
        Temperature: 15°C
        Temperature feels like: 14°C
        Pressure: 1012 hPa
        Humidity: 77%
        Weather Description: Clear sky

## How It Works
- User Input: The program prompts you to enter the name of the city.
- API Request: It sends a GET request to the OpenWeatherMap API with the city name and your API key.
- Weather Data: Once the response is received, the program parses the JSON data and extracts the temperature, humidity, pressure, and weather description.
- Results Display: It then displays the weather information in a human-readable format.

## Troubleshooting
API Request Fails: If the API request fails or the city is not found, make sure the city name is correct and try again.

API Key: Ensure that you have a valid API key from OpenWeatherMap.

Error Handling: If the API returns an error (e.g., invalid city name), the program will display a failure message.
