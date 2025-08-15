from src.config import Settings

def test_settings_defaults():
    s = Settings(cities=['Lisbon'], units='metric', output_format='csv', output_path='./data/weather.csv', api_key='x')
    assert s.units == 'metric'
    assert s.output_format in ('csv','parquet')
