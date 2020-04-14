#numerologia.io python code by ΛNDRΞS

#libraries import
import functools
import re
import math
import datetime
from collections import Counter
from heapq import nsmallest

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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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
            if master(master_value) == True:
                temp = sum([int(i) for i in str(master_value)])
                return [temp, True, master_value]
            else:
                temp = sum([int(i) for i in str(suma)])
                return [temp, False, 0]
        else:
            master_value = sum([int(i) for i in str(suma)])
            if master(master_value) == True:
                temp = sum([int(i) for i in str(master_value)])
                return [temp, True, master_value]
            else:
                final = sum([int(i) for i in str(master_value)])
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
#-------------------------

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
        print(f"Desde Octubre {t_year} hasta Octubre {t_year_plus}, tu ciclo anual es: {today_year_cycle}  ")
    else:
        pre_today_year_cycle = int(birth_vibration[0]) + int(redux_t_year)
        # print(f" Pre no -> NOV/DIC: {pre_today_year_cycle}")
        today_year_cycle = redux(pre_today_year_cycle)
        print(f"Desde Octubre {t_year_minus} hasta Octubre {t_year}, tu ciclo anual es: {today_year_cycle}  ")
    pass

#Function to measure frequency of a list
#-------------------------
def CountFrequency(list):
    # Python3 code using dict.get() to get count of each element in string
    # res = {}
    #
    # for keys in list:
    #     res[keys] = res.get(keys, 0) + 1
    #
    # return res
    # naive method
    all_freq = {}

    for i in list:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    return all_freq

#function to check excess or lack of numbers in your name_count

def numberFrequency(dictionary):
    temp_dictionary = {}
    for i in range(1,10):
        if str(i) in dictionary:
            key = str(i)
            # print("Key exists")
            value = dictionary.get(key)
            # print(f"This is the value found for the key {key} -> {value}")
            temp_dictionary[i] = value

        else:
            # print("Key NOT FOUND")
            temp_dictionary[i] = 0
    return temp_dictionary
#-------------------------
#function to get top 3 frequency numbers
def top(my_dict):
    k = Counter(my_dict)
    high = k.most_common(3)
    return high

#function to get bottom 3 frequency numbers
def bottom(my_dict):
    # ThreeLowest = nsmallest(3, my_dict, key = my_dict.get)
    k = Counter(my_dict)
    ThreeLowest = k.most_common()[:-3-1:-1]
    return ThreeLowest



#-------------------------

# Functions to analyze characters
#-------------------------
#Function to sum the values for each key on the list
def characterSum(list, dict):
    sum = 0
    for i in list:
        # print(f"Key to look for: {i}")
        # print(f" Value: {dict.get(i)}")
        temp = dict.get(i)
        # print(f"Temp is: {type(temp)}")
        sum = sum + temp
        # print(f"Sum is: {type(sum)}")
    return sum

def fullCharacter(dictionary):
    character = {
        'mental' : [1,7,8,9],
        'emotional' : [2,3,6,9],
        'intuitive' : [2,7,9],
        'artistic' : [3,6,9],
        'scientific' : [1,4,5,7,8],
        'business' : [2,4,8],
        'physical' : [4,5,8]
    }
    new_dict = {}
    for i in character:
        # print(i)
        new_dict[i] = characterSum(character.get(i), dictionary)
        # print(new_dict)
    return new_dict

# Functions to analyze 52 day cycles
#-------------------------
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

#-------------------------


#-----------------USER INPUT----------------------
#----------------------
#----------------------

#Welcome
print()
print("-- -- -- -- -- -- -- -- -- --")
print("Bienvenido a numerología.io")
print("-- -- -- -- -- -- -- -- -- --")
print()

input_full_name = input("Escribe tu nombre completo (como en el registro civil): ")
date_input = input("Escribe tu fecha de nacimiento en el formato: DD-MM-YYYY: ")
signature_input = input("Escribe tu firma, o lo que significa para ti: ")


#Birth Date calculations
#----------------------
birth_date = realdate(date_input)
birth_dotw = dotw(birth_date)
birth_doty = doty(birth_date)

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
t_year = str(today_date.year)
today_doty = doty(today_date)
#----------------------


