from src.config import load_config
from src.fetch_weather import fetch_all_cities_weather
from src.save_data import save_records
from src.utils import get_logger

logger = get_logger()

def run():
    cfg = load_config()
    logger.info(f"Iniciando pipeline para %d cidades...", len(cfg.cities))
    records = fetch_all_cities_weather(cfg)
    logger.info("Registos coletados: %d", len(records))
    save_records(records, cfg)

if __name__ == "__main__":
    run()
