from heapq import nlargest

#function to check excess or lack of numbers in your name_count
dict = {'1':8, '2':2, '3':15, '9':6}

def lackorexcess(dictionary):
    # temp_dictionary = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0,'7':0,'8':0 ,'9':0}
    temp_dictionary = {}
    for i in range(1,10):
        if str(i) in dictionary:
            key = str(i)
            print("Key exists")
            value = dictionary.get(key)
            print(f"This is the value found for the key {key} -> {value}")
            # print(f"This is the key we are looking: {key}")
            temp_dictionary[i] = str(value)
            # temp_dictionary.update(key = value)
            print(i)

        else:
            # temp_dictionary.update(i= 0)
            print(i)
            print("Key NOT FOUND")
            temp_dictionary[i] = "0"
    return temp_dictionary

#function to get top 3 frequency numbers
def top(my_dict):
    # k = Counter(my_dict)
    # high = k.most_common(3)
    ThreeHighest = nlargest(3, my_dict, key = my_dict.get)
    return ThreeHighest

result = lackorexcess(dict)
print(result)
print(top(result))
