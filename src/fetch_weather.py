import requests
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)

# Connect to OpenWeatherMap API
def get_weather_data(api_key, cities, units="metric"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    results = []
    errors = []

    for city in cities:
        params = {"q": city, "appid": api_key, "units": units}

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Check if the response contains valid data; log and skip if the city is not found or data is incomplete

            if data.get("cod") != 200:
                error_msg = f"API error for {city}: {data.get('message')}"
                logger.error(error_msg)
                errors.append(error_msg)
                continue

            if "main" not in data or "weather" not in data:
                error_msg = f"Incomplete data for {city}: {data}"
                logger.error(error_msg)
                errors.append(error_msg)
                continue

            results.append({
                "city": city,
                "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "weather": data["weather"][0]["description"]
            })

        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code if e.response else "unknown"
            error_msg = f"HTTP error for {city}: {status_code} - {e}"
            logger.error(error_msg)
            errors.append(error_msg)

        except requests.exceptions.RequestException as e:
            error_msg = f"Network error for {city}: {e}"
            logger.error(error_msg)
            errors.append(error_msg)

        except Exception as e:
            error_msg = f"Unexpected error for {city}: {e}"
            logger.error(error_msg)
            errors.append(error_msg)

    return results, errors
