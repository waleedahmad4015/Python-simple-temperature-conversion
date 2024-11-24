
# Temperature Conversion Program

This is a Python program that converts temperatures between Celsius and Fahrenheit. The user is prompted to input the current temperature and specify whether it's in Celsius or Fahrenheit. The program then converts the temperature to the opposite unit and displays the result.

## Features
- Converts temperature from **Celsius** to **Fahrenheit**.
- Converts temperature from **Fahrenheit** to **Celsius**.
- Validates user input to ensure the correct format for units.

## How to Use
1. Run the program in a Python environment (Python 3.x recommended).
2. When prompted, enter the unit of the temperature (C for Celsius or F for Fahrenheit).
3. Enter the temperature value you want to convert.
4. The program will display the converted temperature.

### Example:

```bash
Is this temperature in celsius or fahrenheit (C / F) ? : C
Enter the temperature ? : 25
Your Temperature in fahrenheit is 77.0°F
```

## Code Explanation
1. **Input**: The program asks the user to input the temperature unit (either `C` for Celsius or `F` for Fahrenheit).
2. **Temperature Conversion**:
   - If the unit is Celsius (`C` or `c`), it converts the temperature to Fahrenheit using the formula:
     \[
     F = \left( \frac{9}{5} \times C \right) + 32
     \]
   - If the unit is Fahrenheit (`F` or `f`), it converts the temperature to Celsius using the formula:
     \[
     C = \left( F - 32 \right) \times \frac{5}{9}
     \]
3. **Validation**: If the input unit is neither `C`, `c`, `F`, nor `f`, the program will notify the user that the input is invalid.

## Example Code:

```python
unit = input("Is this temperature in celsius or fahrenheit (C / F) ? : ")
temp = float(input("Enter the temperature ? : "))

if unit != "C" and unit != "c" and unit != "f" and unit != "F":
    print(f'"{unit} is not valid"')
else:
    if unit == "c" or unit == "C":
        temp = round(((9 * temp) / 5 + 32), 1)
        print(f"Your Temperature in fahrenheit is {temp}°F")
    if unit == "f" or unit == "F":
        temp = round(((temp - 32) * 5 / 9), 1)
        print(f"Your Temperature in celsius is {temp}°C")
```

## Requirements
- Python 3.x or higher.

## License
This program is licensed under the MIT License.
