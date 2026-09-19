cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("We have", cars, "cars")
print("Only", drivers, "drivers have came to job today")
print("So,", cars_not_driven, "cars are empty")
print("We can transfer", carpool_capacity, "persons today")
print("We have to transfer", passengers, "persons today")
print("Every car will contain about", average_passengers_per_car, "persons")
