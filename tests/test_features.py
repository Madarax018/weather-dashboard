import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class WeatherTests(unittest.TestCase):
    def test_weather_api_and_interface(self):
        html = (ROOT / "index.html").read_text()
        self.assertIn("open-meteo.com", html)
        self.assertIn("temperature_2m", html)
        self.assertIn("relative_humidity_2m", html)
        self.assertIn("getWeather()", html)
