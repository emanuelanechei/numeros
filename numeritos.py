#!/usr/bin/python3


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.calcTable = {'A':1,'Á':1,  'J':1, 'S':1,'Š':1,  'B':2, 'K':2, 'T':2, 'Ť':2,'C':3, 'Č':3, 'L':3, 'U':3, 'Ú':3, 'Ů':3, 'D':4, 'Ď':4, 'M':4, 'V':4,'E':5, 'É':5, 'Ě':5,
                                    'N':5,'Ň':5, 'W':5,'Ö':5, 'F':6, 'O':6,'Ó':6,  'X':6,'G':7, 'P':7, 'Y':7, 'Ý':7,'H':8, 'Q':8, 'Z':8,'Ž':8,'I':9,'Í':9, 'Ü':9, 'R':9, 'Ř':9}
        self.risks = [7, 16, 25, 34, 52, 61, 70, 79, 88, 92]
        self.highrisks = [29, 40, 43]
        self.problematic = 0

    def gcalc(self, word):
        """Calculate the gross number from the word."""
        word = list(word)
        total = 0
        for letter in word:
            value = self.calcTable[letter]
            total = total + value
        return(total)

    def reduce(self, number):
        """Reduce gross numbers to netto numbers."""
        if number == 11 or number == 22:  # Numbers 11 or 22 should not be reduced.
            total = number
        else:
            total = number
            size = len(str(total))
            if size > 1:
                while size > 1: # Repeats until the number is not fully reduced to one digit only.
                    if total == 11 or total == 22: #Numbers 11 or 22 should not be reduced.
                        break
                    word = str(total)
                    word = list(word)
                    total = 0
                    for letter in word:
                        total = total +int(letter)
                    size = len(str(total))

            else:
                total = number
        return(total)

    def ncalc(self, word):
        """Calculate the netto numbers."""
        word = list(word)
        total = self.gcalc(word)
        total = self.reduce(total)
        return(total)

    def getInNum(self):
        """Return the numeric value of the first letter in a name."""
        nletter = list(self.name)
        nletter = nletter[0]
        total = self.calcTable[nletter]
        return(total)

    def getIsNum(self):
        """Return the numeric values of the first letter in a surname."""
        sletter = list(self.surname)
        sletter = sletter[0]
        total = self.calcTable[sletter]
        return(total)


    def getWest(self):
        """Return the number for the western part of cross."""
        west = self.ncalc(self.name)
        west = self.reduce(west)
        return(west)

    def getEast(self):
        """Return the number for the eastern part of cross."""
        east = self.ncalc(self.surname)
        east = self.reduce(east)
        return(east)

    def getSubNorth(self):
        subnorth = self.getInNum()+self.getIsNum()
        return(subnorth)

    def getNorth(self):
        """Return the personal number."""
        north = self.getSubNorth()
        north = self.reduce(north)
        return(north)

    def getFirst(self):
        """Return the number of the first life trimester."""
        first = self.gcalc(self.name) + self.gcalc(self.surname)
        return(first)

    def getSecond(self):
        """Return the number of the second life trimester."""
        second = self.getNorth() + self.getFirst()
        return(second)

    def getThird(self):
        """Return the number of the third life trimester."""
        third = (self.gcalc(self.name)+self.getSubNorth()) + (self.gcalc(self.surname)+self.getSubNorth())
        return(third)

    def getSouth(self):
        """Return the number in the southern part of cross."""
        south = self.reduce(self.getThird())
        return(south)

    def calcCross(self):
        """Return the values of the horizontal and vertical additions on the cross."""
        horizontal = self.getWest()+self.getEast()
        vertical = self.getNorth()+self.getSouth()
        middle = horizontal + vertical
        return(horizontal,vertical,middle)

    def getLowest(self):
        number = self.getThird()
        size = len(str(number))
        if size > 1:
            number = list(str(number))
            total = 0
            for num in number:
                total = total + int(num)
        else:
            total = number
        return(total)

    def getRisk(self,number):
        """Find out whether a number is a risk number."""
        if number in self.risks:
            risk = '!'
        elif number in self.highrisks:
            risk = 'X'
        else:
            risk = ''
        return(risk)

    def getFlow(self, number):
        """Find out whether there is an energy leak."""
        if number == 8:
            flow = 'EF'
        elif number%8 == 0:
            flow = 'PEF'
        else:
            flow = ''
        return(flow)

