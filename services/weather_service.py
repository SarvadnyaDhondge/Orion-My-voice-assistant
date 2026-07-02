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

HEADERS = {
    "User-Agent": "Orion Voice Assistant"
}


def get_weather(city):
    """
    Get the current weather for a city.

    Parameters
    ----------
    city : str
        Name of the city.

    Returns
    -------
    dict | None
        Example:
        {
            "city": "Pune",
            "temperature": 31,
            "description": "clear sky",
            "humidity": 52
        }

        Returns None if the request fails.
    """

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
    }

    try:

        response = requests.get(
            BASE_URL,
            params=params,
            headers=HEADERS,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }

    except requests.RequestException:
        print("Weather service request failed.")
        return None