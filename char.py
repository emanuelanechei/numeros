#This is the test function to create a dictionary with each character value

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
        print(i)
        new_dict[i] = characterSum(character.get(i), dictionary)
        # print(new_dict)
    return new_dict


# printing sum
mental = [5,7,1,9]
you = {1: 7, 2: 0, 3: 1, 4: 3, 5: 2, 6: 6, 7: 0, 8: 0, 9: 7}
mental_sum = characterSum(mental, you)
print(f"The character amount is: {mental_sum}")
your_character = fullCharacter(you)
print(your_character)
