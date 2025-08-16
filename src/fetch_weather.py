import requests
from datetime import datetime, timezone

# Connect to OpenWeatherMap API
def get_weather_data(api_key, cities, units="metric"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    results = []

    for city in cities:
        params = {"q": city, "appid": api_key, "units": units}

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            results.append({
                "city": city,
                "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "weather": data["weather"][0]["description"]
            })
        except Exception as e:
            print(f"Error fetching data for {city}: {e}")
        
    return results
