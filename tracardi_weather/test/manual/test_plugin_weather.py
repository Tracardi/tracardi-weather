import asyncio
from tracardi.domain.profile import Profile
from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from tracardi_weather.plugin import WeatherAction


def test_weather_plugin_plain_text():
    init = {
        "system": "metric",
        "city": "Wrocław"
    }

    payload = {}
    result = run_plugin(WeatherAction, init, payload)

    print(result)


def test_weather_plugin_path():
    init = {
        "system": "metric",
        "city": "payload@city"
    }

    payload = {"city": "Wrocław"}

    result = run_plugin(WeatherAction, init, payload)

    print(result)