#Name calculations
#----------------------
name_count = stringcount(input_full_name)
#----------------------
interior_values = rem_consonants(input_full_name)
exterior_values = rem_vowel(input_full_name)
#----------------------
calc_name = cypher(input_full_name)
cypher_no_strings = calc_name.replace(" ", "")
name_frequency = CountFrequency(cypher_no_strings)
name_frequency_dictionary = numberFrequency(name_frequency)
excess = top(name_frequency_dictionary)
lack = bottom(name_frequency_dictionary)
sorted_frequency = sorted(name_frequency.items(), reverse=True, key=lambda x: x[1])

#-----Signature calculations
calc_signature = cypher(signature_input)
signaturevalues_nostrings = calc_signature.replace(" ", "")
signature = calsum(signaturevalues_nostrings)

#------Destiny calculations
destiny = birth_vibration
temp_destiny = int(destiny[0])+int(signature[0])
temp_destiny_string = str(temp_destiny)
real_destiny = calsum(temp_destiny_string)

#-----Character calculations

your_character = fullCharacter(name_frequency_dictionary)
character_reading = top(your_character)

#----------------------
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


# ----------Cycle calculations
# today_year_cycle = cycle(today_date, birth_vibration)
today_month_cycle = monthCycle(birth_doty, today_doty)



#Results
#----------------------
print()
print("-- Resultados de consulta --")
print(f"La fecha de hoy en formato AAAA-MM-DD es: {today_date}")
print(f"Naciste en el día {birth_doty} del año {v_year}")
print(f"Hoy es el día {today_doty} del año {t_year}")
print()
print(f"Tu nombre es: {input_full_name}")
print(f"Tu nombre contiene {name_count} letras")
print("Tu nombre representado en números es el siguiente:")
print(calc_name)
# print(type(name_frequency))
# print(name_frequency)
print()
print("Tu nombre contiene la siguiente frecuencia de números:")
# print(name_frequency)
#confirm input is a dictionary
# print(type(name_frequency))
print(name_frequency_dictionary)
print("Exceso de números:")
print(excess)
for elem in excess:
    print(elem[0] , " ::" , elem[1] )
print("Carencia de números:")
print(lack)
for elem in lack:
    print(elem[0] , " ::" , elem[1] )

print()
print(f"Tu puntuación por grupo es: ")
print(your_character)
print(f"Tu caracter se define por los siguientes 3 atributos: ")
print(character_reading)
# print(sorted_frequency)
#Sorted list of pairs = number and frequency
# print(type(sorted_frequency))
# for elem in sorted_frequency:
#     print(elem[0] , " ::" , elem[1] )
print()
print("-- Análisis numerológico de nombre --")
print()
print(interior_redux)
print(list_interior)
print(input_full_name)
print(list_exterior)
print(exterior_redux)
print()
print(f"Tu INTERIOR es {interior}")
print(f"Tu EXTERIOR es {exterior}")
# print(f" Your GOAL is {calc_goals}")
print(f"Tu número de METAS es: {goals}")
print()
print("-- Resultados de Fecha --")
print()
print(f"Naciste el: {birth_date}")
print(f"Era un {birth_dotw}")
# print(type(birth_date))
# print(type(date_list))
# print(v_year)
# print(v_month)
# print(v_day)
# print(redux_year)
# print(redux_month)
# print(redux_day)
# print(date_string)
print(f"Tu vibración de nacimiento es: {birth_vibration}")
cycle(today_date, birth_vibration)
print(f"Te encuentras en el ciclo mensual {today_month_cycle} de 7")
print()
print("Análisis de Firma: ")
# print(calc_signature)
# print(signaturevalues_nostrings)
print(f" Tu firma tiene una vibración: {signature[0]}")
print()
print("-- Análisis de Destino --")
print(f"Tu posible destino es: {destiny[0]}")
print(f"Tu destino REAL es: {real_destiny[0]}")
print()


#Consultation date input
choice = input("Quieres consultar tu ciclo para otra fecha? (s/n): ")
choice = choice.upper()
if choice == 'S':
    #Consult Date calculations
    #----------------------
    consult_date_input = input("Escribe la fecha de consulta: DD-MM-YYYY: ")
    consult_date = realdate(consult_date_input)
    cycle(consult_date, birth_vibration)
    consult_doty = doty(consult_date)
    consult_month_cycle = monthCycle(birth_doty, consult_doty)
    print(f"Ciclo {consult_month_cycle} de 7")
    print(f"Gracias por tu consulta :)")
else:
    #Finish
    #----------------------
    print(f"Gracias por tu consulta :)")
