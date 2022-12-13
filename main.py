import math as m


# BaseToBasePy
# ThatRobster 2022/12/13

# Ew python

def main():
    ##
    # Get the inputs
    ##
    while True:
        starting_base = input("Enter the current base of the number (in decimal numbers): ")
        # Check if the number is a valid number, if so, escape out of the while loop.
        if isint(starting_base):
            break
        print("That is not a valid base! Type the number of the base in base10!")

    while True:
        desired_base = input("Enter the base you would like the number to be: ")
        # Check if the number is a valid number, if so, escape out of the while loop.
        if isint(desired_base):
            break
        print("That is not a valid base! Type the number of the base in base10!")

    num = input("Enter the number in the format of base" + str(starting_base) + ": ")
    print("---------------")
    base10 = anytodecimal(starting_base, num)
    print("Decimal: " + str(base10))
    new_number = decimaltoany(desired_base, base10)
    print("Base" + desired_base + ": " + new_number)
    input("---------------")
    for i in range(5):
        print(" ")


# Converts any decimal number to any other base. It can only have decimals as input, because thats much easier
def decimaltoany(newbase, num):
    ##
    # Get the number of digits needed to write this number
    ##

    # We loop through i, to find the number of decimals needed.
    # When newbase^i > num for the first time, then i must be the amount of needed digits
    escape = False
    digits_total = 0
    while not escape:
        digits_total += 1
        # If this is true, digits_total must be.. well.. the amount of needed digits
        if m.pow(int(newbase), digits_total) > num:
            escape = True
            digits_total -= 1

    ##
    # Convert the characters, starting at the end
    ##

    # Now we loop down through digits_total, and keep a running total.
    digit = digits_total
    running_total = num
    newNumber = ""
    while not digit == -1:
        # If the minimum value of this digit (newbase^digit) is bigger than the total left, the digit must be 0.
        if m.pow(int(newbase), digit) > running_total:
            newNumber += getvaluechar(0)
        else:
            # The number at this digit must be the number of times the running total is greater than newbase^digit,
            # floored.
            unfloored = running_total / (m.pow(int(newbase), digit))
            floored = m.floor(unfloored)
            newNumber += getvaluechar(floored)

            # Remove the amount that we just put in newNumber from the running total
            running_total -= floored * m.pow(int(newbase), digit)
        digit -= 1

    return newNumber


# Converts a number from any base to decimal, to make it easier to calculate with (Since its now an integer)
def anytodecimal(base, number):
    ##
    # Multiply each characters individual value by the base to the power of the digit, to get the number in base10
    # format.
    ##

    # Get an array of all the characters in the number-string
    InvertedCharArray = [char for char in number]
    InvertedCharArray.reverse()
    # Keep a running total, after the loop this will be the total in decimal
    RunningTotal = 0
    # Loop through all the chars
    for i in range(len(InvertedCharArray)):
        # Get the worth of the character on its own
        CharVal = getcharvalue(InvertedCharArray[i])
        # Offset that amount by the amount of digits before the number. Basically adding 0's to the end of the number
        RunningTotal += CharVal * m.pow(int(base), i)
    # Return the total
    return RunningTotal


def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def getvaluechar(value):
    if value == 0:
        return "0"
    elif value == 1:
        return "1"
    elif value == 2:
        return "2"
    elif value == 3:
        return "3"
    elif value == 4:
        return "4"
    elif value == 5:
        return "5"
    elif value == 6:
        return "6"
    elif value == 7:
        return "7"
    elif value == 8:
        return "8"
    elif value == 9:
        return "9"
    elif value == 10:
        return "A"
    elif value == 11:
        return "B"
    elif value == 12:
        return "C"
    elif value == 13:
        return "D"
    elif value == 14:
        return "E"
    elif value == 15:
        return "F"
    else:
        print("Unknown value: " + value)
        return "X"


def getcharvalue(char):
    if char == "0":
        return 0
    elif char == "1":
        return 1
    elif char == "2":
        return 2
    elif char == "3":
        return 3
    elif char == "4":
        return 4
    elif char == "5":
        return 5
    elif char == "6":
        return 6
    elif char == "7":
        return 7
    elif char == "8":
        return 8
    elif char == "9":
        return 9
    elif char == "A":
        return 10
    elif char == "B":
        return 11
    elif char == "C":
        return 12
    elif char == "D":
        return 13
    elif char == "E":
        return 14
    elif char == "F":
        return 15
    else:
        print("Unknown character: " + char)
        return 0


while True:
    main()
