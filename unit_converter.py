# Simple unit converter.

def inch_to_feet(_in):  # Inch to Feet.
    return _in/12


def feet_to_inch(_ft):  # Feet to Inch.
    return _ft*12


def mile_to_kilometer(_mil):  # Miles to Kilometer.
    return _mil*1.609


def kilometer_to_mile(_km):  # Kilometer to Miles.
    return _km/1.609


def celsius_to_fahrenheit(_cel):  # Celsius to Fahrenheit.
    return 9*_cel/5+32


def fahrenheit_to_celsius(_farh):  # Fahrenheit to Celsius.
    return (_farh-32)*5/9


conversion = {'Inch to Feet': inch_to_feet,
              'Feet to Inch': feet_to_inch,
              'Miles to Kilometer': mile_to_kilometer,
              'Kilometer to Miles': kilometer_to_mile,
              'Celsius to Fahrenheit': celsius_to_fahrenheit,
              'Fahrenheit to Celsius': fahrenheit_to_celsius}

print('Available conversions (to and from):\nInch to Feet, Feet to Inch, Miles to Kilometer, Kilometer to Miles, Celsius to Fahrenheit, Fahrenheit to Celsius')
convert = input('Select from the list: ')

try:
    num = float(input('What is the value in the base unit: '))
except ValueError:
    print('Invalid value input. Please enter a valid number.')
    num = None

operation = conversion.get(convert, None)
if operation and num:
    result = operation(num)
    print(result)
else:
    print('Invalid conversion type selected or invalid value input')
