#numerologia.io python code by ΛNDRΞS

#libraries import
import functools
import re
import datetime

#Dictionary
alpha = {
    'A':1,'Á':1,'Ä':1,  'J':1, 'S':1,'Š':1,
    'B':2, 'K':2, 'T':2, 'Ť':2,
    'C':3, 'Č':3, 'Ç':3, 'L':3, 'U':3, 'Ú':3, 'Ů':3,
    'D':4, 'Ď':4, 'M':4, 'V':4,
    'E':5, 'É':5, 'Ě':5,'N':5,'Ň':5, 'W':5,'Ö':5,
    'F':6, 'O':6,'Ó':6, 'X':6,
    'G':7, 'P':7, 'Y':7, 'Ý':7,
    'H':8, 'Q':8, 'Z':8,'Ž':8,
    'I':9,'Í':9, 'Ü':9, 'R':9, 'Ř':9, ' ':' '}

#Function to replace characters in a word with the value
def cypher(words):
    result = words.upper()
    result = [alpha[i] for i in result]
    strings = [str(x) for x in result]
    a_string = "".join(strings)
    # an_integer = int(a_string)
    return a_string

#Function to check is there's a Master Value
def master(value):
    number = int(value)
    if number == 11 or number == 22 or number == 33 or number == 44:
        ismaster = True
        return ismaster
    else:  # Numbers 11, 22, 33 or 44 should not be reduced.
        ismaster = False
        return ismaster

#Function for simple sum
def redux(value):
    redux = sum([int(i) for i in str(value)])
    while int(redux) > 9:
        redux = sum([int(i) for i in str(redux)])
    return redux

#Function to calculate sum of string
 #1721 -> 11 -> 2
def calsum(value):
    if master(value) == True:
        master_value = sum([int(i) for i in str(value)])
        return [master_value, True, value]
    else:
        suma  = sum([int(i) for i in value])
        if master(suma) == True:
            master_value = sum([int(i) for i in str(suma)])
            return [master_value, True, suma]
        else:
            final = sum([int(i) for i in str(suma)])
            return [final, False, 0]


#Function to remove the vowels of a string
def rem_vowel(string):
    return (re.sub("[aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜůěýŮĚÝ]","",string))

#Function to remove the consonants of a string
def rem_consonants(string):
    return (re.sub("[qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNMčďňřšťžČĎŇŘŠŤŽ]","",string))

#Funcion to reduce each string value

def topo(list):
    for i in list:
        result = [redux(i) for i in list]
        return result

# Function to calculate the sum of a list
def calculin(list):
    y = sum(list)
    if master(y):
        master_value = y
        redux = sum([int(i) for i in str(y)])
        return [redux, True, master_value]
    else:
        redux = calsum(str(y))
        # redux = sum([int(i) for i in str(y)])
        return redux

#Count characters of string withou  spaces
def stringcount(string):
    result = len(string) - string.count(' ')
    return result

def dotw(date):
    dotw = date.strftime("%A")
    return dotw

def realdate(string):
    day, month, year = map(int, string.split('-'))
    birth_date = datetime.date(year, month, day)
    return birth_date

def datecalc(string):
    string = string.split('-')
    return string



#Cycle funtions

def cycle(date, birth_vibration):
    t_year = str(date.year)
    redux_t_year = redux(t_year)
    t_year_plus = int(t_year) + 1
    t_year_minus = int(t_year) - 1
    t_month = str(date.strftime('%m'))
    t_day = str(date.strftime('%d'))
    if (int(t_month) == 11) or (int(t_month) == 12):
        pre_today_year_cycle = int(birth_vibration[0]) + int(redux_t_year) + 1
        # print(f" Pre en NOV/DIC: {pre_today_year_cycle}")
        today_year_cycle = redux(pre_today_year_cycle)
        print(f"From October {t_year} to October {t_year_plus}, your YEAR CYCLE is {today_year_cycle}  ")
    else:
        pre_today_year_cycle = int(birth_vibration[0]) + int(redux_t_year)
        # print(f" Pre no -> NOV/DIC: {pre_today_year_cycle}")
        today_year_cycle = redux(pre_today_year_cycle)
        print(f"From October {t_year_minus} to October {t_year}, your YEAR CYCLE is {today_year_cycle}  ")
    pass



