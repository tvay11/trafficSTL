# trafficSTL

## Overview

This Python script uses Google Maps Directions API to fetch real-time estimated travel times between various origin-destination pairs. The script reads these pairs from a CSV file (`locations.csv`) and writes the travel time information to another CSV file (`travel_time_data.csv`). The collected data is appended to the CSV file every few seconds, providing a time-series of travel times.

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
