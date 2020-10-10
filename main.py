from src.functions import nutrition
from src.functions.web_api import get_weather
import random


comands = {
	'name': ('лис', 'лисенок', 'рыжий', 'лиз', 'лист'),
	'rec': ('скажи', 'расскажи', 'сколько', 'сегодня', 'привет', 'какая'),
	'cmd': {
		'greeting': ('меня зовут', 'как тебя зовут', 'тебя зовут'),
		'nutrition': ('будут питаться', 'питаются', 'будут есть'),
		'weather': ('погода', 'погодка', 'сейчас погода')
	}
}



def replace_words_in_string(text):

	text = text.lower()

	for row in comands['name']:
		text = text.replace(row, '').strip()

	for row in comands['rec']:
		text = text.replace(row, '').strip()

	return text


def check_comands(text):

	if text in comands['cmd']['greeting']:

		greetings = ['Привет, меня зовут Лис!', 'Хай! Меня зовут ЛИИИС!']
		random.shuffle(greetings)
		print(greetings[0])
		return greetings[0]


	elif text in comands['cmd']['weather']:
		return get_weather()

	if text in comands['cmd']['nutrition']:
		pass



print(check_comands(replace_words_in_string('Привет лис какая сейчас погода')))