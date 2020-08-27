###########################################################
#  Computer Project #1
#    Algorithm
#       prompt for a number of rods
#       input a number
#       convert number to a float
#       convert float number of rods to meters
#       convert float number of rods to feet
#       convert float number of rods to miles
#       convert float number of rods to furlongs
#       convert float number of rods to minutes
###########################################################

input_rods = input("Input rods: ") #variable to get num of rods from user
float_rods = float(input_rods) #convert number to a float

print("You input", float_rods, "rods.") 
print() #skip line
print("Conversions")

float_meters = float_rods * 5.0292 #convert rods to meters
rounded_meters = round(float_meters, 3) #round meters 3 decimals
print("Meters:", rounded_meters)

float_feet = float_meters / 0.3048 #convert rods to feet 
rounded_feet = round(float_feet, 3) #round feet 3 decimlas
print("Feet:", rounded_feet)

float_miles = float_meters / 1609.34 #convert rods to miles
rounded_miles = round(float_miles, 3) #round miles 3 decimals
print("Miles:", rounded_miles)

float_furlongs = float_rods / 40 #convert rods to furlongs
rounded_furlongs = round(float_furlongs, 3) #round furlongs 3 decimals
print("Furlongs:", rounded_furlongs)

float_minutes = (float_miles / 3.1) * 60 #convert rods to minutes
rounded_minutes = round(float_minutes, 3) #round minutes 3 decimals
print("Minutes to walk", float_rods, "rods:", rounded_minutes)