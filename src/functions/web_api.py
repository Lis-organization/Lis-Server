import requests
from .keys.keys import get_weather_key



def get_weather(country='ru', city='Perm'):

	response = requests.get('https://api.openweathermap.org/data/2.5/weather?', headers={'Accept':'application/json'}, params={
		'lang': 'ru',
		'q': city,
		'appid': get_weather_key(),
		})

	data = response.json()
	return str(round(data['main']['temp'] - 273.15, 2)) + ' °C, ' + data['weather'][0]['description']