## Weather Pipeline (OpenWeatherMap)

[![CI](https://github.com/fbaiao/weather-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/fbaiao/weather-pipeline/actions/workflows/ci.yml)
[![GitHub Repo](https://img.shields.io/badge/GitHub-weather--pipeline-blue?logo=github)](https://github.com/fbaiao/weather-pipeline)
[![Docker Hub](https://img.shields.io/docker/pulls/fabriciobaiao/weather-pipeline)](https://hub.docker.com/r/fabriciobaiao/weather-pipeline)

Daily Python pipeline to fetch current weather for a configurable list of cities using the OpenWeatherMap API.

   - Saves results as Parquet (data folder)
   - Inserts data into MongoDB (weather_data collection)
   - Logs pipeline execution in MongoDB (pipeline_logs collection)
   - Handles API/network errors gracefully without stopping execution

---

## Overview (pipeline details)

1. Fetch Weather Data
   - Uses OpenWeatherMap API to get current weather metrics (temperature, feels_like, humidity, description)
   - Configurable list of cities and units (metric/imperial)

2. Data Export
   - Saves results as a Parquet file in the data folder
   - Optional CSV export supported

3. MongoDB Integration
   - Inserts fetched weather data into weather_data collection
   - Logs execution summary in pipeline_logs collection including:
      - run_id (unique identifier for each run)
      - Start and end timestamps
      - Number of records processed
      - Status (success, partial_success, failed)
      - Errors for individual cities, without stopping pipeline

4. Error Handling
   - API or network failures are logged and do not interrupt the processing of remaining cities
   - Partial successes are recorded with details of which cities failed

5. Configuration
   - .env file for MongoDB URI and API keys
   - config.json for cities list, units, and output paths

---

## Features
- Modular structure (`src/`)
- External configuration (`config.json.example` + `.env.example`)
- Simple logging
- Output to CSV or Parquet (configurable)
- GitHub Actions for CI/CD (tests + Docker build & push)

---

## Prerequisites:
   - Python 3.11+
   - OpenWeatherMap account (to generate the API key)
   - Optional: Docker / MongoDB running

---

## Logging
   Logs are printed to stdout and stored in MongoDB (save_log_mongodb).

---

## How to use locally

1. **Clone the repository** and enter the folder:
   git clone https://github.com/fbaiao/weather-pipeline.git
   cd weather-pipeline

2. **Install the dependencies**:
   pip install -r requirements.txt

3. **Prepare configs**:
   - Create the `.env` file based on `.env.example`, and provide your API key (`OPENWEATHER_API_KEY`) and the connection string to insert data into the MongoDB database (`MONGO_URI`).
   - Create and copy `config.json.example` to `config.json` and adjust values as needed:
     example:
      {
         "cities": ["Lisbon", "Porto", "Madrid", "Paris"],
         "units": "metric",
         "output_format": "csv",
         "output_path_csv": "./data/weather_data.csv",
         "output_path_parquet": "./data/weather_data.parquet"
      }

4. **Execute**:
   python src/main.py

---

## Execute with Docker
- Build the image:
   docker build -t weather-pipeline .

- Run the container:
   docker run --rm --env-file .env weather-pipeline

Note: The `.env` file is not included in the Docker image for security reasons.

---

## GitHub Actions

The project comes with automatic workflows:

1. **CI (ci.yml)**

   - When it runs: on push or pull request.
   - What it does: installs dependencies and runs tests with pytest.
   - Where to see results: GitHub → Actions → CI.

2. **Build e Push Docker (docker.yml)**

   - When it runs: on push to the main branch.
   - What it does: builds the Docker image and pushes it to Docker Hub (`fabriciobaiao/weather-pipeline:latest`).
   - Required secrets: `DOCKER_USERNAME` and `DOCKER_PASSWORD` in GitHub Secrets.

Tip: You can manually trigger any workflow using the "Run workflow" button in GitHub Actions.

---

## Tests
pytest -q

---

## Variables and Configuration
- **API_Key** comes from `.env` (variable `OPENWEATHER_API_KEY`).
- **MONGO_URI** comes from `.env` (variable `MONGO_URI`).
- **List of cities**, units, output format, and path are defined in `config.json`.

---

## Project structure

weather_pipeline/
│── src/
│   ├── __init__.py        # to mark the folder `src` like a Python package
│   ├── main.py            # entry point
│   ├── fetch_weather.py   # API call
│   ├── config.py          # config reader
│   ├── save_data.py       # CSV/Parquet and MongoDB database saving
│   └── utils.py           # helper functions
│
│── .devcontainer/         # Devcontainer configuration (VS Code / Codespaces)
│   └── devcontainer.json
│
│── .github/
│   └── workflows/         # pipelines CI/CD
│       ├── ci.yml         # CI workflow: installs dependencies and runs tests (pytest) on each push/PR
│       └── docker.yml     # CD workflow: builds and publishes Docker image to Docker Hub (main branch)
│
│── data/
│   └── .gitkeep           # Created so git can version the folder
│
│── .env.example           # example to create your .env
│── config.json.example    # example to create your config.json, main configuration (list of cities, output format, file paths, etc.)
│── Dockerfile             # instructions to build the project's Docker image
│── LICENSE                # code usage and distribution license
│── pytest.ini             # pytest configuration (test discovery and execution)
│── README.md              # main project documentation
│── requirements.txt       # list of required Python dependencies
