import datetime
import math

def realdate(string):
    day, month, year = map(int, string.split('-'))
    birth_date = datetime.date(year, month, day)
    return birth_date

def doty(calendar):
    day_of_year = calendar.timetuple().tm_yday
    return day_of_year

def monthCycle(birth_doty, query_doty):
    if birth_doty > query_doty:
        x = 365 - int(birth_doty)
        y = x + int(query_doty)
        m_cycle = math.ceil(y/52.14)
    else:
        y = int(query_doty) - int(birth_doty)
        m_cycle = math.ceil(y/52.14)
    return m_cycle



today = datetime.datetime.now()
print(today)
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)

date_input = input("Escribe tu fecha de nacimiento en el formato: DD-MM-YYYY: ")
birth_date = realdate(date_input)
doty_calc = doty(birth_date)
print(birth_date)
print(doty_calc)
cycle = monthCycle(doty_calc, day_of_year)
print(cycle)
