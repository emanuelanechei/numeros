#libraries import
import functools
import re

alphabets = {
    'A':1,'Á':1,'Ä':1,  'J':1, 'S':1,'Š':1,
    'B':2, 'K':2, 'T':2, 'Ť':2,
    'C':3, 'Č':3, 'Ç':3, 'L':3, 'U':3, 'Ú':3, 'Ů':3,
    'D':4, 'Ď':4, 'M':4, 'V':4,
    'E':5, 'É':5, 'Ě':5,'N':5,'Ň':5, 'W':5,'Ö':5,
    'F':6, 'O':6,'Ó':6, 'X':6,
    'G':7, 'P':7, 'Y':7, 'Ý':7,
    'H':8, 'Q':8, 'Z':8,'Ž':8,
    'I':9,'Í':9, 'Ü':9, 'R':9, 'Ř':9, ' ':0}

#  -- FUNCTIONS

# https://stackoverflow.com/questions/44501933/numerology-how-to-shorten-code/44502584
def numerology(word):
    return functools.reduce(
        lambda a, b: sum(int(digit) for digit in str(a + b)),
        (alphabets[letter] for letter in word.upper()),
        0
    )
#Function to separate words in a sentence
def separate(sentence):
    split = sentence.split()
    return split


#Function to remove the vowels of a string
def rem_vowel(string):
    return (re.sub("[aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜůěýŮĚÝ]","",string))
#Function to remove the consonants of a string
def rem_consonants(string):
    return (re.sub("[qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNMčďňřšťžČĎŇŘŠŤŽ]","",string))


# -------------------------
# ------ User facing ------

input_full_name =input("Type your full name: ") #since i am using python 3 to code this

#Signature block

# signature = input("Type your signature, or what your signature means: ")
# signature_value = numerology(signature)

#Name calculations
name_value = numerology(input_full_name)
name_vowels = rem_consonants(input_full_name)
name_consonants = rem_vowel(input_full_name)
name_count = len(input_full_name) - input_full_name.count(' ')

interior = numerology(name_vowels)
exterior = numerology(name_consonants)

list = (separate(input_full_name))

#Print each word result

for i in list:
    print(numerology(i))

# print (numerology(word))

print(name_consonants)
print(f" Your Vibration is: {name_value}")
print(f" Your Full Name character count is: {name_count}")
print(f" Your consonants name is {name_consonants}")
print(f" Your vowels name is {name_vowels}")
print(f" Your INTERIOR is {interior}")
print(f" Your EXTERIOR is {exterior}")

# print(f" Your Signature number is {signature_value}")
