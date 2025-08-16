# Lê configs (.env ou json)
import os
from dotenv import load_dotenv
import json

# Carregar variáveis do .env
load_dotenv()

def load_config(path="config.json"):
    with open(path, "r") as f:
        config = json.load(f)
    
    # Substitui api_key pela variável do .env
    config["api_key"] = os.getenv("OPENWEATHER_API_KEY")
    if not config["api_key"]:
        raise ValueError("API Key not founded in .env ")
    
    return config

def get_api_key():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("API Key not founded in .env ")
    return api_key

