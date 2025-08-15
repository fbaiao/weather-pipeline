import datetime as dt
import requests
from typing import List, Dict
from src.utils import get_logger
from src.config import Settings

logger = get_logger()

def get_weather(city: str, api_key: str, units: str = "metric") -> dict:
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units={units}"
    )
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        return {
            "city": city,
            "date_utc": dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
        }
    except requests.HTTPError as e:
        logger.error("HTTP error para %s: %s", city, e)
    except requests.RequestException as e:
        logger.error("Erro de rede para %s: %s", city, e)
    except Exception as e:
        logger.error("Erro inesperado para %s: %s", city, e)
    return {}

def fetch_all_cities_weather(cfg: Settings) -> List[Dict]:
    results: List[Dict] = []
    if not cfg.api_key:
        logger.error("API key não encontrada. Configure OWM_API_KEY no .env.")
        return results

    for city in cfg.cities:
        rec = get_weather(city, cfg.api_key, cfg.units)
        if rec:
            results.append(rec)
    return results
