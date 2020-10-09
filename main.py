import speech_recognition as sr
import pyttsx3
from src.functions import nutrition
import random
import requests
from src.functions.keys.keys import get_weather_key
import eel


eel.init("web")
eel.start("main.html", size=(900, 1000))

comands = {
	'name': ('лис', 'лисенок', 'рыжий', 'лиз', 'лист'),
	'rec': ('скажи', 'расскажи', 'сколько', 'сегодня', 'привет', 'какая'),
	'cmd': {
		'greeting': ('меня зовут', 'как тебя зовут', 'тебя зовут'),
		'nutrition': ('будут питаться', 'питаются', 'будут есть'),
		'weather': ('погода', 'погодка', 'сейчас погода')
	}
}


def speak_text(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', 'ru')
	for voice in voices:
		if voice.name == 'Aleksandr':
			engine.setProperty('voice', voice.id)
	engine.say(text)
	engine.runAndWait()


def recognize_speak():
	recognizer = sr.Recognizer()
	with sr.Microphone(device_index=0) as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		text = recognizer.recognize_google(audio, language='ru-RU')
		return text.lower()


def replace_words_in_string(text):
	for row in comands['name']:
		text = text.replace(row, '').strip()

	for row in comands['rec']:
		text = text.replace(row, '').strip()

	return text


def check_comands(text):

	if text in comands['cmd']['greeting']:

		greetings = ['Привет, меня зовут Лис!', 'Хай! Меня зовут ЛИИИС!']
		random.shuffle(greetings)
		speak_text(greetings[0])


	elif text in comands['cmd']['weather']:
		speak_text(get_weather())

	if text in comands['cmd']['nutrition']:
		pass




def get_weather(country='ru', city='Perm'):

	response = requests.get('https://api.openweathermap.org/data/2.5/weather?', headers={'Accept':'application/json'}, params={
		'lang': 'ru',
		'q': city,
		'appid': get_weather_key(),
		})

	data = response.json()
	return str(round(data['main']['temp'] - 273.15, 2)) + ' °C, ' + data['weather'][0]['description']



check_comands(replace_words_in_string(recognize_speak()))