"""
print ("You wake up in the morning and check the weather.")
print ("Depending on the weather you will ski or climb today.")

weather_forecast = input("How does it look? ")

if weather_forecast == "cold":
    print ("Ski today.")
elif weather_forecast == "warm":
    print ("Climb today.")
elif weather_forecast == "rain":
    print ("Stay inside.")
else:
    print ("Go to work.")
"""

"""
temp_today = int(input("What is the temp today? "))

if temp_today <= 32:
    print ("Cold")
elif temp_today > 32:
    print ("Not Cold")
"""

tiemps = int(input("What are the tiemps today?: "))

if tiemps <= 20:
    print ("Really Cold")
elif tiemps > 20 and tiemps <=40: #checks for value in between 20 and 40. Use and, not or here
    print ("Its tiemps")
else:
    print ("Not tiemps")
