class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
        
    def add_flight(self, flight):
        self.flights.append(flight)
        
    def search_by_city(self, city):
        results = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                results.append(flight)
        return results
        
    def search_by_source(self, source):
        results = []
        for flight in self.flights:
            if flight.source == source:
                results.append(flight)
        return results
        
    def search_between_cities(self, source, destination):
        results = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                results.append(flight)
        return results

def print_flight_data(flights):
    if not flights:
        print("No flights found.")
    else:
        print("Flight ID  From  To    Price")
        for flight in flights:
            print(f"{flight.flight_id}  {flight.source}  {flight.destination}  {flight.price}")

# Creating flight objects
flights_data = [
    ("AI161E90", "BLR", "BOM", 5600),
    ("BR161F91", "BOM", "BBI", 6750),
    ("AI161F99", "BBI", "BLR", 8210),
    ("VS171E20", "JLR", "BBI", 5500),
    ("AS171G30", "HYD", "JLR", 4400),
    ("AI131F49", "HYD", "BOM", 3499)
]

flight_table = FlightTable()
for data in flights_data:
    flight_table.add_flight(Flight(*data))

# User interface
while True:
    print("\nSearch options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        city = input("Enter the city: ")
        result = flight_table.search_by_city(city)
        print_flight_data(result)
    elif choice == 2:
        source = input("Enter the source city: ")
        result = flight_table.search_by_source(source)
        print_flight_data(result)
    elif choice == 3:
        source = input("Enter the source city: ")
        destination = input("Enter the destination city: ")
        result = flight_table.search_between_cities(source, destination)
        print_flight_data(result)
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
