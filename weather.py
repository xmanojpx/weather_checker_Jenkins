#!/usr/bin/env python3

import sys
import requests

def get_weather(city):
    """Fetch weather data for a given city using wttr.in API."""
    try:
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        return f"Error fetching weather: {str(e)}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)
    
    city = sys.argv[1]
    weather = get_weather(city)
    print(f"Weather in {city}: {weather}")

if __name__ == "__main__":
    main() 