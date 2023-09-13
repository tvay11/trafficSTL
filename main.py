import json
import requests
import csv
import time
from datetime import datetime

with open('config.json', 'r') as f:
    config = json.load(f)
    api_key = config.get("API_KEY")


def fetch_highway_travel_time(api_key, origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}&departure_time=now&traffic_model=best_guess"

    response = requests.get(url)
    data = json.loads(response.text)

    if 'error_message' in data:
        print(f"Error: {data['error_message']}")
        return None

    if not data['routes']:
        print(f"No routes found between {origin} and {destination}")
        return None

    try:
        travel_time = data['routes'][0]['legs'][0]['duration_in_traffic']['text']
        print(f"Current estimated travel time from {origin} to {destination}: {travel_time}")
        return (f"{origin} - {destination}", travel_time)
    except KeyError:
        print(f"Could not retrieve travel time between {origin} and {destination}.")
        return None


def append_to_csv(data_dict):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open('travel_time_data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            row_data = [current_time]
            for origin_dest, travel_time in data_dict.items():
                row_data.append(travel_time)
            writer.writerow(row_data)
    except Exception as e:
        print(f"An error occurred while writing to the CSV: {e}")


def read_locations():
    locations = []
    try:
        with open('locations.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    locations.append((row[0], row[1]))
        return locations
    except FileNotFoundError:
        print("The file locations.csv was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

try:
    with open('travel_time_data.csv', 'x', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp'])
except FileExistsError:
    pass

if __name__ == "__main__":
    locations = read_locations()
    header_written = False

    while True:
        travel_data_dict = {}
        for origin, destination in locations:
            result = fetch_highway_travel_time(api_key, origin, destination)
            if result:
                travel_data_dict[result[0]] = result[1]

            result_reverse = fetch_highway_travel_time(api_key, destination, origin)
            if result_reverse:
                travel_data_dict[result_reverse[0]] = result_reverse[1]

        if not header_written:
            with open('travel_time_data.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                headers = ['Timestamp'] + list(travel_data_dict.keys())
                writer.writerow(headers)
            header_written = True

        append_to_csv(travel_data_dict)
        time.sleep(180)
