#number of cars available
cars = 100
#Space in each car
space_in_a_car = 4
#drivers available
drivers = 30
#passangers
passengers = 90
#Cars that are not going to be driven because of lack of drivers
cars_not_driven = cars - drivers 
#Cars that will be driven
cars_driven = drivers
#Total number of people that can be carried
carpool_capacity = cars_driven * space_in_a_car
#Number of persons that can sit in one car
average_person_per_car = passengers/cars_driven

print("There are", cars, "cars available")
print("There will be only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("we need to put about", average_person_per_car, "in each car")