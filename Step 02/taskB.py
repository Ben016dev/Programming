#header

location = input("location: ")
distance = input("Distance (miles) : ")
miles_per_gallon = input("Miles per gallon: ")
gas_price = input("Gas price: ")
people_splitting = input("People splitting cost: ")

average_speed = 55

distance = float(distance)
miles_per_gallon = float(miles_per_gallon)
gas_price = float(gas_price)
people_splitting = float(people_splitting)
full_gallons = float(distance // miles_per_gallon)
remaining_gallon = float(int((distance % miles_per_gallon) / miles_per_gallon * 10) / 10 )
gallons = full_gallons + remaining_gallon
gas_cost = float(int(gallons * gas_price * 100) / 100)
cost_per_person = float(int(gas_cost / people_splitting * 100) / 100 )
time = distance / average_speed * 60
hours = time // 60
remaining_minutes = time % 60
round_trip_gas = float(int(gas_cost * 200) / 100)
gallons = str(gallons)
gas_cost = str(gas_cost)
cost_per_person = str(cost_per_person)
hours = str(int(hours))
remaining_minutes = str(int(remaining_minutes))
average_speed = str(average_speed)
round_trip_gas = str(round_trip_gas)

print("--- Trip to "+ location +" ---")
print("Gallons of gas: " + gallons)
# unsure how you got a different number on the task, when i checked with a calculator this was correct
print("Gas cost: " + gas_cost)
print("Cost per person: " + cost_per_person)
print("Driving time: " + hours + " hr " + remaining_minutes + " min (at " + average_speed + " mph)") 
print("Round trip gas: " + round_trip_gas)
