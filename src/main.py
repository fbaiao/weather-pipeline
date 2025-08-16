from config import load_config, get_api_key
from fetch_weather import get_weather_data
from utils import get_logger
from save_data import save_to_parquet, save_to_mongodb, save_log_mongodb
import os
from dotenv import load_dotenv

load_dotenv()
logger = get_logger()

# Orchestrates the execution of the project
def main():
    mongo_uri = None
    try: 
        #Load .env variables
        mongo_uri = os.getenv("MONGO_URI")
        if not mongo_uri:
            logger.warning("MONGO_URI not set in .env file. MongoDB won't be used.")
        
        # Load configs and API key
        config = load_config("config.json")
        api_key = get_api_key()

        # Cities and units from config
        cities = config.get("cities", [])
        units = config.get("units", "metric")
        output_path = config.get("output_path_parquet", "weather_data.parquet")

        logger.info(f"Fetching weather data for cities: {cities}")

        # Fetch weather data
        weather_records = get_weather_data(api_key, cities, units)

        if not weather_records:
            logger.warning("No weather data fetched. Exiting.")
            return

        # Show results in console
        for r in weather_records:
            logger.info(f"{r['city']} | {r['date']} | {r['temperature']}°C | {r['humidity']}% | {r['weather']}")

        # Save to parquet
        save_to_parquet(weather_records, output_path)

        # Save to mongoDB collection
        if mongo_uri:
            save_to_mongodb(weather_records, mongo_uri)
        
        logger.info(f"Pipeline finished successfully. {len(weather_records)} records processed.")
        if mongo_uri:
            save_log_mongodb(f"Pipeline finished successfully. {len(weather_records)} records processed.", level="INFO",      mongo_uri=mongo_uri)
    

    except Exception as e:
        logger.exception(f"Pipeline failed with error: {e}")
        if mongo_uri:
            save_log_mongodb(f"Pipeline failed with error: {e}", level="ERROR", mongo_uri=mongo_uri)

if __name__ == "__main__":
    main()