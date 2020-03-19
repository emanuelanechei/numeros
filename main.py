#libraries import
import functools
import re

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
    # if int(redux) > 9:
    #     redux = sum([int(i) for i in str(redux)])
    #     return redux
    # else:
    #     return redux

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

#Function to replace characters in a word with the value
def cypher(words):
    result = words.upper()
    result = [alpha[i] for i in result]
    strings = [str(x) for x in result]
    a_string = "".join(strings)
    # an_integer = int(a_string)
    return a_string
#Funcion to reduce each string value

def topo(list):
    for i in list_interior:
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

#-----------------USER INPUT----------------------


input_full_name = input("Type your full name: ")
name_count = len(input_full_name) - input_full_name.count(' ')
interior_values = rem_consonants(input_full_name)
exterior_values = rem_vowel(input_full_name)
# interior = calsum(interior_values)
# exterior = calsum(exterior_values)

# calc = cypher(input_full_name)
calc_name = cypher(input_full_name)
calc_interior = cypher(interior_values)
calc_exterior = cypher(exterior_values)
list_interior = calc_interior.split()
list_exterior = calc_exterior.split()
interior_redux = topo(list_interior)
exterior_redux = topo(list_exterior)
interior = calculin(interior_redux)
exterior = calculin(exterior_redux)
intext = interior[0] + exterior[0]
# calc_goals = [int(i) for i in str(intext)]
# goals = sum([int(i) for i in str(calc_goals)])
goals = calsum(str(intext))

# number = numerology(input_full_name)
# input_number = input("Type numbers: ")
# sum = digit_sum(input_number)

#Results
print()
print("-- Resultados de consulta --")
print(input_full_name)
print(f" Your name contains {name_count} letters")
print(calc_name)
print()
print(interior_redux)
print(list_interior)
print(input_full_name)
print(list_exterior)
print(exterior_redux)
print()
print(f" Your INTERIOR is {interior}")
print(f" Your EXTERIOR is {exterior}")
# print(f" Your GOAL is {calc_goals}")
print(f" Your GOAL is {goals}")
# print(sum)
