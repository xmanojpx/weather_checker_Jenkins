import pytest
from unittest.mock import patch
from weather import get_weather

def test_get_weather_success():
    """Test successful weather fetch with mocked response."""
    mock_response = "🌤️ +34°C"
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = mock_response
        result = get_weather("Chennai")
        assert result == mock_response

def test_get_weather_failure():
    """Test weather fetch failure with mocked error."""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("Network error")
        result = get_weather("InvalidCity")
        assert "Error fetching weather" in result 