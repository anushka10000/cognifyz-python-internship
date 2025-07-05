def convert_temperature():
    temp = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C/F): ").upper()

    if unit == 'C':
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is {fahrenheit}°F")
    elif unit == 'F':
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is {celsius}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
convert_temperature()