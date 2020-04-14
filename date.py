import datetime

def realdate(string):
    day, month, year = map(int, string.split('-'))
    birth_date = datetime.date(year, month, day)
    return birth_date

def doty(calendar):
    day_of_year = calendar.timetuple().tm_yday
    return day_of_year

today = datetime.datetime.now()
print(today)
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)

date_input = input("Escribe tu fecha de nacimiento en el formato: DD-MM-YYYY: ")
birth_date = realdate(date_input)
doty_calc = doty(birth_date)
print(birth_date)
print(doty_calc)
