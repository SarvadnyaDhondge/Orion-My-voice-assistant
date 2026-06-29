"""
weather.py

This module handles weather-related voice commands.

Responsibilities:
- Understand the user's command.
- Extract the city name.
- Ask the weather service for data.
- Speak the result.

It does NOT communicate directly with OpenWeather.
That responsibility belongs to weather_service.py.
"""

from speak import speak
from services.weather_service import get_weather


def handle_weather(command):
    """
    Handles weather/temperature commands.

    Returns
    -------
    bool
        True  -> Weather command handled.
        False -> Not a weather command.
    """

    command = command.lower().strip()

    # ---------------- Temperature ----------------

    if command.startswith("temperature"):

        city = command.replace("temperature", "", 1).strip()

        # Support: "temperature in pune"
        if city.startswith("in "):
            city = city[3:].strip()

    # ---------------- Weather ----------------

    elif command.startswith("weather"):

        city = command.replace("weather", "", 1).strip()

        # Support: "weather in pune"
        if city.startswith("in "):
            city = city[3:].strip()

    else:
        return False

    # Default city
    if not city:
        city = "Pune"

    # Debug (temporary)
    print("City:", city)

    weather = get_weather(city)

    if weather is None:
        speak("Sorry, I couldn't get the temperature.")
        return True

    speak(
        f"The temperature in {weather['city']} is "
        f"{round(weather['temperature'])} degrees Celsius "
        f"with {weather['description']}. "
        f"The humidity is {weather['humidity']} percent."
    )

    return True