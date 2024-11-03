# Objective: The aim of this assignment is to deepen your understanding of tuples in Python.
# Task 1: 
# Formatting Flight Itineraries
#  Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:"Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"


def formatted_flights():
    print("Please Enter Information as needed")
    flight_info = []
    itinerary = 0
    while True:
        traveler_name = input("Enter Your Name(Or Enter Done): ")

        if traveler_name.lower() == "done":
            break
        
        origin = input("Enter Current Location: ")
        destination = input("Enter Where You Are Going: ")
        
        flight_info.append((traveler_name,origin,destination))
        
        itinerary += 1
        print(f"Itinerary {itinerary}: {traveler_name} - From {origin} to {destination}")
    return flight_info


    

formatted_flights()