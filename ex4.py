cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
#take out cars_driven?
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#cars = 100. there are 100 cars
print ("There are", cars, "cars available.")
#drivers = 30. There are 30 drivers
print ("There are only", drivers, "drivers available.")
#cars_not_driven = cars - drivers. 100-30 = 70
print ("There will be", cars_not_driven, "empty cars today.")
#carpool_capacity = cars_driven(30) x drivers(4)
print ("We can transport", carpool_capacity, "people today.")
#passengers(90)
print ("We have", passengers, "people to carpool today.")
#passengers(90) / cars_driven(30) = 3
print ("We need to put about", average_passengers_per_car, "in each car.")

#Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined
#Error here is due to mispelled 'carpool_capacity' as 'car_pool_capacity'