#-----------------USER INPUT----------------------
#----------------------
#----------------------

#Welcome
print()
print("-- -- -- -- -- -- -- -- -- --")
print("Bienvenido a numerología.io")
print("-- -- -- -- -- -- -- -- -- --")
print()

input_full_name = input("Type your full name: ")
date_input = input("Escribe tu fecha de nacimiento en el formato: DD-MM-YYYY: ")
birth_date = realdate(date_input)
birth_dotw = dotw(birth_date)

#Birth Date calculations
#----------------------
v_year = str(birth_date.year)
v_month = str(birth_date.strftime('%m'))
v_day = str(birth_date.strftime('%d'))
#----------------------
redux_year = redux(v_year)
redux_month = redux(v_month)
redux_day = redux(v_day)
#----------------------
date_string = str(redux_year)+str(redux_month)+str(redux_day)
birth_vibration = calsum(date_string)
#----------------------

#Today calculations
#----------------------
today_date = datetime.date.today()
#----------------------

#Cycle for today
#----------------------
# t_year = str(today_date.year)
# redux_t_year = redux(t_year)
# t_year_plus = int(t_year) + 1
# t_year_minus = int(t_year) - 1
# t_month = str(today_date.strftime('%m'))
# t_day = str(today_date.strftime('%d'))
#----------------------

#Name calculations
#----------------------
name_count = stringcount(input_full_name)
interior_values = rem_consonants(input_full_name)
exterior_values = rem_vowel(input_full_name)
#----------------------
calc_name = cypher(input_full_name)
calc_interior = cypher(interior_values)
calc_exterior = cypher(exterior_values)
#----------------------
list_interior = calc_interior.split()
list_exterior = calc_exterior.split()
#----------------------
interior_redux = topo(list_interior)
exterior_redux = topo(list_exterior)
#----------------------
interior = calculin(interior_redux)
exterior = calculin(exterior_redux)
#----------------------
intext = interior[0] + exterior[0]
#----------------------
goals = calsum(str(intext))



#Results
print()
print("-- Resultados de consulta --")
print(f"{today_date}")
print()
print(f"Your name is: {input_full_name}")
print(f"Your name contains {name_count} letters")
print(calc_name)
print()
print(interior_redux)
print(list_interior)
print(input_full_name)
print(list_exterior)
print(exterior_redux)
print()
print(f"Your INTERIOR is {interior}")
print(f"Your EXTERIOR is {exterior}")
# print(f" Your GOAL is {calc_goals}")
print(f"Your GOAL is {goals}")
print()
print("-- Resultados de Fecha --")
print()
print(f"Your birth date is: {birth_date}")
print(f"You where born on a: {birth_dotw}")
# print(type(birth_date))
# print(type(date_list))
# print(v_year)
# print(v_month)
# print(v_day)
# print(redux_year)
# print(redux_month)
# print(redux_day)
# print(date_string)
print(f"Your Vibration is: {birth_vibration}")
cycle(today_date, birth_vibration)

#Consultation date input
choice = input("Do you want to consult a specific date?? (y/n): ")
choice = choice.upper()
if choice == 'Y':
    #Consult Date calculations
    #----------------------
    consult_date_input = input("Escribe la fecha de consulta: DD-MM-YYYY: ")
    consult_date = realdate(consult_date_input)
    cycle(consult_date, birth_vibration)
    print(f"Thank you for your consult!, Come back any time :)")
else:
    #Finish
    #----------------------
    print(f"Thank you for your consult!, Come back any time :)")
