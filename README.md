# Simple Unit Converter
## Description
This code is a simple unit converter that converts between different units of measurements. The units of measurements supported in this code are:
1.	Inches to Feet
2.	Feet to Inches
3.	Miles to Kilometers
4.	Kilometers to Miles
5.	Celsius to Fahrenheit
6.	Fahrenheit to Celsius

## Requirements
To run this code, you need to have Python installed on your machine.

## Usage
1.	Open the terminal or command prompt and navigate to the directory where the code is saved.
2.	Type the following command and press enter: python <filename>.py
3.	The code will display a list of available conversions.
4.	Select the conversion you want to perform from the list.
5.	Enter the value in the base unit that you want to convert.
6.	The code will perform the conversion and display the result.
## Code Overview
The code consists of six functions that perform the conversions between different units of measurements:

1.	inch_to_feet: This function converts inches to feet.
2.	feet_to_inch: This function converts feet to inches.
3.	mile_to_kilometer: This function converts miles to kilometers.
4.	kilometer_to_mile: This function converts kilometers to miles.
5.	celsius_to_fahrenheit: This function converts Celsius to Fahrenheit.
6.	fahrenheit_to_celsius: This function converts Fahrenheit to Celsius.
  
The code also defines a dictionary named conversion that maps the available conversions to their corresponding functions. 
The code then prompts the user to select a conversion from the list and enters the value in the base unit. The code uses the conversion.get() method to retrieve the function that performs the selected conversion and stores it in the operation variable.
If the operation variable and the value entered by the user are not None, the code calls the function with the value as an argument and displays the result.

## Error Handling
The code has basic error handling to ensure that the user inputs a valid number. If the user inputs an invalid value, the code displays an error message.
## Contributions
Contributions to this code are welcome. If you find any bugs or have suggestions for improvements, please create a pull request or open an issue.
## License
This code is open-source. It is free to use for educational purposes.
## Author
This program is created by xzebcex.
## Conclusion
This code provides a simple and easy-to-use interface for converting between different units of measurements. The code is well commented and easy to understand, making it suitable for use as a starting point for more complex projects or as a reference for learning.
