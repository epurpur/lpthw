#write two functions: c2f and f2c. f2c should accept as a paremeter a temperature in Fahrenheit and
#return the corresponding temperature in Celsius. c2f should accpet as a parameter a temperature
#in Celsius and return the corresponding temperature in Fahrenheit
#Neither function should print anything nor ask for any input. You should not have any code outside these two functions

def celsius_to_fahrenheit(temp_input):
    tempf = (temp_input * (9/5) + 32)
    print (f"The temp in fahrenheit is {tempf}")

def fahrenheit_to_celsius(temp_input):
    tempc = (temp_input - 32) * (5/9)
    print (f"The temp in celsius is {tempc}")
