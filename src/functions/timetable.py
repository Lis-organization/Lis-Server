import gspread


def getTimeTable(class_number = 'all', class_letter = 'all'):

	gc =  gspread.service_account('keys/Lisitsa-87bffa742f6e.json')
	sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oE_VShFd_4DY6xynGvxPPkztb2duZoVvOtF6emfTGtI/edit?usp=sharing')
	worksheet = sheet.worksheet('05.11 ЧТ ') # There should be a function with time generation

	value = worksheet.get('J43')

	return value[0]

print(getTimeTable())