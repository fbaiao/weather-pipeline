# Salva os dados em parquet
import os
import pandas as pd
from utils import get_logger
from pymongo import MongoClient
from datetime import datetime, timezone

logger = get_logger()

# Save parquet file
def save_to_parquet(records, path="./data/weather_data.parquet"):
    if not records:
        logger.warning("No records to save.")
        return
    
    df = pd.DataFrame(records)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_parquet(path, engine='pyarrow', index=False)

    logger.info(f"Data saved in parquet file to {path}")

# Save csv file
def save_to_csv(records, path="./data/weather_data.csv"):
    if not records:
        logger.warning("No records to save.")
        return
    
    df = pd.DataFrame(records)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if os.path.exists(path):
        df.to_csv(path, mode='a', header=False, index=False)
    else:
        df.to_csv(path, index=False)

    logger.info(f"Data saved in csv file to {path}")

# Save data in mongoDB database
def save_to_mongodb(records, mongo_uri, db_name="weather_db", collection_name="weather_data"):
    if not records:
        logger.warning("No records to save to MongoDB.")
        return
    
    try:
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]

        collection.insert_many(records)
        logger.info(f"Data inserted into MongoDB: {db_name}.{collection_name} ({len(records)} records)")
    except Exception as e:
        logger.error(f"Error saving data to MongoDB: {e}")

# Save a single execution log in MongoDB summarizing the pipeline run.
def save_log_mongodb(run_id, start_time, end_time, records_processed, errors=None, mongo_uri=None, db_name="weather_db", collection_name="pipeline_logs"):

    if not mongo_uri:
        logger.warning("MONGO_URI not set. Logs won't be saved to MongoDB.")
        return
    
    status = "success"
    if errors:
        if records_processed > 0:
            status = "partial_success"
        else:
            status = "failed"

    log_doc = {
        "run_id": run_id,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "status": status,
        "records_processed": records_processed,
        "errors": errors or []
    }

    try:
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]
        collection.insert_one(log_doc)
        logger.info(f"Pipeline log saved_ run_id={run_id}, status={status}")
    except Exception as e:
        logger.error(f"Error saving pipeline log to MongoDB: {e}")