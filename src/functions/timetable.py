import gspread
import datetime


def getTimeTable(class_number = 'all', class_letter = 'all', day='today'):

	gc =  gspread.service_account('keys/Lisitsa-87bffa742f6e.json')
	sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oE_VShFd_4DY6xynGvxPPkztb2duZoVvOtF6emfTGtI/edit?usp=sharing')


	if day == 'today':
		worksheet = sheet.worksheet('05.11 ЧТ ') # There should be a function with time generation

		count = 0
		lessons = []
		teachers = []
		class_places = []
		for i in worksheet.get('A45:S69'):
			print()
			if i[3]:
				if count == 0:
					lesson = i[3]
					count += 1
				elif count == 1:
					teacher = i[3]
					count += 1
				elif count == 2:
					class_place = i[3]
					lessons.append(lesson)
					teachers.append(teacher)
					class_places.append(class_place)

					count = 0
		return lessons



print(getTimeTable())