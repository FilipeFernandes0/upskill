#Problem: Implement a flight scheduler system that stores 
#flight information such as airline, origin, destination, and departure time. 
#Allow users to add new flights, search for flights by origin or destination, update flight details, and cancel flights. 
#Each flight is represented as a dictionary with keys for flight number, airline, origin, destination, and departure time. 
#The add_flight function adds a new flight to the scheduler dictionary. The flight is stored with its flight number as the key. 
#The search_by_origin function searches for flights based on the given origin and returns a list of matching flights. 
#The search_by_destination function searches for flights based on the given destination and returns a list of matching flights. 
#The update_flight function updates the details of an existing flight in the scheduler. Any field that is not provided remains unchanged. 
#The cancel_flight function cancels a flight by removing it from the scheduler based on its flight number. 
#print(flight) # Output: {'flight_number': 'GHI789', 'airline': 'Airline C', 'origin': 'London', 'destination': 'Paris', 'departure_time': '16:00'} 
#print(flights_to_denver) # Output: [{'flight_number': 'DEF456', 'airline': 'Airline B', 'origin': 'Chicago', 'destination': 'Denver', 'departure_time': '12:30'}] 
#print(flights_from_ny) # Output: [{'flight_number': 'ABC123', 'airline': 'Airline A', 'origin': 'New York', 'destination': 'Los Angeles', 'departure_time': '09:00'}]  

 
 


#flight = {}
more_avioes = []
flight = {}
def add_flight(number):
    flight = {}
    number = input("what is your flight number: ")
    flight.setdefault("flight number",number)
    airline = input("what is the airline: ")
    flight.setdefault("airline",airline)
    origin = input("origin of the flight: ")
    flight.setdefault("origin",origin)
    destination = input("destination of the flight: ")
    flight.setdefault("destination",destination)
    departure_time = input("what hours is the departure time: ")
    flight.setdefault("departure time",departure_time)
    more_avioes.append(flight)
    return more_avioes
    
def search_by_origin(origin):
    for flight in more_avioes:
        for key , value in flight.items():
            if key in "origin" and value in origin:
                print(flight)
            # if key  in "number" :
            #     print("wrong output")
            # if key in "airline":
            #     print("wrong output")
            # if key in "destination":
            #     print("wrong output")
            # if key in "departure time":
            #     print("wrong output")
        
            #if #key not in "origin":
                #print("wrong output")

def search_by_destination(destination):
    for flight in more_avioes:
        for key,value in flight.items():
            if key in "destination" and value in destination:
                print(flight)


def update_flight():
    menu = int(input("what do you want to update: " " \n " "1 - update number \n 2 - update airline \n 3 - update origin \n 4 - update destination \n 5 - update departure time \n"))
    
    if menu == 1:
        new_number = input("what number you want to change: ")
        for flight in more_avioes:
            if "flight number" in flight:
                flight["flight number"] = new_number
                print(flight)
    elif menu == 2:
        new_airline = input("enter the new airline: ")
        for flight in more_avioes:
            flight["airline"] = new_airline
            print(flight)
    elif menu == 3:
        new_origin = input("enter the new origin: ")
        for flight in more_avioes:
            flight["origin"] = new_origin
            print(flight)
    elif menu == 4:
        new_destination = input("enter the new destination: ")
        for flight in more_avioes:
            flight["destination"] = new_destination
            print(flight)
    elif menu == 5:
        new_departure_time = input("enter the new departure time: ")
        for flight in more_avioes:
            flight["departure time"] = new_departure_time
            print(flight)


def cancel_flight():
    cancel = input("Do you want to cancel the flight: ")
    if cancel == "yes":
        flight.clear()
        print(flight)
    else: 
        #cancel == "no"
        print("your flight wasnt cancelled")
       

while True:
    flight_scheduler = int(input("1 - Add new flight \n" "2 - search for origin \n" "3 - search for destination \n" "4 - update flight details \n" "5 - cancel flights \n" "6 - EXIT \n"))
    if flight_scheduler == 1:
        xcv = None
        add_flight(xcv)
        #more_avioes.append(flight)
        print(more_avioes)
        
    if flight_scheduler == 2:
        origin = input("search for origin: ")
        search_by_origin(origin)
    if flight_scheduler == 3:
        destination = input("search for destination: ")
        search_by_destination(destination)
    if flight_scheduler == 4:
        update_flight()
    if flight_scheduler == 5:
        cancel_flight()
    if flight_scheduler == 6:
        break
        
        
        


