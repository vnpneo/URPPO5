def convert_to_fahrenheit(celsius):
    c = float(celsius)
    f = c * 9 / 5 + 32
    print('%r Celsius, converted to Fahrenheit, is: %r Fahrenheit.' %(c, f))

def convert_to_celsius(fahrenheit):
    f = float(fahrenheit)
    c = (f - 32) * 5 / 9
    print('%r Fahrenheit, converted to Celsius, is: %r Celsius.' %(f, c))

def convert():
    print('To convert a temperature from Celsius to Fahrenheit:')
    cels = input('CELSIUS: ')
    convert_to_fahrenheit(cels)
    print('')
    print('To convert a temperature from Fahrenheit to Celsius:')
    fahr = input('FAHRENHEIT: ')
    convert_to_celsius(fahr)

convert()