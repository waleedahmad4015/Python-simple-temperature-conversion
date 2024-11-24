# Temperature conversion program

unit = input("Is this temperature in celsius or fahrenheit (C / F) ? : ")
temp = float(input("Enter the temperature ? : "))

if unit != "C" and unit != "c" and unit != "f" and unit != "F" :
    print(f'"{unit} is not valid"')
else:
    if unit == "c" or unit == "C":
        temp = round(((9 * temp) / 5 + 32 ) , 1)
        print(f"Your Temperature in fahrenheit is {temp}°F")
    if unit == "f" or unit == "F":
        temp = round(((temp - 32) * 5 /9 ) , 1)
        print(f"Your Temperature in celsius is {temp}°C")
