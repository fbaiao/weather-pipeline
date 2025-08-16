import sys
import os
import json
import tempfile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import load_config, get_api_key


def test_get_api_key(monkeypatch):
    # Environment variable
    monkeypatch.setenv("OPENWEATHER_API_KEY", "fake_key")
    assert get_api_key() == "fake_key"


def test_load_config(monkeypatch):
    # Create temp config.json
    temp_config = {
        "cities": ["Lisbon"],
        "units": "metric",
        "output_format": "csv",
        "output_path": "./data/weather.csv"
    }

    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
        json.dump(temp_config, tmp)
        tmp_path = tmp.name

    try:
        monkeypatch.setenv("OPENWEATHER_API_KEY", "fake_key")
        cfg = load_config(tmp_path)
        assert cfg["units"] == "metric"
        assert cfg["output_format"] in ("csv", "parquet")
        assert cfg["api_key"] == "fake_key"
    finally:
        os.remove(tmp_path)
