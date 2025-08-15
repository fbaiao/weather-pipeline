import os
import pandas as pd
from src.utils import get_logger
from src.config import Settings

logger = get_logger()

def save_records(records: list[dict], cfg: Settings) -> None:
    if not records:
        logger.warning("Nenhum registro para salvar.")
        return
    os.makedirs(os.path.dirname(cfg.output_path), exist_ok=True)
    df = pd.DataFrame(records)

    if cfg.output_format == "parquet":
        path = cfg.output_path if cfg.output_path.endswith(".parquet") else cfg.output_path + ".parquet"
        df.to_parquet(path, index=False)
        logger.info("Parquet salvo em %s", path)
    else:
        path = cfg.output_path if cfg.output_path.endswith(".csv") else cfg.output_path + ".csv"
        header = not os.path.exists(path)
        df.to_csv(path, index=False, mode="a" if not header else "w", header=header)
        logger.info("CSV atualizado em %s", path)
