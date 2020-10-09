import csv
from datetime import datetime

OUTPUT_PATH = 'outputs/'


def nutrition(free, paysites):
	with open('outputs/nutrition.csv') as csvfile:
		field_names = ['Date', 'Free/Paysites']
		writer = csv.DictWriter(csvfile, fieldnames=field_names)

		writer.writeheader()
		writer.writerow({'Date': datetime.now().date(), 'Free/Paysites': f'{free}/{paysites}'})