from src.functions import nutrition
from src.functions.web_api import get_weather, get_wikipedia
import random


comands = {
	'name': ('лис', 'лисенок', 'рыжий', 'лиз', 'лист'),
	'rec': ('скажи', 'расскажи', 'сколько', 'сегодня', 'привет', 'какая'),
	'cmd': {
		'greeting': ('меня зовут', 'как тебя зовут', 'тебя зовут'),
		'nutrition': ('будут питаться', 'питаются', 'будут есть'),
		'wikipedia': ('что означает слово', 'что такое', 'что такое слово', 'что за слово', 'кто такой',' кто такая'),
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
		return greetings[0]


	elif comands['cmd']['wikipedia'][0] in text or comands['cmd']['wikipedia'][1] in text or comands['cmd']['wikipedia'][2] in text or comands['cmd']['wikipedia'][3] in text or comands['cmd']['wikipedia'][4] in text or comands['cmd']['wikipedia'][5] in text:
		for row in comands['cmd']['wikipedia']:
			text = text.replace(row, '').strip()
		return get_wikipedia(text)


	elif text in comands['cmd']['weather']:
		return get_weather()

	if text in comands['cmd']['nutrition']:
		pass