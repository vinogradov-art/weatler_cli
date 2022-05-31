import os
from get_weather import get_weather_open_weather
from printout import printout
from dotenv import load_dotenv


def main():
    load_dotenv('.env')
    token = os.getenv('OPEN_WEATHER_TOKEN')
    city = input("Введите название города: ")
    data = get_weather_open_weather(city, token)
    printout(data)


if __name__ == '__main__':
    main()
