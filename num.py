#libraries import
import functools
import re

def master(value):
    number = int(value)
    if number == 11 or number == 22 or number == 33 or number == 44:
        ismaster = True
        return ismaster
    else:  # Numbers 11, 22, 33 or 44 should not be reduced.
        ismaster = False
        return ismaster

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




input_number = input("Type numbers: ")

# master = master(input_number)
sum = calsum(input_number)
print(sum)
