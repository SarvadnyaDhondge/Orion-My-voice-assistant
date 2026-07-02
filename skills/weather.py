"""
weather.py

This module handles weather-related voice commands.

Responsibilities
----------------
- Understand weather commands.
- Extract the city name.
- Ask weather_service.py for weather data.
- Speak the result.

This module does NOT communicate directly with the weather API.
"""

from speak import speak
from services.weather_service import get_weather


def handle_weather(command):
    """
    Handle weather-related commands.

    Returns
    -------
    bool
        True -> Command handled.
        False -> Not a weather command.
    """

    command = command.lower().strip()

    # Determine command type
    if command.startswith("temperature"):
        keyword = "temperature"

    elif command.startswith("weather"):
        keyword = "weather"

    else:
        return False

    # Extract city
    city = command.replace(keyword, "", 1).strip()

    if city.startswith("in "):
        city = city[3:].strip()

    # Default city
    if not city:
        city = "Pune"

    weather = get_weather(city)

    if weather is None:
        speak("Sorry, I couldn't get the weather information.")
        return True

    speak(
        f"The temperature in {weather['city']} is "
        f"{round(weather['temperature'])} degrees Celsius "
        f"with {weather['description']}. "
        f"The humidity is {weather['humidity']} percent."
    )

    return True