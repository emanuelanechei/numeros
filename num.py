import datetime

class Person:
    def __init__(self, full_name, birth_date):
        self.full_name = full_name
        self.birth_date = birth_date
        self.alpha = {
            'A':1,'Á':1,'Ä':1,  'J':1, 'S':1,'Š':1,
            'B':2, 'K':2, 'T':2, 'Ť':2,
            'C':3, 'Č':3, 'Ç':3, 'L':3, 'U':3, 'Ú':3, 'Ů':3,
            'D':4, 'Ď':4, 'M':4, 'V':4,
            'E':5, 'É':5, 'Ě':5,'N':5,'Ň':5, 'W':5,'Ö':5,
            'F':6, 'O':6,'Ó':6, 'X':6,
            'G':7, 'P':7, 'Y':7, 'Ý':7,
            'H':8, 'Q':8, 'Z':8,'Ž':8,
            'I':9,'Í':9, 'Ü':9, 'R':9, 'Ř':9, ' ':' '}

    def dotw(self):
        dotw = self.birth_date.strftime("%A")
        return dotw

    def master(value):
        number = int(value)
        if number == 11 or number == 22 or number == 33 or number == 44:
            ismaster = True
            return ismaster
        else:  # Numbers 11, 22, 33 or 44 should not be reduced.
            ismaster = False
            return ismaster





#Welcome
print("Bienvenido a numerología.io")
print()

#Birth Date input
#----------------------
input_full_name = input("Escribe tu nombre completo (cómo en el registro civil): ")
date_entry = input("Escribe tu fecha de nacimiento en el formato: DD-MM-YYYY: ")
#Date calculations
day, month, year = map(int, date_entry.split('-'))
birth_date = datetime.date(year, month, day)
dotw_birth = person.dotw()

person = Person(input_full_name, birth_date)
print(person.dotw())

print(day)
print(month)
print(year)
print(birth_date)
print(f" Nombre introducido es: {person.full_name}")
print(f" Tu fecha de nacimiento es: {person.birth_date}")
