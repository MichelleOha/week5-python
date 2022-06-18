# A person needs 800g of trail mix per day to stay in fighting fit shape.
# A person needs 2L of water per day to survive in the desert.
# A post-apocalyptic truck needs 23L/100km of Guzzoline to drive.
# The journey from Brisbane to Perth is 4500km.
# We can travel at a max of 65km/hr
# We can drive for 14hrs per day before we need to rest.

# setting values (constant variable (in all upper case) meaning assign a value and won't change)
FOOD_PER_DAY = 0.8  # LITRES
WATER_PER_DAY = 2.0  # LITRES
FUEL_EFFICIENCY = 0.23  # (23L/100KM)
DISTANCE = 4500.0  # KM
MAX_SPEED = 65.0  # KM PER HOUR
HOURS_TRAVELED_PER_DAY = 14.0  # HOURS

# (true variables as they will change (in lower case)) input from user (need to convert to float or int so it works it out as a number not a string) (every line is a statement)
# expression after the f
quantity_of_food = float(input("How much trail mix do you have in kilos?: "))
quantity_of_water = float(input("How much water do you have in Litres?: "))
quantity_of_fuel = float(input("How much fuel do you have in Litres?: "))
number_of_people = int(input("How much people are in your party?: "))

# work out how many of each thing you will now need to make the journey
# days traveled not treated as a constant as we are calculating this, it's not given to us like above, true variable)
days_traveled = DISTANCE / (MAX_SPEED * HOURS_TRAVELED_PER_DAY)

food_required = number_of_people * FOOD_PER_DAY * days_traveled
water_required = number_of_people * WATER_PER_DAY * days_traveled
fuel_required = DISTANCE * FUEL_EFFICIENCY

# what you actually need to achieve this trip
print(
    f"Days required: {days_traveled}\nFood required: {fuel_required}\nWater required: {water_required}")

# feedback to the user, if they have enough of everything to make the trip
print(f"Sufficient fuel: {quantity_of_fuel >= fuel_required}")
print(f"Sufficient water: {quantity_of_water >= water_required}")
print(f"Sufficient food?: {quantity_of_food >= food_required}")
