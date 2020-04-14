#Function to check is there's a Master Value
def master(value):
    number = int(value)
    if number == 11 or number == 22 or number == 33 or number == 44:
        ismaster = True
        return ismaster
    else:  # Numbers 11, 22, 33 or 44 should not be reduced.
        ismaster = False
        return ismaster

def calsumdate(value):
    if master(value) == True:
        master_value = sum([int(i) for i in str(value)])
        return [master_value, True, value]
    else:
        string = str(value)
        no_zero_string = string.replace('0', '')
        # print(type(no_zero_string))
        # print(no_zero_string)
        redux = sum([int(i) for i in str(no_zero_string)])
        # print(type(redux))
        # print(redux)
        # return redux
        # redux_string = str(redux)
        while redux > 99:
            redux = sum([int(i) for i in str(redux)])
        print(redux)
        if master(redux) == True:
            master_value = sum([int(i) for i in str(redux)])
            return [master_value, True, redux]
        else:
            master_value = sum([int(i) for i in str(redux)])
            if master(master_value) == True:
                redux = sum([int(i) for i in str(master_value)])
                return [master_value, True, redux]
            else:
                redux = sum([int(i) for i in str(master_value)])
                return [redux, False, 0]


mval = 19891010
val = 22
yes_master = calsumdate(mval)
print(yes_master)
no_master = calsumdate(val)
print(no_master)