class PrintCross:
    """Print out all values in the cross (no background though)."""
    def __init__(self, person):
        self.person = person

    def printCross(self):
        print('                            {}                                '.format(self.person.getNorth()))
        print('                                                               ')
        print('               {}                           {}                 '.format(self.person.getInNum(), self.person.getIsNum()))
        print('                                                              ')
        print('{}                                                           {}'.format(self.person.getWest(), self.person.getEast()))
        print('                            {}                               '.format(self.person.getFirst()))
        print('                                                           ')
        print('             {}            {}             {}                 '.format(self.person.gcalc(name), self.person.getSecond(), self.person.gcalc(surname)))
        print('                                                            ')
        print('                            {}                               '.format(self.person.getThird()))
        print('                                                             ')
        print('               {}                         {}                 '.format((self.person.gcalc(name)+self.person.getNorth()), (self.person.gcalc(surname)+self.person.getNorth())))
        print('                            {}                               '.format(self.person.getLowest()))
        print('                                                             ')
        print('                            {}                               '.format(self.person.getSouth()))

class PrintNums:
    def __init__(self, person):
        self.person = person

    def printNums(self):
        print("Name calculation:",self.person.name, self.person.surname)
        print("=============================================================")
        print("Gross sum of name:", self.person.gcalc(name), self.person.getRisk(self.person.gcalc(name)))
        print("Gross sum of lastname:", self.person.gcalc(surname), self.person.getRisk(self.person.gcalc(surname)))
        print("-------------------------------------------------------------")
        print("West:", self.person.getWest(), self.person.getRisk(self.person.getWest()))
        print("East:", self.person.getEast(), self.person.getRisk(self.person.getEast()))
        print("North:", self.person.getNorth(), self.person.getRisk(self.person.getNorth()))
        print("South:", self.person.getSouth(), self.person.getRisk(self.person.getSouth()))
        print("-------------------------------------------------------------")
        print("Name Reduced: ", self.person.getInNum(), self.person.getRisk(self.person.getInNum()))
        print("Last Name Reduced: ", self.person.getIsNum(), self.person.getRisk(self.person.getIsNum()))
        print("Personality: ",self.person.getSubNorth(),self.person.getRisk(self.person.getSubNorth()))
        print("-------------------------------------------------------------")
        print("Number of the first phase of life: ", self.person.getFirst(), self.person.getRisk(self.person.getFirst()))
        print("Number of the second phase of life: ", self.person.getSecond(), self.person.getRisk(self.person.getSecond()))
        print("Number of the third phase of life: ", self.person.getThird(), self.person.getRisk(self.person.getThird()))
        print("Auxilary number: ", self.person.getLowest(), self.person.getRisk(self.person.getLowest()))
        print("-------------------------------------------------------------")
        kname = self.person.gcalc(name)+self.person.getSubNorth()
        ksurname = (self.person.gcalc(surname)+self.person.getSubNorth())
        print("Name and personality combination number (bottom left):", kname, self.person.getRisk(kname))
        print("Surname and personality combination number (bottom right):", ksurname, self.person.getRisk(ksurname))
        print("-------------------------------------------------------------")
        hor, ver, sum = self.person.calcCross()
        print("Horizontal calculation of the cross: ", hor, self.person.getRisk(hor), self.person.getFlow(hor))
        print("Vertical calculation of the cross: ", ver, self.person.getRisk(ver), self.person.getFlow(ver))
        print("Sum of the cross: ", sum, self.person.getRisk(sum), self.person.getFlow(sum))
        print("=============================================================")


incoming = input("Enter your first and last name (John Doe): ")
incoming = incoming.upper()
incoming = incoming.split(" ")

name = incoming[0]
surname = incoming[1]

person = Person(name, surname)
calculation = PrintNums(person)
calculation.printNums()

choice = input("Do you want to display a cross for this name?? (y/n): ")
choice = choice.upper()
if choice == 'Y':
    cross = PrintCross(person)
    cross.printCross()
else:
    pass
