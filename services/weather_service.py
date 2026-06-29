"""
weather_service.py

Responsible for communicating with the OpenWeather API.

This module should ONLY communicate with the API.

It should NOT:
- Speak
- Listen
- Understand commands

It only returns weather data.
"""

import requests

from config.settings import WEATHER_API_KEY


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Returns weather information for a city.

    Parameters
    ----------
    city : str

    Returns
    -------
    dict | None
    """

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(BASE_URL, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }

    except requests.RequestException as e:
        print("Weather Service Error:", e)
        return None