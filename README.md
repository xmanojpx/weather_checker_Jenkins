# Weather Checker CLI

A simple command-line tool that fetches current weather for any city using wttr.in.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/weatherchecker.git
cd weatherchecker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with a city name as argument:
```bash
python weather.py Chennai
```

Example output:
```
Weather in Chennai: 🌤️ +34°C
```

## Testing

Run the tests using pytest:
```bash
pytest test_weather.py
```

## CI/CD

This project uses Jenkins for continuous integration:
- GitHub push triggers Jenkins job
- Jenkins pulls the repository
- Runs tests automatically
- Shows pass/fail status 