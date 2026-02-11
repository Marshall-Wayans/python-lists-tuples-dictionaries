# create a tuple
Bikes=("Yamaha","Honda","Suzuki","Harley-Davidson")
print(Bikes)

# add a value to a tuple
#Bikes.append("Ducati") # this will raise an error because tuples are immutable
#print(Bikes)

#Bikes.insert(1, "BMW")
#print(Bikes)

# remove a value from a tuple
#Bikes.remove("Honda") # this will raise an error because tuples are immutable
#print(Bikes)

#create a new tuple 
Cars=("Toyota","Honda","Ford","Chevrolet")
print(Cars)

# concatenate two tuples
vehicles=Cars+Bikes
print(vehicles)

# slice a tuple
my_vehicles=Bikes+Cars[::4] 
print(my_vehicles)
