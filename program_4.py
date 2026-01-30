#Temp Conversion
#Samuel Renneke, 1/30/2026
def temp_conversion(celsius):

    fahrenheit = 1.8*celsius + 32

    return fahrenheit

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    
    # Get the Celsius temperature.
    celsius = float(input("Enter a Celsius temperature: "))
    fahrenheit = temp_conversion(celsius)
    # Display the Fahrenheit temperature.
    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")
