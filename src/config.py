from pydantic import BaseModel
from typing import List, Literal
from dotenv import load_dotenv
import os, json

class Settings(BaseModel):
    cities: List[str]
    units: Literal['metric','imperial','standard'] = 'metric'
    output_format: Literal['csv','parquet'] = 'csv'
    output_path: str
    api_key: str | None = None

def load_config() -> Settings:
    load_dotenv()
    api_key_env = os.getenv("OWM_API_KEY")

    with open("config.json", "r", encoding="utf-8") as f:
        cfg = json.load(f)

    return Settings(**{**cfg, "api_key": api_key_env})
