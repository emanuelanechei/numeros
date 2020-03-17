import datetime

#FUNCTIONS--------------
# Function to check values with only one value instead of 2 and reducing
maestros = [11, 22, 33, 44]

def digitcheck(twodigits):

    if len(twodigits) < 2:
        # print(True)
        # print(f"The value has only one digit: {twodigits}")
        value = f"0{twodigits}"
        # print(f"The fixed value is: {value}")
        var = int(value[0]) + int(value[1])

        if var > 9:
            str1 = str(var)
            var2 = int(str1[0]) + int(str1[1])
            # print(f"Sum of Value is greater than 9: {var}")
            # print(f"This is the reduced one: {var2}")
            return(var2)
        else:
            # print(f"Sum of Value is less than 9: {var}")
            return(var)
    else:
        # print(False)
        # print(f"The value has two digit: {twodigits}")
        var = int(twodigits[0]) + int(twodigits[1])

        if var > 9:
            str1 = str(var)
            var2 = int(str1[0]) + int(str1[1])
            # print(f"Sum of Value is greater than 9: {var}")
            # print(f"This is the reduced one: {var2}")
            return(var2)
        else:
            # print(f"Sum of Value is less than 9: {var}")
            return(var)

# END OF FUNCTION

#----------------------
#----------------------

#Welcome
print("Bienvenido a numerología.io")
print()

#Birth Date input
#----------------------
date_entry = input("Escribe tu fecha de nacimiento en el formato: DD-MM-YYYY: ")
#Date calculations
day, month, year = map(int, date_entry.split('-'))
birth_date = datetime.date(year, month, day)
dotw_birth_date = birth_date.strftime("%A")
today_date = datetime.date.today()
#----------------------

#Birth Date calculations
#----------------------
v_year = str(birth_date.year)
v_month = str(birth_date.strftime('%m'))
v_day = str(birth_date.strftime('%d'))
#----------------------

#Consultation date input

date_entry = input("Escribe la fecha de consulta: DD-MM-YYYY: ")
day, month, year = map(int, date_entry.split('-'))
consult_date = datetime.date(year, month, day)

#Consult Date calculations
#----------------------
c_year = str(consult_date.year)
c_year_plus = int(c_year) + 1
c_year_minus = int(c_year) - 1
c_month = str(consult_date.strftime('%m'))
c_day = str(consult_date.strftime('%d'))

pre_calc_sum_c_year = int(c_year[0]) + int(c_year[1]) + int(c_year[2]) + int(c_year[3])
calc_sum_c_year = digitcheck(str(pre_calc_sum_c_year))
#----------------------

#Today Calculations
#----------------------
t_year = str(today_date.year)
t_year_plus = int(t_year) + 1
t_year_minus = int(t_year) - 1
t_month = str(today_date.strftime('%m'))
t_day = str(today_date.strftime('%d'))

pre_calc_sum_t_year = int(t_year[0]) + int(t_year[1]) + int(t_year[2]) + int(t_year[3])
calc_sum_t_year = digitcheck(str(pre_calc_sum_t_year))

#----------------------




pre_calc_sum_year = int(v_year[0]) + int(v_year[1]) + int(v_year[2]) + int(v_year[3])
calc_sum_year = digitcheck(str(pre_calc_sum_year))

calc_sum_month = int(v_month[0]) + int(v_month[1])

calc_sum_day = int(v_day[0]) + int(v_day[1])

pre_calc_sum_total = int(calc_sum_year) + int(calc_sum_month) + int(calc_sum_day)

if (pre_calc_sum_total == 11) or (pre_calc_sum_total == 22) or (pre_calc_sum_total == 33) or (pre_calc_sum_total == 44):
    birth_vibration_master = True
    birth_vibration_master_value = pre_calc_sum_total
    birth_vibration = digitcheck(str(pre_calc_sum_total))
else:
    birth_vibration_master = False
    birth_vibration_master_value = False
    birth_vibration = digitcheck(str(pre_calc_sum_total))



#----------------------

#Name input
# name_entry = input("Escribe tu nombre completo como aparece en tu registro civil: ")

#Results
print()
print("-- Resultados de consulta --")
print(f"Consulta realizada el día: {today_date}")
print()
print(f"Tu fecha de nacimiento es {birth_date}")
print(f"Día de la semana cuando naciste: {dotw_birth_date}")
# print(f"Test de Año {v_year}")
# print(f"Test de mes {v_month}")
# print(f"Test de día {v_day}")
print()
print(f"Año reducido: {pre_calc_sum_year}")
print(f"Número de Año: {calc_sum_year}")
print(f"Número de Mes: {calc_sum_month}")
print(f"Número de Día: {calc_sum_day}")
print(f"TOTAL antes de check maestros: {pre_calc_sum_total}")
print(f"TOTAL post maestros: {birth_vibration}")
print()
print(f"Tu VIBRACIÓN DE NACIMIENTO es: {birth_vibration}")
print(f"¿Tienes una Vibración maestra?: {birth_vibration_master}")
print(f"Tu Vibración maestra es: {birth_vibration_master_value}")
print()
print()
# print(c_year)
# print(pre_calc_sum_c_year)
# print(birth_vibration)
#Consult Results
print(f"Tu ciclo para la fecha: {consult_date}")
print()
if c_month in maestros:
    pre_consult_year_cycle = int(birth_vibration) + int(calc_sum_c_year) + 1
    # print(f" Pre en NOV/DIC: {pre_consult_year_cycle}")
    consult_year_cycle = digitcheck(str(pre_consult_year_cycle))
    print(f"From October {c_year} to October {c_year_plus}, your YEAR CYCLE is {consult_year_cycle}  ")
else:
    pre_consult_year_cycle = int(birth_vibration) + int(calc_sum_c_year)
    # print(f" Pre NO -> NOV/DIC: {pre_consult_year_cycle}")
    consult_year_cycle = digitcheck(str(pre_consult_year_cycle))
    print(f"From October {c_year_minus} to October {c_year}, your YEAR CYCLE is {consult_year_cycle}  ")

print()
print()

#Today Results
print(f"Tu ciclo para hoy: {today_date}")
print()
if (int(t_month) == 11) or (int(t_month) == 12):
    pre_today_year_cycle = int(birth_vibration) + int(calc_sum_t_year) + 1
    # print(f" Pre en NOV/DIC: {pre_today_year_cycle}")
    today_year_cycle = digitcheck(str(pre_today_year_cycle))
    print(f"From October {t_year} to October {t_year_plus}, your YEAR CYCLE is {today_year_cycle}  ")
else:
    pre_today_year_cycle = int(birth_vibration) + int(calc_sum_t_year)
    # print(f" Pre no -> NOV/DIC: {pre_today_year_cycle}")
    today_year_cycle = digitcheck(str(pre_today_year_cycle))
    print(f"From October {t_year_minus} to October {t_year}, your YEAR CYCLE is {today_year_cycle}  ")
