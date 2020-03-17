import functools
alphabets = {
    'A':1,'Á':1,'Ä':1,  'J':1, 'S':1,'Š':1,
    'B':2, 'K':2, 'T':2, 'Ť':2,
    'C':3, 'Č':3, 'L':3, 'U':3, 'Ú':3, 'Ů':3,
    'D':4, 'Ď':4, 'M':4, 'V':4,
    'E':5, 'É':5, 'Ě':5,'N':5,'Ň':5, 'W':5,'Ö':5,
    'F':6, 'O':6,'Ó':6, 'X':6,
    'G':7, 'P':7, 'Y':7, 'Ý':7,
    'H':8, 'Q':8, 'Z':8,'Ž':8,
    'I':9,'Í':9, 'Ü':9, 'R':9, 'Ř':9}

# def digit_sum(n):
#     #prepare a list of numbers in n convert to string and reconvert
#     numbers=[]
#     for digit in str(n):
#         numbers.append(int(digit))
#     # add up the total of numbers
#     total=0
#     for number in numbers:
#         total += number
#     return total
#
# def numerology(word):
#         total = 0
#         for letter in word.upper():
#             total += alphabets[letter]
#             total = digit_sum(total)
#
#         return total

def numerology(word):
    return functools.reduce(
        lambda a, b: sum(int(digit) for digit in str(a + b)),
        (alphabets[letter] for letter in word.upper()),
        0
    )

def separate(sentence):
    split = sentence.split()
    return split

word =input("Type your word: ") #since i am using python 3 to code this
list = (separate(word))
for i in list:
    print(numerology(i))
# print (numerology(word))
