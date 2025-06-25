# """
# Переделать программу с погодой так что бы она
# запрашивала город а в ответ выдавала подробную информацию
# о погоде в этом городе в красивом формате.
# """

# Проблема с API, не могу выполнить на 100%
from pyowm import OWM
from pprint import pprint

owm = OWM("cfeff9fdf03f7360dc2663779f39193f")
mgr = owm.weather_manager()

city = input("Введите название город: ")

obs = mgr.weather_at_place(city)
weather = obs.weather

weather_data = {
    "Температура": weather.temperature("celsius")["temp"],
    "Давление": weather.pressure["press"],
    "Осадки": weather.rain if weather.rain else "Нет осадков",
    "Скорость ветра": weather.wind()["speed"],
}

pprint(weather_data)
