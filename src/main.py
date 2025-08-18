from config import load_config, get_api_key
from fetch_weather import get_weather_data
from utils import get_logger
from save_data import save_to_parquet, save_to_mongodb, save_log_mongodb
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
import uuid

load_dotenv()
logger = get_logger()

def main():
    mongo_uri = os.getenv("MONGO_URI")
    run_id = str(uuid.uuid4())  # unique id for execution
    start_time = datetime.now(timezone.utc)
    errors = []

    try:
        if not mongo_uri:
            logger.warning("MONGO_URI not set in .env file. MongoDB won't be used.")
        
        # Load configs and API key
        config = load_config("config.json")
        api_key = get_api_key()

        cities = config.get("cities", [])
        units = config.get("units", "metric")
        output_path = config.get("output_path_parquet", "./data/weather_data.parquet")

        logger.info(f"Fetching weather data for cities: {cities}")

        # Fetch weather data
        weather_records, errors = get_weather_data(api_key, cities, units)

        if weather_records:
            # Show results in console
            for r in weather_records:
                logger.info(f"{r['city']} | {r['date']} | {r['temperature']}°C | {r['humidity']}% | {r['weather']}")

            # Save to parquet
            save_to_parquet(weather_records, output_path)

            # Save to MongoDB
            if mongo_uri:
                save_to_mongodb(weather_records, mongo_uri)

        # Determine status
        if weather_records and not errors:
            status = "success"
        elif weather_records and errors:
            status = "partial_success"
        else:
            status = "failed"

        end_time = datetime.now(timezone.utc)
        records_processed = len(weather_records)

        # Save pipeline log
        if mongo_uri:
            save_log_mongodb(
                run_id=run_id,
                start_time=start_time,
                end_time=end_time,
                records_processed=len(weather_records),
                errors=errors,
                mongo_uri=mongo_uri
            )

        logger.info(f"Pipeline finished with status '{status}'. {records_processed} records processed.")

    except Exception as e:
        end_time = datetime.now(timezone.utc)
        logger.exception(f"Pipeline failed with error: {e}")
        if mongo_uri:
            save_log_mongodb(
                run_id=run_id,
                start_time=start_time,
                end_time=datetime.now(timezone.utc),
                records_processed=0,
                errors=[str(e)],
                mongo_uri=mongo_uri
            )

if __name__ == "__main__":
    main()
