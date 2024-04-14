def compare_routes(airlines, operation, airline1, airline2):
    route1 = airlines.get(airline1, set())
    route2 = airlines.get(airline2, set())
    
    if operation == "issubset":
        result = route1.issubset(route2)
        print(result)
    elif operation == "issuperset":
        result = route1.issuperset(route2)
        print(result)
    elif operation == "isdisjoint":
        result = route1.isdisjoint(route2)
        print(result)
    else:
        print("Invalid operation")

airlines = {
    "airline1": {"LAX", "JFK", "CDG", "DXB"},
    "airline2": {"JFK", "CDG", "LHR", "BKK"}
}

while True:
    print("\n1. Compare flight routes")
    print("2. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        operation = input("Enter the operation (issubset, issuperset, isdisjoint): ")
        airline1 = input("Enter the first airline: ")
        airline2 = input("Enter the second airline: ")
        compare_routes(airlines, operation, airline1, airline2)
    elif choice == "2":
        print("Exiting...")
        break
    else:
        print("Invalid input")
