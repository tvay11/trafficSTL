# trafficSTL

## Overview

This Python script uses Google Maps Directions API to fetch real-time estimated travel times between various origin-destination pairs. The script reads these pairs from a CSV file (`locations.csv`) and writes the travel time information to another CSV file (`travel_time_data.csv`). The collected data is appended to the CSV file every three minutes, providing a time-series of travel times.

## Prerequisites

- Python 3.x
- Google Maps Directions API key
- `requests` library

To install the `requests` library, run:

```bash
pip install requests
```

## Configuration

### API Key

Save your Google Maps API key in a `config.json` file as follows:

```json
{
  "API_KEY": "YOUR_GOOGLE_MAPS_API_KEY_HERE"
}
```

### .gitignore

To keep sensitive information like your API key secure, create a `.gitignore` file in the root directory of your project and add the following:

```
# .gitignore

# Ignore configuration files
config.json

## Usage

Run the Python script:

```bash
python main.py
```

The script will:

1. Read origin-destination pairs from `locations.csv`.
2. Fetch real-time travel times for each pair.
3. Append this data to `travel_time_data.csv`.

## Output

```csv
Current estimated travel time from 38.608157, -90.212793 to  38.503658, -90.338531: 13 mins
Current estimated travel time from  38.503658, -90.338531 to 38.608157, -90.212793: 20 mins
Current estimated travel time from 38.645402767911236, -90.19038008948353 to 38.73941750302947, -90.36711780510736: 16 mins
Current estimated travel time from 38.73941750302947, -90.36711780510736 to 38.645402767911236, -90.19038008948353: 13 mins
Current estimated travel time from 38.50704992855341, -90.34868169228166 to 38.69506236867715, -90.45064444421797: 18 mins
Current estimated travel time from 38.69506236867715, -90.45064444421797 to 38.50704992855341, -90.34868169228166: 18 mins
Current estimated travel time from 38.619117861748094, -90.18701619928001 to 38.62974944872341, -90.34160510195098: 12 mins
Current estimated travel time from 38.62974944872341, -90.34160510195098 to 38.619117861748094, -90.18701619928001: 8 mins
Current estimated travel time from 38.64272364200376, -90.1884845499635 to 38.55058291280976, -90.42464789236925: 25 mins
Current estimated travel time from 38.55058291280976, -90.42464789236925 to 38.64272364200376, -90.1884845499635: 17 mins
```
