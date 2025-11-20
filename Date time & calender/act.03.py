def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental: ", rental_car_cost(6))
print("Cost of hotel stay: ", hotel_cost(4))
print("Cost of plane ride: ", plane_ride_cost("Tampa"))

print("Total trip cost: ", trip_cost("Los Angeles", 5, 600))

print(trip_cost("Trampa", 3, 100))