import requests


def get_weather_open_weather(city: str, token: str) -> dict:
    try:
        response_weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&lang=ru&units=metric")
        data: dict = response_weather.json()
        data_acquisition: dict = {
            'temperature': round(data['main']['temp']),
            'city': data['name'],
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
            'weather': data['weather'][0]['description'],
            'weather_main': data['weather'][0]['main'],

        }
        print(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&lang=ru&units=metric")
        return data_acquisition
    except Exception as ex:
        print(ex)
