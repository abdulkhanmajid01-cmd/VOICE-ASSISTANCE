"""
Weather Features Module
Handles weather information retrieval and updates
"""

import logging
import requests
from config import WEATHER_API_KEY, DEFAULT_CITY, TEMPERATURE_UNIT, DEBUG_MODE

logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)
logger = logging.getLogger(__name__)


def get_weather(city=None):
    """
    Get current weather for a city.
    
    Args:
        city (str): City name. If None, uses default city from config.
        
    Returns:
        tuple: (success: bool, message: str or dict)
    """
    try:
        if city is None:
            city = DEFAULT_CITY
        
        if WEATHER_API_KEY == "YOUR_API_KEY_HERE":
            logger.warning("Weather API key not configured")
            return False, "Weather API is not configured. Please set your API key in config.py"
        
        # Using Open-Meteo (free API, no key required) or OpenWeatherMap
        # This example uses a simple approach without API key
        logger.info(f"Fetching weather for: {city}")
        
        # Alternative: Using wttr.in (free weather API)
        try:
            response = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5)
            if response.status_code == 200:
                data = response.json()
                weather_data = data['current_condition'][0]
                
                info = {
                    "city": city,
                    "temperature": weather_data['temp_C'],
                    "description": weather_data['weatherDesc'][0]['value'],
                    "humidity": weather_data['humidity'],
                    "wind_speed": weather_data['windspeedKmph'],
                }
                
                logger.info(f"Weather data retrieved for {city}")
                return True, info
        except Exception as e:
            logger.error(f"Error fetching weather from wttr.in: {e}")
        
        return False, f"I couldn't retrieve weather for {city}."
    except Exception as e:
        logger.error(f"Error in get_weather: {e}")
        return False, "An error occurred while retrieving weather information."


def format_weather_message(weather_data):
    """
    Format weather data into a readable message.
    
    Args:
        weather_data (dict): Weather information dictionary
        
    Returns:
        str: Formatted weather message
    """
    try:
        message = f"The weather in {weather_data['city']} is {weather_data['description']}. "
        message += f"Temperature is {weather_data['temperature']} degrees, "
        message += f"with {weather_data['humidity']}% humidity and wind speed of {weather_data['wind_speed']} km/h."
        
        logger.info("Weather message formatted")
        return message
    except Exception as e:
        logger.error(f"Error formatting weather message: {e}")
        return "I couldn't format the weather information."


def get_weather_forecast(city=None, days=3):
    """
    Get weather forecast for a city.
    
    Args:
        city (str): City name
        days (int): Number of days to forecast
        
    Returns:
        tuple: (success: bool, message: str or list)
    """
    try:
        if city is None:
            city = DEFAULT_CITY
        
        logger.info(f"Fetching {days}-day forecast for: {city}")
        
        # This would require a more comprehensive API
        # For now, returning a placeholder
        logger.warning("Forecast feature requires API upgrade")
        return False, "Weather forecast feature requires an API upgrade."
    except Exception as e:
        logger.error(f"Error getting weather forecast: {e}")
        return False, "An error occurred while retrieving the forecast."


def is_weather_available():
    """
    Check if weather service is available.
    
    Returns:
        bool: True if available, False otherwise
    """
    try:
        response = requests.get("https://wttr.in/London?format=j1", timeout=2)
        is_available = response.status_code == 200
        logger.info(f"Weather service available: {is_available}")
        return is_available
    except Exception:
        logger.warning("Weather service not available")
        return False
