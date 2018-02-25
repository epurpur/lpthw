tempc = int(input("What is the temperature in Celsius? "))

tempf = (tempc * (9/5) + 32)

print (f"The temp in fahrenheit is {tempf}")

tempk = ((tempf + 459.67) * (5/9))

print (f"The temp in kelvin is {tempk}")

tempf = int(input("What is the temperature in Fahrenheit? "))

tempc = (tempf - 32) * (5/9)

print (f"The temp in celsius is {tempc}")

tempk = tempc + 272.15

print (f"The temp in kelvin is {tempk}")
