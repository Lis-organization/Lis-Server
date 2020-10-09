import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keys/lisitsa-291010-086e2c1d680b.json', scope)
client = gspread.authorize(creds)
sheet = client.open('dddd').sheet1

telemedicine = sheet.get_all_records() # Получение всех записей в таблице
print(telemedicine)